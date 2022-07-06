
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ...osmosis.epochs import query_pb2 as osmosis_dot_epochs_dot_query__pb2

class QueryStub(object):
    'Query defines the gRPC querier service.\n    '

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.EpochInfos = channel.unary_unary('/osmosis.epochs.v1beta1.Query/EpochInfos', request_serializer=osmosis_dot_epochs_dot_query__pb2.QueryEpochsInfoRequest.SerializeToString, response_deserializer=osmosis_dot_epochs_dot_query__pb2.QueryEpochsInfoResponse.FromString)
        self.CurrentEpoch = channel.unary_unary('/osmosis.epochs.v1beta1.Query/CurrentEpoch', request_serializer=osmosis_dot_epochs_dot_query__pb2.QueryCurrentEpochRequest.SerializeToString, response_deserializer=osmosis_dot_epochs_dot_query__pb2.QueryCurrentEpochResponse.FromString)

class QueryServicer(object):
    'Query defines the gRPC querier service.\n    '

    def EpochInfos(self, request, context):
        'EpochInfos provide running epochInfos\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CurrentEpoch(self, request, context):
        'CurrentEpoch provide current epoch of specified identifier\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'EpochInfos': grpc.unary_unary_rpc_method_handler(servicer.EpochInfos, request_deserializer=osmosis_dot_epochs_dot_query__pb2.QueryEpochsInfoRequest.FromString, response_serializer=osmosis_dot_epochs_dot_query__pb2.QueryEpochsInfoResponse.SerializeToString), 'CurrentEpoch': grpc.unary_unary_rpc_method_handler(servicer.CurrentEpoch, request_deserializer=osmosis_dot_epochs_dot_query__pb2.QueryCurrentEpochRequest.FromString, response_serializer=osmosis_dot_epochs_dot_query__pb2.QueryCurrentEpochResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('osmosis.epochs.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    'Query defines the gRPC querier service.\n    '

    @staticmethod
    def EpochInfos(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.epochs.v1beta1.Query/EpochInfos', osmosis_dot_epochs_dot_query__pb2.QueryEpochsInfoRequest.SerializeToString, osmosis_dot_epochs_dot_query__pb2.QueryEpochsInfoResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CurrentEpoch(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.epochs.v1beta1.Query/CurrentEpoch', osmosis_dot_epochs_dot_query__pb2.QueryCurrentEpochRequest.SerializeToString, osmosis_dot_epochs_dot_query__pb2.QueryCurrentEpochResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
