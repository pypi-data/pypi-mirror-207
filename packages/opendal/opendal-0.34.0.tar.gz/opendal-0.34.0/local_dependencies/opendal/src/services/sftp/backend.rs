// Licensed to the Apache Software Foundation (ASF) under one
// or more contributor license agreements.  See the NOTICE file
// distributed with this work for additional information
// regarding copyright ownership.  The ASF licenses this file
// to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance
// with the License.  You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing,
// software distributed under the License is distributed on an
// "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
// KIND, either express or implied.  See the License for the
// specific language governing permissions and limitations
// under the License.

use std::cmp::min;
use std::collections::HashMap;
use std::fmt::Debug;
use std::fmt::Formatter;

use async_trait::async_trait;
use bb8::PooledConnection;
use futures::executor::block_on;
use log::debug;
use openssh::RemoteChild;
use openssh::Session;
use openssh::SessionBuilder;
use openssh::Stdio;
use openssh_sftp_client::Sftp;
use owning_ref::OwningHandle;
use tokio::sync::OnceCell;

use super::error::is_not_found;
use super::error::is_sftp_protocol_error;
use super::error::SftpError;
use super::pager::SftpPager;
use super::utils::SftpReader;
use super::writer::SftpWriter;
use crate::ops::*;
use crate::raw::*;
use crate::*;

/// SFTP services support. (only works on unix)
///
/// # Capabilities
///
/// This service can be used to:
///
/// - [x] read
/// - [x] write
/// - [x] list
/// - [ ] ~~scan~~
/// - [ ] ~~presign~~
/// - [ ] blocking
///
/// - [x] stat
/// - [x] read
/// - [x] write
/// - [x] create_dir
/// - [x] delete
/// - [ ] copy
/// - [ ] rename
/// - [x] list
/// - [ ] ~~scan~~
/// - [ ] ~~presign~~
/// - [ ] blocking
///
/// # Configuration
///
/// - `endpoint`: Set the endpoint for connection
/// - `root`: Set the work directory for backend, default to `/home/$USER/`
/// - `user`: Set the login user
/// - `key`: Set the public key for login
///
/// It doesn't support password login, you can use public key instead.
///
/// You can refer to [`SftpBuilder`]'s docs for more information
///
/// # Example
///
/// ## Via Builder
///
/// ```no_run
/// use anyhow::Result;
/// use opendal::services::Ftp;
/// use opendal::Object;
/// use opendal::Operator;
///
/// #[tokio::main]
/// async fn main() -> Result<()> {
///     // create backend builder
///     let mut builder = Sftp::default();
///
///     builder.endpoint("127.0.0.1").user("test").password("test");
///
///     let op: Operator = Operator::new(builder)?.finish();
///     let _obj: Object = op.object("test_file");
///     Ok(())
/// }
/// ```

#[derive(Default)]
pub struct SftpBuilder {
    endpoint: Option<String>,
    root: Option<String>,
    user: Option<String>,
    key: Option<String>,
}

impl Debug for SftpBuilder {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        f.debug_struct("Builder")
            .field("endpoint", &self.endpoint)
            .field("root", &self.root)
            .finish()
    }
}

impl SftpBuilder {
    /// set endpoint for sftp backend.
    pub fn endpoint(&mut self, endpoint: &str) -> &mut Self {
        self.endpoint = if endpoint.is_empty() {
            None
        } else {
            Some(endpoint.to_string())
        };

        self
    }

    /// set root path for sftp backend.
    pub fn root(&mut self, root: &str) -> &mut Self {
        self.root = if root.is_empty() {
            None
        } else {
            Some(root.to_string())
        };

        self
    }

    /// set user for sftp backend.
    pub fn user(&mut self, user: &str) -> &mut Self {
        self.user = if user.is_empty() {
            None
        } else {
            Some(user.to_string())
        };

        self
    }

    /// set key path for sftp backend.
    pub fn key(&mut self, key: &str) -> &mut Self {
        self.key = if key.is_empty() {
            None
        } else {
            Some(key.to_string())
        };

        self
    }
}

impl Builder for SftpBuilder {
    const SCHEME: Scheme = Scheme::Sftp;
    type Accessor = SftpBackend;

