
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ....osmosis.mint.v1beta1 import query_pb2 as osmosis_dot_mint_dot_v1beta1_dot_query__pb2

class QueryStub(object):
    'Query provides defines the gRPC querier service.\n    '

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.Params = channel.unary_unary('/osmosis.mint.v1beta1.Query/Params', request_serializer=osmosis_dot_mint_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, response_deserializer=osmosis_dot_mint_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString)
        self.EpochProvisions = channel.unary_unary('/osmosis.mint.v1beta1.Query/EpochProvisions', request_serializer=osmosis_dot_mint_dot_v1beta1_dot_query__pb2.QueryEpochProvisionsRequest.SerializeToString, response_deserializer=osmosis_dot_mint_dot_v1beta1_dot_query__pb2.QueryEpochProvisionsResponse.FromString)

class QueryServicer(object):
    'Query provides defines the gRPC querier service.\n    '

    def Params(self, request, context):
        'Params returns the total set of minting parameters.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EpochProvisions(self, request, context):
        'EpochProvisions current minting epoch provisions value.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=osmosis_dot_mint_dot_v1beta1_dot_query__pb2.QueryParamsRequest.FromString, response_serializer=osmosis_dot_mint_dot_v1beta1_dot_query__pb2.QueryParamsResponse.SerializeToString), 'EpochProvisions': grpc.unary_unary_rpc_method_handler(servicer.EpochProvisions, request_deserializer=osmosis_dot_mint_dot_v1beta1_dot_query__pb2.QueryEpochProvisionsRequest.FromString, response_serializer=osmosis_dot_mint_dot_v1beta1_dot_query__pb2.QueryEpochProvisionsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('osmosis.mint.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    'Query provides defines the gRPC querier service.\n    '

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.mint.v1beta1.Query/Params', osmosis_dot_mint_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, osmosis_dot_mint_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EpochProvisions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.mint.v1beta1.Query/EpochProvisions', osmosis_dot_mint_dot_v1beta1_dot_query__pb2.QueryEpochProvisionsRequest.SerializeToString, osmosis_dot_mint_dot_v1beta1_dot_query__pb2.QueryEpochProvisionsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
