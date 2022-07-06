
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ....bitsong.fantoken.v1beta1 import query_pb2 as bitsong_dot_fantoken_dot_v1beta1_dot_query__pb2

class QueryStub(object):
    'Query creates service with fantoken as RPC\n    '

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.FanToken = channel.unary_unary('/bitsong.fantoken.v1beta1.Query/FanToken', request_serializer=bitsong_dot_fantoken_dot_v1beta1_dot_query__pb2.QueryFanTokenRequest.SerializeToString, response_deserializer=bitsong_dot_fantoken_dot_v1beta1_dot_query__pb2.QueryFanTokenResponse.FromString)
        self.FanTokens = channel.unary_unary('/bitsong.fantoken.v1beta1.Query/FanTokens', request_serializer=bitsong_dot_fantoken_dot_v1beta1_dot_query__pb2.QueryFanTokensRequest.SerializeToString, response_deserializer=bitsong_dot_fantoken_dot_v1beta1_dot_query__pb2.QueryFanTokensResponse.FromString)
        self.Params = channel.unary_unary('/bitsong.fantoken.v1beta1.Query/Params', request_serializer=bitsong_dot_fantoken_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, response_deserializer=bitsong_dot_fantoken_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString)

class QueryServicer(object):
    'Query creates service with fantoken as RPC\n    '

    def FanToken(self, request, context):
        'FanToken returns fantoken with fantoken name\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FanTokens(self, request, context):
        'FanTokens returns the fantoken list\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Params(self, request, context):
        'Params queries the fantoken parameters\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'FanToken': grpc.unary_unary_rpc_method_handler(servicer.FanToken, request_deserializer=bitsong_dot_fantoken_dot_v1beta1_dot_query__pb2.QueryFanTokenRequest.FromString, response_serializer=bitsong_dot_fantoken_dot_v1beta1_dot_query__pb2.QueryFanTokenResponse.SerializeToString), 'FanTokens': grpc.unary_unary_rpc_method_handler(servicer.FanTokens, request_deserializer=bitsong_dot_fantoken_dot_v1beta1_dot_query__pb2.QueryFanTokensRequest.FromString, response_serializer=bitsong_dot_fantoken_dot_v1beta1_dot_query__pb2.QueryFanTokensResponse.SerializeToString), 'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=bitsong_dot_fantoken_dot_v1beta1_dot_query__pb2.QueryParamsRequest.FromString, response_serializer=bitsong_dot_fantoken_dot_v1beta1_dot_query__pb2.QueryParamsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('bitsong.fantoken.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    'Query creates service with fantoken as RPC\n    '

    @staticmethod
    def FanToken(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bitsong.fantoken.v1beta1.Query/FanToken', bitsong_dot_fantoken_dot_v1beta1_dot_query__pb2.QueryFanTokenRequest.SerializeToString, bitsong_dot_fantoken_dot_v1beta1_dot_query__pb2.QueryFanTokenResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FanTokens(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bitsong.fantoken.v1beta1.Query/FanTokens', bitsong_dot_fantoken_dot_v1beta1_dot_query__pb2.QueryFanTokensRequest.SerializeToString, bitsong_dot_fantoken_dot_v1beta1_dot_query__pb2.QueryFanTokensResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bitsong.fantoken.v1beta1.Query/Params', bitsong_dot_fantoken_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, bitsong_dot_fantoken_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
