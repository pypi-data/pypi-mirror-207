# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from pydeephaven.proto import storage_pb2 as deephaven_dot_proto_dot_storage__pb2


class StorageServiceStub(object):
    """
    Shared storage management service.

    Operations may fail (or omit data) if the current session does not have permission to read or write that resource.

    Paths will be "/" delimited and must start with a leading slash.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListItems = channel.unary_unary(
                '/io.deephaven.proto.backplane.grpc.StorageService/ListItems',
                request_serializer=deephaven_dot_proto_dot_storage__pb2.ListItemsRequest.SerializeToString,
                response_deserializer=deephaven_dot_proto_dot_storage__pb2.ListItemsResponse.FromString,
                )
        self.FetchFile = channel.unary_unary(
                '/io.deephaven.proto.backplane.grpc.StorageService/FetchFile',
                request_serializer=deephaven_dot_proto_dot_storage__pb2.FetchFileRequest.SerializeToString,
                response_deserializer=deephaven_dot_proto_dot_storage__pb2.FetchFileResponse.FromString,
                )
        self.SaveFile = channel.unary_unary(
                '/io.deephaven.proto.backplane.grpc.StorageService/SaveFile',
                request_serializer=deephaven_dot_proto_dot_storage__pb2.SaveFileRequest.SerializeToString,
                response_deserializer=deephaven_dot_proto_dot_storage__pb2.SaveFileResponse.FromString,
                )
        self.MoveItem = channel.unary_unary(
                '/io.deephaven.proto.backplane.grpc.StorageService/MoveItem',
                request_serializer=deephaven_dot_proto_dot_storage__pb2.MoveItemRequest.SerializeToString,
                response_deserializer=deephaven_dot_proto_dot_storage__pb2.MoveItemResponse.FromString,
                )
        self.CreateDirectory = channel.unary_unary(
                '/io.deephaven.proto.backplane.grpc.StorageService/CreateDirectory',
                request_serializer=deephaven_dot_proto_dot_storage__pb2.CreateDirectoryRequest.SerializeToString,
                response_deserializer=deephaven_dot_proto_dot_storage__pb2.CreateDirectoryResponse.FromString,
                )
        self.DeleteItem = channel.unary_unary(
                '/io.deephaven.proto.backplane.grpc.StorageService/DeleteItem',
                request_serializer=deephaven_dot_proto_dot_storage__pb2.DeleteItemRequest.SerializeToString,
                response_deserializer=deephaven_dot_proto_dot_storage__pb2.DeleteItemResponse.FromString,
                )


class StorageServiceServicer(object):
    """
    Shared storage management service.

    Operations may fail (or omit data) if the current session does not have permission to read or write that resource.

    Paths will be "/" delimited and must start with a leading slash.
    """

    def ListItems(self, request, context):
        """Lists the files and directories present in a given directory. Will return an error
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FetchFile(self, request, context):
        """Reads the file at the given path. Client can optionally specify an etag, asking the server
        not to send the file if it hasn't changed.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SaveFile(self, request, context):
        """Can create new files or modify existing with client provided contents.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MoveItem(self, request, context):
        """Moves a file from one path to another.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateDirectory(self, request, context):
        """Creates a directory at the given path.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteItem(self, request, context):
        """Deletes the file or directory at the given path. Directories must be empty to be deleted.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StorageServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListItems': grpc.unary_unary_rpc_method_handler(
                    servicer.ListItems,
                    request_deserializer=deephaven_dot_proto_dot_storage__pb2.ListItemsRequest.FromString,
                    response_serializer=deephaven_dot_proto_dot_storage__pb2.ListItemsResponse.SerializeToString,
            ),
            'FetchFile': grpc.unary_unary_rpc_method_handler(
                    servicer.FetchFile,
                    request_deserializer=deephaven_dot_proto_dot_storage__pb2.FetchFileRequest.FromString,
                    response_serializer=deephaven_dot_proto_dot_storage__pb2.FetchFileResponse.SerializeToString,
            ),
            'SaveFile': grpc.unary_unary_rpc_method_handler(
                    servicer.SaveFile,
                    request_deserializer=deephaven_dot_proto_dot_storage__pb2.SaveFileRequest.FromString,
                    response_serializer=deephaven_dot_proto_dot_storage__pb2.SaveFileResponse.SerializeToString,
            ),
            'MoveItem': grpc.unary_unary_rpc_method_handler(
                    servicer.MoveItem,
                    request_deserializer=deephaven_dot_proto_dot_storage__pb2.MoveItemRequest.FromString,
                    response_serializer=deephaven_dot_proto_dot_storage__pb2.MoveItemResponse.SerializeToString,
            ),
            'CreateDirectory': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateDirectory,
                    request_deserializer=deephaven_dot_proto_dot_storage__pb2.CreateDirectoryRequest.FromString,
                    response_serializer=deephaven_dot_proto_dot_storage__pb2.CreateDirectoryResponse.SerializeToString,
            ),
            'DeleteItem': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteItem,
                    request_deserializer=deephaven_dot_proto_dot_storage__pb2.DeleteItemRequest.FromString,
                    response_serializer=deephaven_dot_proto_dot_storage__pb2.DeleteItemResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'io.deephaven.proto.backplane.grpc.StorageService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StorageService(object):
    """
    Shared storage management service.

    Operations may fail (or omit data) if the current session does not have permission to read or write that resource.

    Paths will be "/" delimited and must start with a leading slash.
    """

    @staticmethod
    def ListItems(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.deephaven.proto.backplane.grpc.StorageService/ListItems',
            deephaven_dot_proto_dot_storage__pb2.ListItemsRequest.SerializeToString,
            deephaven_dot_proto_dot_storage__pb2.ListItemsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FetchFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.deephaven.proto.backplane.grpc.StorageService/FetchFile',
            deephaven_dot_proto_dot_storage__pb2.FetchFileRequest.SerializeToString,
            deephaven_dot_proto_dot_storage__pb2.FetchFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SaveFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.deephaven.proto.backplane.grpc.StorageService/SaveFile',
            deephaven_dot_proto_dot_storage__pb2.SaveFileRequest.SerializeToString,
            deephaven_dot_proto_dot_storage__pb2.SaveFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MoveItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.deephaven.proto.backplane.grpc.StorageService/MoveItem',
            deephaven_dot_proto_dot_storage__pb2.MoveItemRequest.SerializeToString,
            deephaven_dot_proto_dot_storage__pb2.MoveItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateDirectory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.deephaven.proto.backplane.grpc.StorageService/CreateDirectory',
            deephaven_dot_proto_dot_storage__pb2.CreateDirectoryRequest.SerializeToString,
            deephaven_dot_proto_dot_storage__pb2.CreateDirectoryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.deephaven.proto.backplane.grpc.StorageService/DeleteItem',
            deephaven_dot_proto_dot_storage__pb2.DeleteItemRequest.SerializeToString,
            deephaven_dot_proto_dot_storage__pb2.DeleteItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
