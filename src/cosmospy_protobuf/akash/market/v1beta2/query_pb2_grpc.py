
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ....akash.market.v1beta2 import query_pb2 as akash_dot_market_dot_v1beta2_dot_query__pb2

class QueryStub(object):
    'Query defines the gRPC querier service\n    '

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.Orders = channel.unary_unary('/akash.market.v1beta2.Query/Orders', request_serializer=akash_dot_market_dot_v1beta2_dot_query__pb2.QueryOrdersRequest.SerializeToString, response_deserializer=akash_dot_market_dot_v1beta2_dot_query__pb2.QueryOrdersResponse.FromString)
        self.Order = channel.unary_unary('/akash.market.v1beta2.Query/Order', request_serializer=akash_dot_market_dot_v1beta2_dot_query__pb2.QueryOrderRequest.SerializeToString, response_deserializer=akash_dot_market_dot_v1beta2_dot_query__pb2.QueryOrderResponse.FromString)
        self.Bids = channel.unary_unary('/akash.market.v1beta2.Query/Bids', request_serializer=akash_dot_market_dot_v1beta2_dot_query__pb2.QueryBidsRequest.SerializeToString, response_deserializer=akash_dot_market_dot_v1beta2_dot_query__pb2.QueryBidsResponse.FromString)
        self.Bid = channel.unary_unary('/akash.market.v1beta2.Query/Bid', request_serializer=akash_dot_market_dot_v1beta2_dot_query__pb2.QueryBidRequest.SerializeToString, response_deserializer=akash_dot_market_dot_v1beta2_dot_query__pb2.QueryBidResponse.FromString)
        self.Leases = channel.unary_unary('/akash.market.v1beta2.Query/Leases', request_serializer=akash_dot_market_dot_v1beta2_dot_query__pb2.QueryLeasesRequest.SerializeToString, response_deserializer=akash_dot_market_dot_v1beta2_dot_query__pb2.QueryLeasesResponse.FromString)
        self.Lease = channel.unary_unary('/akash.market.v1beta2.Query/Lease', request_serializer=akash_dot_market_dot_v1beta2_dot_query__pb2.QueryLeaseRequest.SerializeToString, response_deserializer=akash_dot_market_dot_v1beta2_dot_query__pb2.QueryLeaseResponse.FromString)

class QueryServicer(object):
    'Query defines the gRPC querier service\n    '

    def Orders(self, request, context):
        'Orders queries orders with filters\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Order(self, request, context):
        'Order queries order details\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Bids(self, request, context):
        'Bids queries bids with filters\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Bid(self, request, context):
        'Bid queries bid details\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Leases(self, request, context):
        'Leases queries leases with filters\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Lease(self, request, context):
        'Lease queries lease details\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Orders': grpc.unary_unary_rpc_method_handler(servicer.Orders, request_deserializer=akash_dot_market_dot_v1beta2_dot_query__pb2.QueryOrdersRequest.FromString, response_serializer=akash_dot_market_dot_v1beta2_dot_query__pb2.QueryOrdersResponse.SerializeToString), 'Order': grpc.unary_unary_rpc_method_handler(servicer.Order, request_deserializer=akash_dot_market_dot_v1beta2_dot_query__pb2.QueryOrderRequest.FromString, response_serializer=akash_dot_market_dot_v1beta2_dot_query__pb2.QueryOrderResponse.SerializeToString), 'Bids': grpc.unary_unary_rpc_method_handler(servicer.Bids, request_deserializer=akash_dot_market_dot_v1beta2_dot_query__pb2.QueryBidsRequest.FromString, response_serializer=akash_dot_market_dot_v1beta2_dot_query__pb2.QueryBidsResponse.SerializeToString), 'Bid': grpc.unary_unary_rpc_method_handler(servicer.Bid, request_deserializer=akash_dot_market_dot_v1beta2_dot_query__pb2.QueryBidRequest.FromString, response_serializer=akash_dot_market_dot_v1beta2_dot_query__pb2.QueryBidResponse.SerializeToString), 'Leases': grpc.unary_unary_rpc_method_handler(servicer.Leases, request_deserializer=akash_dot_market_dot_v1beta2_dot_query__pb2.QueryLeasesRequest.FromString, response_serializer=akash_dot_market_dot_v1beta2_dot_query__pb2.QueryLeasesResponse.SerializeToString), 'Lease': grpc.unary_unary_rpc_method_handler(servicer.Lease, request_deserializer=akash_dot_market_dot_v1beta2_dot_query__pb2.QueryLeaseRequest.FromString, response_serializer=akash_dot_market_dot_v1beta2_dot_query__pb2.QueryLeaseResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('akash.market.v1beta2.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    'Query defines the gRPC querier service\n    '

    @staticmethod
    def Orders(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.market.v1beta2.Query/Orders', akash_dot_market_dot_v1beta2_dot_query__pb2.QueryOrdersRequest.SerializeToString, akash_dot_market_dot_v1beta2_dot_query__pb2.QueryOrdersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Order(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.market.v1beta2.Query/Order', akash_dot_market_dot_v1beta2_dot_query__pb2.QueryOrderRequest.SerializeToString, akash_dot_market_dot_v1beta2_dot_query__pb2.QueryOrderResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Bids(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.market.v1beta2.Query/Bids', akash_dot_market_dot_v1beta2_dot_query__pb2.QueryBidsRequest.SerializeToString, akash_dot_market_dot_v1beta2_dot_query__pb2.QueryBidsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Bid(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.market.v1beta2.Query/Bid', akash_dot_market_dot_v1beta2_dot_query__pb2.QueryBidRequest.SerializeToString, akash_dot_market_dot_v1beta2_dot_query__pb2.QueryBidResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Leases(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.market.v1beta2.Query/Leases', akash_dot_market_dot_v1beta2_dot_query__pb2.QueryLeasesRequest.SerializeToString, akash_dot_market_dot_v1beta2_dot_query__pb2.QueryLeasesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Lease(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.market.v1beta2.Query/Lease', akash_dot_market_dot_v1beta2_dot_query__pb2.QueryLeaseRequest.SerializeToString, akash_dot_market_dot_v1beta2_dot_query__pb2.QueryLeaseResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
