# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import warnings
from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple, Union

from google.api_core import gapic_v1
from google.api_core import grpc_helpers_async
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore
from grpc.experimental import aio  # type: ignore

from google.cloud.webrisk_v1.types import webrisk
from .base import WebRiskServiceTransport, DEFAULT_CLIENT_INFO
from .grpc import WebRiskServiceGrpcTransport


class WebRiskServiceGrpcAsyncIOTransport(WebRiskServiceTransport):
    """gRPC AsyncIO backend transport for WebRiskService.

    Web Risk API defines an interface to detect malicious URLs on
    your website and in client applications.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _grpc_channel: aio.Channel
    _stubs: Dict[str, Callable] = {}

    @classmethod
    def create_channel(
        cls,
        host: str = "webrisk.googleapis.com",
        credentials: ga_credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> aio.Channel:
        """Create and return a gRPC AsyncIO channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            aio.Channel: A gRPC AsyncIO channel object.
        """

        return grpc_helpers_async.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs,
        )

    def __init__(
        self,
        *,
        host: str = "webrisk.googleapis.com",
        credentials: ga_credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        channel: aio.Channel = None,
        api_mtls_endpoint: str = None,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
        ssl_channel_credentials: grpc.ChannelCredentials = None,
        client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = None,
        quota_project_id=None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            channel (Optional[aio.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or application default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for the grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure a mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Ignore credentials if a channel was passed.
            credentials = False
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None
        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
        )

        if not self._grpc_channel:
            self._grpc_channel = type(self).create_channel(
                self._host,
                credentials=self._credentials,
                credentials_file=credentials_file,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @property
    def grpc_channel(self) -> aio.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Return the channel from cache.
        return self._grpc_channel

    @property
    def compute_threat_list_diff(
        self,
    ) -> Callable[
        [webrisk.ComputeThreatListDiffRequest],
        Awaitable[webrisk.ComputeThreatListDiffResponse],
    ]:
        r"""Return a callable for the compute threat list diff method over gRPC.

        Gets the most recent threat list diffs. These diffs
        should be applied to a local database of hashes to keep
        it up-to-date. If the local database is empty or
        excessively out-of-date, a complete snapshot of the
        database will be returned. This Method only updates a
        single ThreatList at a time. To update multiple
        ThreatList databases, this method needs to be called
        once for each list.

        Returns:
            Callable[[~.ComputeThreatListDiffRequest],
                    Awaitable[~.ComputeThreatListDiffResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "compute_threat_list_diff" not in self._stubs:
            self._stubs["compute_threat_list_diff"] = self.grpc_channel.unary_unary(
                "/google.cloud.webrisk.v1.WebRiskService/ComputeThreatListDiff",
                request_serializer=webrisk.ComputeThreatListDiffRequest.serialize,
                response_deserializer=webrisk.ComputeThreatListDiffResponse.deserialize,
            )
        return self._stubs["compute_threat_list_diff"]

    @property
    def search_uris(
        self,
    ) -> Callable[[webrisk.SearchUrisRequest], Awaitable[webrisk.SearchUrisResponse]]:
        r"""Return a callable for the search uris method over gRPC.

        This method is used to check whether a URI is on a
        given threatList. Multiple threatLists may be searched
        in a single query. The response will list all requested
        threatLists the URI was found to match. If the URI is
        not found on any of the requested ThreatList an empty
        response will be returned.

        Returns:
            Callable[[~.SearchUrisRequest],
                    Awaitable[~.SearchUrisResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_uris" not in self._stubs:
            self._stubs["search_uris"] = self.grpc_channel.unary_unary(
                "/google.cloud.webrisk.v1.WebRiskService/SearchUris",
                request_serializer=webrisk.SearchUrisRequest.serialize,
                response_deserializer=webrisk.SearchUrisResponse.deserialize,
            )
        return self._stubs["search_uris"]

    @property
    def search_hashes(
        self,
    ) -> Callable[
        [webrisk.SearchHashesRequest], Awaitable[webrisk.SearchHashesResponse]
    ]:
        r"""Return a callable for the search hashes method over gRPC.

        Gets the full hashes that match the requested hash
        prefix. This is used after a hash prefix is looked up in
        a threatList and there is a match. The client side
        threatList only holds partial hashes so the client must
        query this method to determine if there is a full hash
        match of a threat.

        Returns:
            Callable[[~.SearchHashesRequest],
                    Awaitable[~.SearchHashesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_hashes" not in self._stubs:
            self._stubs["search_hashes"] = self.grpc_channel.unary_unary(
                "/google.cloud.webrisk.v1.WebRiskService/SearchHashes",
                request_serializer=webrisk.SearchHashesRequest.serialize,
                response_deserializer=webrisk.SearchHashesResponse.deserialize,
            )
        return self._stubs["search_hashes"]

    @property
    def create_submission(
        self,
    ) -> Callable[[webrisk.CreateSubmissionRequest], Awaitable[webrisk.Submission]]:
        r"""Return a callable for the create submission method over gRPC.

        Creates a Submission of a URI suspected of containing phishing
        content to be reviewed. If the result verifies the existence of
        malicious phishing content, the site will be added to the
        `Google's Social Engineering
        lists <https://support.google.com/webmasters/answer/6350487/>`__
        in order to protect users that could get exposed to this threat
        in the future. Only projects with CREATE_SUBMISSION_USERS
        visibility can use this method.

        Returns:
            Callable[[~.CreateSubmissionRequest],
                    Awaitable[~.Submission]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_submission" not in self._stubs:
            self._stubs["create_submission"] = self.grpc_channel.unary_unary(
                "/google.cloud.webrisk.v1.WebRiskService/CreateSubmission",
                request_serializer=webrisk.CreateSubmissionRequest.serialize,
                response_deserializer=webrisk.Submission.deserialize,
            )
        return self._stubs["create_submission"]

    def close(self):
        return self.grpc_channel.close()


__all__ = ("WebRiskServiceGrpcAsyncIOTransport",)