    fn build(&mut self) -> Result<Self::Accessor> {
        debug!("sftp backend build started: {:?}", &self);
        let endpoint = match self.endpoint.clone() {
            Some(v) => v,
            None => return Err(Error::new(ErrorKind::ConfigInvalid, "endpoint is empty")),
        };

        let user = match self.user.clone() {
            Some(v) => v,
            None => return Err(Error::new(ErrorKind::ConfigInvalid, "user is empty")),
        };

        let root = self
            .root
            .clone()
            .map(|r| normalize_root(r.as_str()))
            .unwrap_or(format!("/home/{}/", user));

        debug!("sftp backend finished: {:?}", &self);

        Ok(SftpBackend {
            endpoint,
            root,
            user,
            key: self.key.clone(),
            sftp: OnceCell::new(),
        })
    }

    fn from_map(map: HashMap<String, String>) -> Self {
        let mut builder = SftpBuilder::default();

        map.get("root").map(|v| builder.root(v));
        map.get("endpoint").map(|v| builder.endpoint(v));
        map.get("user").map(|v| builder.user(v));
        map.get("key").map(|v| builder.key(v));

        builder
    }
}

#[derive(Clone)]
pub struct Manager {
    endpoint: String,
    user: String,
    key: Option<String>,
}

pub struct Connection {
    // the remote child owns the ref to session, so we need to use owning handle
    // The session will only create one child, so we can make sure the child can live
    // as long as the session. (the session will be dropped when the connection is dropped)
    // Related: https://stackoverflow.com/a/47260399
    child: OwningHandle<Box<Session>, Box<RemoteChild<'static>>>,
    pub sftp: Sftp,
}

#[async_trait]
impl bb8::ManageConnection for Manager {
    type Connection = Connection;
    type Error = SftpError;

    async fn connect(&self) -> std::result::Result<Self::Connection, Self::Error> {
        let mut session = SessionBuilder::default();

        session.user(self.user.clone());

        if let Some(key) = &self.key {
            session.keyfile(key);
        }

        let session = session.connect(self.endpoint.clone()).await?;

        let sess = Box::new(session);
        let mut oref = OwningHandle::new_with_fn(sess, unsafe {
            |x| {
                Box::new(
                    block_on(
                        (*x).subsystem("sftp")
                            .stdin(Stdio::piped())
                            .stdout(Stdio::piped())
                            .spawn(),
                    )
                    .unwrap(),
                )
            }
        });

        let sftp = Sftp::new(
            oref.stdin().take().unwrap(),
            oref.stdout().take().unwrap(),
            Default::default(),
        )
        .await?;

        Ok(Connection { child: oref, sftp })
    }

    async fn is_valid(&self, conn: &mut Self::Connection) -> std::result::Result<(), Self::Error> {
        conn.child.session().check().await?;
        Ok(())
    }

    /// Always allow reuse conn.
    fn has_broken(&self, _: &mut Self::Connection) -> bool {
        false
    }
}

/// Backend is used to serve `Accessor` support for sftp.
pub struct SftpBackend {
    endpoint: String,
    root: String,
    user: String,
    key: Option<String>,
    sftp: OnceCell<bb8::Pool<Manager>>,
}

impl Debug for SftpBackend {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        f.debug_struct("Backend").finish()
    }
}

#[async_trait]
impl Accessor for SftpBackend {
    type Reader = SftpReader;
    type BlockingReader = ();
    type Writer = SftpWriter;
    type BlockingWriter = ();
    type Pager = SftpPager;
    type BlockingPager = ();

    fn info(&self) -> AccessorInfo {
        let mut am = AccessorInfo::default();
        am.set_root(self.root.as_str())
            .set_scheme(Scheme::Sftp)
            .set_capability(Capability {
                stat: true,

                read: true,

                write: true,
                create_dir: true,
                delete: true,

                list: true,
                list_with_limit: true,
                list_with_delimiter_slash: true,

                ..Default::default()
            });

        am
    }

    async fn create_dir(&self, path: &str, _: OpCreateDir) -> Result<RpCreateDir> {
        let client = self.sftp_connect().await?;
        let mut fs = client.sftp.fs();
        fs.set_cwd(self.root.clone());

        let paths: Vec<&str> = path.split_inclusive('/').collect();
        let mut current = self.root.clone();
        for p in paths {
            if p.is_empty() {
                continue;
            }

            current.push_str(p);
            let res = fs.create_dir(p).await;

            if let Err(e) = res {
                // ignore error if dir already exists
                if !is_sftp_protocol_error(&e) {
                    return Err(e.into());
                }
            }
            fs.set_cwd(current.clone());
        }

        return Ok(RpCreateDir::default());
    }

