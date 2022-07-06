
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ....osmosis.txfees.v1beta1 import query_pb2 as osmosis_dot_txfees_dot_v1beta1_dot_query__pb2

class QueryStub(object):
    'Missing associated documentation comment in .proto file.'

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.FeeTokens = channel.unary_unary('/osmosis.txfees.v1beta1.Query/FeeTokens', request_serializer=osmosis_dot_txfees_dot_v1beta1_dot_query__pb2.QueryFeeTokensRequest.SerializeToString, response_deserializer=osmosis_dot_txfees_dot_v1beta1_dot_query__pb2.QueryFeeTokensResponse.FromString)
        self.DenomSpotPrice = channel.unary_unary('/osmosis.txfees.v1beta1.Query/DenomSpotPrice', request_serializer=osmosis_dot_txfees_dot_v1beta1_dot_query__pb2.QueryDenomSpotPriceRequest.SerializeToString, response_deserializer=osmosis_dot_txfees_dot_v1beta1_dot_query__pb2.QueryDenomSpotPriceResponse.FromString)
        self.DenomPoolId = channel.unary_unary('/osmosis.txfees.v1beta1.Query/DenomPoolId', request_serializer=osmosis_dot_txfees_dot_v1beta1_dot_query__pb2.QueryDenomPoolIdRequest.SerializeToString, response_deserializer=osmosis_dot_txfees_dot_v1beta1_dot_query__pb2.QueryDenomPoolIdResponse.FromString)
        self.BaseDenom = channel.unary_unary('/osmosis.txfees.v1beta1.Query/BaseDenom', request_serializer=osmosis_dot_txfees_dot_v1beta1_dot_query__pb2.QueryBaseDenomRequest.SerializeToString, response_deserializer=osmosis_dot_txfees_dot_v1beta1_dot_query__pb2.QueryBaseDenomResponse.FromString)

class QueryServicer(object):
    'Missing associated documentation comment in .proto file.'

    def FeeTokens(self, request, context):
        'FeeTokens returns a list of all the whitelisted fee tokens and their\n        corresponding pools It does not include the BaseDenom, which has its own\n        query endpoint\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DenomSpotPrice(self, request, context):
        'Missing associated documentation comment in .proto file.'
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DenomPoolId(self, request, context):
        'Missing associated documentation comment in .proto file.'
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BaseDenom(self, request, context):
        'Missing associated documentation comment in .proto file.'
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'FeeTokens': grpc.unary_unary_rpc_method_handler(servicer.FeeTokens, request_deserializer=osmosis_dot_txfees_dot_v1beta1_dot_query__pb2.QueryFeeTokensRequest.FromString, response_serializer=osmosis_dot_txfees_dot_v1beta1_dot_query__pb2.QueryFeeTokensResponse.SerializeToString), 'DenomSpotPrice': grpc.unary_unary_rpc_method_handler(servicer.DenomSpotPrice, request_deserializer=osmosis_dot_txfees_dot_v1beta1_dot_query__pb2.QueryDenomSpotPriceRequest.FromString, response_serializer=osmosis_dot_txfees_dot_v1beta1_dot_query__pb2.QueryDenomSpotPriceResponse.SerializeToString), 'DenomPoolId': grpc.unary_unary_rpc_method_handler(servicer.DenomPoolId, request_deserializer=osmosis_dot_txfees_dot_v1beta1_dot_query__pb2.QueryDenomPoolIdRequest.FromString, response_serializer=osmosis_dot_txfees_dot_v1beta1_dot_query__pb2.QueryDenomPoolIdResponse.SerializeToString), 'BaseDenom': grpc.unary_unary_rpc_method_handler(servicer.BaseDenom, request_deserializer=osmosis_dot_txfees_dot_v1beta1_dot_query__pb2.QueryBaseDenomRequest.FromString, response_serializer=osmosis_dot_txfees_dot_v1beta1_dot_query__pb2.QueryBaseDenomResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('osmosis.txfees.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    'Missing associated documentation comment in .proto file.'

    @staticmethod
    def FeeTokens(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.txfees.v1beta1.Query/FeeTokens', osmosis_dot_txfees_dot_v1beta1_dot_query__pb2.QueryFeeTokensRequest.SerializeToString, osmosis_dot_txfees_dot_v1beta1_dot_query__pb2.QueryFeeTokensResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DenomSpotPrice(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.txfees.v1beta1.Query/DenomSpotPrice', osmosis_dot_txfees_dot_v1beta1_dot_query__pb2.QueryDenomSpotPriceRequest.SerializeToString, osmosis_dot_txfees_dot_v1beta1_dot_query__pb2.QueryDenomSpotPriceResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DenomPoolId(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.txfees.v1beta1.Query/DenomPoolId', osmosis_dot_txfees_dot_v1beta1_dot_query__pb2.QueryDenomPoolIdRequest.SerializeToString, osmosis_dot_txfees_dot_v1beta1_dot_query__pb2.QueryDenomPoolIdResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BaseDenom(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.txfees.v1beta1.Query/BaseDenom', osmosis_dot_txfees_dot_v1beta1_dot_query__pb2.QueryBaseDenomRequest.SerializeToString, osmosis_dot_txfees_dot_v1beta1_dot_query__pb2.QueryBaseDenomResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
