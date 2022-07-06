
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ....bitsong.merkledrop.v1beta1 import query_pb2 as bitsong_dot_merkledrop_dot_v1beta1_dot_query__pb2

class QueryStub(object):
    'Missing associated documentation comment in .proto file.'

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.Merkledrop = channel.unary_unary('/bitsong.merkledrop.v1beta1.Query/Merkledrop', request_serializer=bitsong_dot_merkledrop_dot_v1beta1_dot_query__pb2.QueryMerkledropRequest.SerializeToString, response_deserializer=bitsong_dot_merkledrop_dot_v1beta1_dot_query__pb2.QueryMerkledropResponse.FromString)
        self.IndexClaimed = channel.unary_unary('/bitsong.merkledrop.v1beta1.Query/IndexClaimed', request_serializer=bitsong_dot_merkledrop_dot_v1beta1_dot_query__pb2.QueryIndexClaimedRequest.SerializeToString, response_deserializer=bitsong_dot_merkledrop_dot_v1beta1_dot_query__pb2.QueryIndexClaimedResponse.FromString)
        self.Params = channel.unary_unary('/bitsong.merkledrop.v1beta1.Query/Params', request_serializer=bitsong_dot_merkledrop_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, response_deserializer=bitsong_dot_merkledrop_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString)

class QueryServicer(object):
    'Missing associated documentation comment in .proto file.'

    def Merkledrop(self, request, context):
        'Missing associated documentation comment in .proto file.'
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IndexClaimed(self, request, context):
        'Missing associated documentation comment in .proto file.'
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Params(self, request, context):
        'Params queries the fantoken parameters\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Merkledrop': grpc.unary_unary_rpc_method_handler(servicer.Merkledrop, request_deserializer=bitsong_dot_merkledrop_dot_v1beta1_dot_query__pb2.QueryMerkledropRequest.FromString, response_serializer=bitsong_dot_merkledrop_dot_v1beta1_dot_query__pb2.QueryMerkledropResponse.SerializeToString), 'IndexClaimed': grpc.unary_unary_rpc_method_handler(servicer.IndexClaimed, request_deserializer=bitsong_dot_merkledrop_dot_v1beta1_dot_query__pb2.QueryIndexClaimedRequest.FromString, response_serializer=bitsong_dot_merkledrop_dot_v1beta1_dot_query__pb2.QueryIndexClaimedResponse.SerializeToString), 'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=bitsong_dot_merkledrop_dot_v1beta1_dot_query__pb2.QueryParamsRequest.FromString, response_serializer=bitsong_dot_merkledrop_dot_v1beta1_dot_query__pb2.QueryParamsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('bitsong.merkledrop.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    'Missing associated documentation comment in .proto file.'

    @staticmethod
    def Merkledrop(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bitsong.merkledrop.v1beta1.Query/Merkledrop', bitsong_dot_merkledrop_dot_v1beta1_dot_query__pb2.QueryMerkledropRequest.SerializeToString, bitsong_dot_merkledrop_dot_v1beta1_dot_query__pb2.QueryMerkledropResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IndexClaimed(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bitsong.merkledrop.v1beta1.Query/IndexClaimed', bitsong_dot_merkledrop_dot_v1beta1_dot_query__pb2.QueryIndexClaimedRequest.SerializeToString, bitsong_dot_merkledrop_dot_v1beta1_dot_query__pb2.QueryIndexClaimedResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bitsong.merkledrop.v1beta1.Query/Params', bitsong_dot_merkledrop_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, bitsong_dot_merkledrop_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