    async fn read(&self, path: &str, args: OpRead) -> Result<(RpRead, Self::Reader)> {
        let client = self.sftp_connect().await?;

        let mut fs = client.sftp.fs();
        fs.set_cwd(self.root.clone());
        let path = fs.canonicalize(path).await?;

        let mut file = client.sftp.open(path.as_path()).await?;

        let total_length = file.metadata().await?.len().ok_or(Error::new(
            ErrorKind::NotFound,
            format!("file not found: {}", path.to_str().unwrap()).as_str(),
        ))?;

        let br = args.range();
        let (start, end) = match (br.offset(), br.size()) {
            // Read a specific range.
            (Some(offset), Some(size)) => (offset, min(offset + size, total_length)),
            // Read from offset.
            (Some(offset), None) => (offset, total_length),
            // Read the last size bytes.
            (None, Some(size)) => (
                if total_length > size {
                    total_length - size
                } else {
                    0
                },
                total_length,
            ),
            // Read the whole file.
            (None, None) => (0, total_length),
        };

        let r = SftpReader::new(self.sftp_connect_owned().await?, path, start, end).await?;

        Ok((RpRead::new(end - start), r))
    }

    async fn write(&self, path: &str, args: OpWrite) -> Result<(RpWrite, Self::Writer)> {
        if args.content_length().is_none() {
            return Err(Error::new(
                ErrorKind::Unsupported,
                "write without content length is not supported",
            ));
        }

        if let Some((dir, _)) = path.rsplit_once('/') {
            self.create_dir(dir, OpCreateDir::default()).await?;
        }

        let path = format!("{}{}", self.root, path);

        Ok((
            RpWrite::new(),
            SftpWriter::new(self.sftp_connect_owned().await?, path),
        ))
    }

    async fn stat(&self, path: &str, _: OpStat) -> Result<RpStat> {
        let client = self.sftp_connect().await?;
        let mut fs = client.sftp.fs();
        fs.set_cwd(self.root.clone());

        let meta = fs.metadata(path).await?;

        Ok(RpStat::new(meta.into()))
    }

    async fn delete(&self, path: &str, _: OpDelete) -> Result<RpDelete> {
        let client = self.sftp_connect().await?;

        let mut fs = client.sftp.fs();
        fs.set_cwd(self.root.clone());

        if path.ends_with('/') {
            let file_path = format!("./{}", path);
            let dir = match fs.open_dir(file_path.clone()).await {
                Ok(dir) => dir,
                Err(e) => {
                    if is_not_found(&e) {
                        return Ok(RpDelete::default());
                    } else {
                        return Err(e.into());
                    }
                }
            }
            .read_dir()
            .await?;

            for file in &dir {
                let file_name = file.filename().to_str().unwrap();
                if file_name == "." || file_name == ".." {
                    continue;
                }
                let file_path = format!("{}{}", path, file_name);
                self.delete(file_path.as_str(), OpDelete::default()).await?;
            }

            match fs.remove_dir(path).await {
                Err(e) if !is_not_found(&e) => {
                    return Err(e.into());
                }
                _ => {}
            }
        } else {
            match fs.remove_file(path).await {
                Err(e) if !is_not_found(&e) => {
                    return Err(e.into());
                }
                _ => {}
            }
        };

        Ok(RpDelete::default())
    }

    async fn list(&self, path: &str, args: OpList) -> Result<(RpList, Self::Pager)> {
        let client = self.sftp_connect().await?;
        let mut fs = client.sftp.fs();
        fs.set_cwd(self.root.clone());

        let file_path = format!("./{}", path);

        let mut dir = match fs.open_dir(file_path.clone()).await {
            Ok(dir) => dir,
            Err(e) => {
                if is_not_found(&e) {
                    return Ok((RpList::default(), SftpPager::empty()));
                } else {
                    return Err(e.into());
                }
            }
        };
        let dir = dir.read_dir().await?;

        Ok((
            RpList::default(),
            SftpPager::new(dir.into_inner(), path.to_owned(), args.limit()),
        ))
    }
}

impl SftpBackend {
    async fn pool(&self) -> Result<&bb8::Pool<Manager>> {
        let pool = self
            .sftp
            .get_or_try_init(|| async {
                let manager = Manager {
                    endpoint: self.endpoint.clone(),
                    user: self.user.clone(),
                    key: self.key.clone(),
                };

                bb8::Pool::builder().max_size(10).build(manager).await
            })
            .await?;

        Ok(pool)
    }

    pub async fn sftp_connect(&self) -> Result<PooledConnection<'_, Manager>> {
        let conn = self.pool().await?.get().await?;

        Ok(conn)
    }

    pub async fn sftp_connect_owned(&self) -> Result<PooledConnection<'static, Manager>> {
        let conn = self.pool().await?.get_owned().await?;

        Ok(conn)
    }
}
