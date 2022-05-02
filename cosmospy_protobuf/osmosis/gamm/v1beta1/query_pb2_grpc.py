
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ....osmosis.gamm.v1beta1 import query_pb2 as osmosis_dot_gamm_dot_v1beta1_dot_query__pb2

class QueryStub(object):
    'Missing associated documentation comment in .proto file.'

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.Pools = channel.unary_unary('/osmosis.gamm.v1beta1.Query/Pools', request_serializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryPoolsRequest.SerializeToString, response_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryPoolsResponse.FromString)
        self.NumPools = channel.unary_unary('/osmosis.gamm.v1beta1.Query/NumPools', request_serializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryNumPoolsRequest.SerializeToString, response_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryNumPoolsResponse.FromString)
        self.TotalLiquidity = channel.unary_unary('/osmosis.gamm.v1beta1.Query/TotalLiquidity', request_serializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryTotalLiquidityRequest.SerializeToString, response_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryTotalLiquidityResponse.FromString)
        self.Pool = channel.unary_unary('/osmosis.gamm.v1beta1.Query/Pool', request_serializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryPoolRequest.SerializeToString, response_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryPoolResponse.FromString)
        self.PoolParams = channel.unary_unary('/osmosis.gamm.v1beta1.Query/PoolParams', request_serializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryPoolParamsRequest.SerializeToString, response_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryPoolParamsResponse.FromString)
        self.TotalPoolLiquidity = channel.unary_unary('/osmosis.gamm.v1beta1.Query/TotalPoolLiquidity', request_serializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryTotalPoolLiquidityRequest.SerializeToString, response_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryTotalPoolLiquidityResponse.FromString)
        self.TotalShares = channel.unary_unary('/osmosis.gamm.v1beta1.Query/TotalShares', request_serializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryTotalSharesRequest.SerializeToString, response_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryTotalSharesResponse.FromString)
        self.SpotPrice = channel.unary_unary('/osmosis.gamm.v1beta1.Query/SpotPrice', request_serializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QuerySpotPriceRequest.SerializeToString, response_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QuerySpotPriceResponse.FromString)
        self.EstimateSwapExactAmountIn = channel.unary_unary('/osmosis.gamm.v1beta1.Query/EstimateSwapExactAmountIn', request_serializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QuerySwapExactAmountInRequest.SerializeToString, response_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QuerySwapExactAmountInResponse.FromString)
        self.EstimateSwapExactAmountOut = channel.unary_unary('/osmosis.gamm.v1beta1.Query/EstimateSwapExactAmountOut', request_serializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QuerySwapExactAmountOutRequest.SerializeToString, response_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QuerySwapExactAmountOutResponse.FromString)

class QueryServicer(object):
    'Missing associated documentation comment in .proto file.'

    def Pools(self, request, context):
        'Missing associated documentation comment in .proto file.'
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NumPools(self, request, context):
        'Missing associated documentation comment in .proto file.'
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TotalLiquidity(self, request, context):
        'Missing associated documentation comment in .proto file.'
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Pool(self, request, context):
        'Per Pool gRPC Endpoints\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PoolParams(self, request, context):
        'Missing associated documentation comment in .proto file.'
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TotalPoolLiquidity(self, request, context):
        'Missing associated documentation comment in .proto file.'
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TotalShares(self, request, context):
        'Missing associated documentation comment in .proto file.'
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SpotPrice(self, request, context):
        'SpotPrice defines a gRPC query handler that returns the spot price given\n        a base denomination and a quote denomination.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EstimateSwapExactAmountIn(self, request, context):
        'Estimate the swap.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EstimateSwapExactAmountOut(self, request, context):
        'Missing associated documentation comment in .proto file.'
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Pools': grpc.unary_unary_rpc_method_handler(servicer.Pools, request_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryPoolsRequest.FromString, response_serializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryPoolsResponse.SerializeToString), 'NumPools': grpc.unary_unary_rpc_method_handler(servicer.NumPools, request_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryNumPoolsRequest.FromString, response_serializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryNumPoolsResponse.SerializeToString), 'TotalLiquidity': grpc.unary_unary_rpc_method_handler(servicer.TotalLiquidity, request_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryTotalLiquidityRequest.FromString, response_serializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryTotalLiquidityResponse.SerializeToString), 'Pool': grpc.unary_unary_rpc_method_handler(servicer.Pool, request_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryPoolRequest.FromString, response_serializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryPoolResponse.SerializeToString), 'PoolParams': grpc.unary_unary_rpc_method_handler(servicer.PoolParams, request_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryPoolParamsRequest.FromString, response_serializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryPoolParamsResponse.SerializeToString), 'TotalPoolLiquidity': grpc.unary_unary_rpc_method_handler(servicer.TotalPoolLiquidity, request_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryTotalPoolLiquidityRequest.FromString, response_serializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryTotalPoolLiquidityResponse.SerializeToString), 'TotalShares': grpc.unary_unary_rpc_method_handler(servicer.TotalShares, request_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryTotalSharesRequest.FromString, response_serializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryTotalSharesResponse.SerializeToString), 'SpotPrice': grpc.unary_unary_rpc_method_handler(servicer.SpotPrice, request_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QuerySpotPriceRequest.FromString, response_serializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QuerySpotPriceResponse.SerializeToString), 'EstimateSwapExactAmountIn': grpc.unary_unary_rpc_method_handler(servicer.EstimateSwapExactAmountIn, request_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QuerySwapExactAmountInRequest.FromString, response_serializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QuerySwapExactAmountInResponse.SerializeToString), 'EstimateSwapExactAmountOut': grpc.unary_unary_rpc_method_handler(servicer.EstimateSwapExactAmountOut, request_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QuerySwapExactAmountOutRequest.FromString, response_serializer=osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QuerySwapExactAmountOutResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('osmosis.gamm.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    'Missing associated documentation comment in .proto file.'

    @staticmethod
    def Pools(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.gamm.v1beta1.Query/Pools', osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryPoolsRequest.SerializeToString, osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryPoolsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NumPools(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.gamm.v1beta1.Query/NumPools', osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryNumPoolsRequest.SerializeToString, osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryNumPoolsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TotalLiquidity(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.gamm.v1beta1.Query/TotalLiquidity', osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryTotalLiquidityRequest.SerializeToString, osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryTotalLiquidityResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Pool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.gamm.v1beta1.Query/Pool', osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryPoolRequest.SerializeToString, osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryPoolResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PoolParams(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.gamm.v1beta1.Query/PoolParams', osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryPoolParamsRequest.SerializeToString, osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryPoolParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TotalPoolLiquidity(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.gamm.v1beta1.Query/TotalPoolLiquidity', osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryTotalPoolLiquidityRequest.SerializeToString, osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryTotalPoolLiquidityResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TotalShares(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.gamm.v1beta1.Query/TotalShares', osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryTotalSharesRequest.SerializeToString, osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QueryTotalSharesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SpotPrice(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.gamm.v1beta1.Query/SpotPrice', osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QuerySpotPriceRequest.SerializeToString, osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QuerySpotPriceResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EstimateSwapExactAmountIn(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.gamm.v1beta1.Query/EstimateSwapExactAmountIn', osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QuerySwapExactAmountInRequest.SerializeToString, osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QuerySwapExactAmountInResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EstimateSwapExactAmountOut(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.gamm.v1beta1.Query/EstimateSwapExactAmountOut', osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QuerySwapExactAmountOutRequest.SerializeToString, osmosis_dot_gamm_dot_v1beta1_dot_query__pb2.QuerySwapExactAmountOutResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
