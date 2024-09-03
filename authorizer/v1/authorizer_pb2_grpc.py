# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from authorizer.v1 import authorizer_pb2 as authorizer_dot_v1_dot_authorizer__pb2


class AuthorizerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Authorize = channel.unary_unary(
                '/authorizer.v1.AuthorizerService/Authorize',
                request_serializer=authorizer_dot_v1_dot_authorizer__pb2.AuthorizeRequest.SerializeToString,
                response_deserializer=authorizer_dot_v1_dot_authorizer__pb2.AuthorizeResponse.FromString,
                )
        self.Ping = channel.unary_unary(
                '/authorizer.v1.AuthorizerService/Ping',
                request_serializer=authorizer_dot_v1_dot_authorizer__pb2.PingRequest.SerializeToString,
                response_deserializer=authorizer_dot_v1_dot_authorizer__pb2.PingResponse.FromString,
                )
        self.AuthorizeV2 = channel.unary_unary(
                '/authorizer.v1.AuthorizerService/AuthorizeV2',
                request_serializer=authorizer_dot_v1_dot_authorizer__pb2.AuthorizeV2Request.SerializeToString,
                response_deserializer=authorizer_dot_v1_dot_authorizer__pb2.AuthorizeV2Response.FromString,
                )


class AuthorizerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Authorize(self, request, context):
        """Authorize authorizes an S3 request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Ping(self, request, context):
        """Ping allows us to (a) check and test the connection to the authorizer,
        and (b) easily avoid the lazy initialization behaviour of the gRPC
        channel, so we can give helpful error messages at startup.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AuthorizeV2(self, request, context):
        """A request for authorization. Provide easily-available information about
        the request such as user, bucket and object key, so that the Authorizer
        can work out what additional data it will need to make a proper
        decision. Failures here will result in the user getting an error
        message. An Allow or Deny code means the protocol is ended. An 'extra
        data required' code means the client should either fail authorization
        or submit another Authorize() request with the required data.

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthorizerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Authorize': grpc.unary_unary_rpc_method_handler(
                    servicer.Authorize,
                    request_deserializer=authorizer_dot_v1_dot_authorizer__pb2.AuthorizeRequest.FromString,
                    response_serializer=authorizer_dot_v1_dot_authorizer__pb2.AuthorizeResponse.SerializeToString,
            ),
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=authorizer_dot_v1_dot_authorizer__pb2.PingRequest.FromString,
                    response_serializer=authorizer_dot_v1_dot_authorizer__pb2.PingResponse.SerializeToString,
            ),
            'AuthorizeV2': grpc.unary_unary_rpc_method_handler(
                    servicer.AuthorizeV2,
                    request_deserializer=authorizer_dot_v1_dot_authorizer__pb2.AuthorizeV2Request.FromString,
                    response_serializer=authorizer_dot_v1_dot_authorizer__pb2.AuthorizeV2Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'authorizer.v1.AuthorizerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AuthorizerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Authorize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authorizer.v1.AuthorizerService/Authorize',
            authorizer_dot_v1_dot_authorizer__pb2.AuthorizeRequest.SerializeToString,
            authorizer_dot_v1_dot_authorizer__pb2.AuthorizeResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authorizer.v1.AuthorizerService/Ping',
            authorizer_dot_v1_dot_authorizer__pb2.PingRequest.SerializeToString,
            authorizer_dot_v1_dot_authorizer__pb2.PingResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AuthorizeV2(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authorizer.v1.AuthorizerService/AuthorizeV2',
            authorizer_dot_v1_dot_authorizer__pb2.AuthorizeV2Request.SerializeToString,
            authorizer_dot_v1_dot_authorizer__pb2.AuthorizeV2Response.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
