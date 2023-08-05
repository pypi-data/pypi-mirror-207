# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from pydeephaven.proto import object_pb2 as deephaven_dot_proto_dot_object__pb2


class ObjectServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.FetchObject = channel.unary_unary(
                '/io.deephaven.proto.backplane.grpc.ObjectService/FetchObject',
                request_serializer=deephaven_dot_proto_dot_object__pb2.FetchObjectRequest.SerializeToString,
                response_deserializer=deephaven_dot_proto_dot_object__pb2.FetchObjectResponse.FromString,
                )


class ObjectServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def FetchObject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ObjectServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'FetchObject': grpc.unary_unary_rpc_method_handler(
                    servicer.FetchObject,
                    request_deserializer=deephaven_dot_proto_dot_object__pb2.FetchObjectRequest.FromString,
                    response_serializer=deephaven_dot_proto_dot_object__pb2.FetchObjectResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'io.deephaven.proto.backplane.grpc.ObjectService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ObjectService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def FetchObject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.deephaven.proto.backplane.grpc.ObjectService/FetchObject',
            deephaven_dot_proto_dot_object__pb2.FetchObjectRequest.SerializeToString,
            deephaven_dot_proto_dot_object__pb2.FetchObjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
