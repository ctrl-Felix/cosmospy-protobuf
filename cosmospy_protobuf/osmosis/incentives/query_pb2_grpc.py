
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ...osmosis.incentives import query_pb2 as osmosis_dot_incentives_dot_query__pb2

class QueryStub(object):
    'Query defines the gRPC querier service.\n    '

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.ModuleToDistributeCoins = channel.unary_unary('/osmosis.incentives.Query/ModuleToDistributeCoins', request_serializer=osmosis_dot_incentives_dot_query__pb2.ModuleToDistributeCoinsRequest.SerializeToString, response_deserializer=osmosis_dot_incentives_dot_query__pb2.ModuleToDistributeCoinsResponse.FromString)
        self.ModuleDistributedCoins = channel.unary_unary('/osmosis.incentives.Query/ModuleDistributedCoins', request_serializer=osmosis_dot_incentives_dot_query__pb2.ModuleDistributedCoinsRequest.SerializeToString, response_deserializer=osmosis_dot_incentives_dot_query__pb2.ModuleDistributedCoinsResponse.FromString)
        self.GaugeByID = channel.unary_unary('/osmosis.incentives.Query/GaugeByID', request_serializer=osmosis_dot_incentives_dot_query__pb2.GaugeByIDRequest.SerializeToString, response_deserializer=osmosis_dot_incentives_dot_query__pb2.GaugeByIDResponse.FromString)
        self.Gauges = channel.unary_unary('/osmosis.incentives.Query/Gauges', request_serializer=osmosis_dot_incentives_dot_query__pb2.GaugesRequest.SerializeToString, response_deserializer=osmosis_dot_incentives_dot_query__pb2.GaugesResponse.FromString)
        self.ActiveGauges = channel.unary_unary('/osmosis.incentives.Query/ActiveGauges', request_serializer=osmosis_dot_incentives_dot_query__pb2.ActiveGaugesRequest.SerializeToString, response_deserializer=osmosis_dot_incentives_dot_query__pb2.ActiveGaugesResponse.FromString)
        self.ActiveGaugesPerDenom = channel.unary_unary('/osmosis.incentives.Query/ActiveGaugesPerDenom', request_serializer=osmosis_dot_incentives_dot_query__pb2.ActiveGaugesPerDenomRequest.SerializeToString, response_deserializer=osmosis_dot_incentives_dot_query__pb2.ActiveGaugesPerDenomResponse.FromString)
        self.UpcomingGauges = channel.unary_unary('/osmosis.incentives.Query/UpcomingGauges', request_serializer=osmosis_dot_incentives_dot_query__pb2.UpcomingGaugesRequest.SerializeToString, response_deserializer=osmosis_dot_incentives_dot_query__pb2.UpcomingGaugesResponse.FromString)
        self.UpcomingGaugesPerDenom = channel.unary_unary('/osmosis.incentives.Query/UpcomingGaugesPerDenom', request_serializer=osmosis_dot_incentives_dot_query__pb2.UpcomingGaugesPerDenomRequest.SerializeToString, response_deserializer=osmosis_dot_incentives_dot_query__pb2.UpcomingGaugesPerDenomResponse.FromString)
        self.RewardsEst = channel.unary_unary('/osmosis.incentives.Query/RewardsEst', request_serializer=osmosis_dot_incentives_dot_query__pb2.RewardsEstRequest.SerializeToString, response_deserializer=osmosis_dot_incentives_dot_query__pb2.RewardsEstResponse.FromString)
        self.LockableDurations = channel.unary_unary('/osmosis.incentives.Query/LockableDurations', request_serializer=osmosis_dot_incentives_dot_query__pb2.QueryLockableDurationsRequest.SerializeToString, response_deserializer=osmosis_dot_incentives_dot_query__pb2.QueryLockableDurationsResponse.FromString)

class QueryServicer(object):
    'Query defines the gRPC querier service.\n    '

    def ModuleToDistributeCoins(self, request, context):
        'returns coins that is going to be distributed\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ModuleDistributedCoins(self, request, context):
        'returns coins that are distributed by module so far\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GaugeByID(self, request, context):
        'returns Gauge by id\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Gauges(self, request, context):
        'returns gauges both upcoming and active\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ActiveGauges(self, request, context):
        'returns active gauges\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ActiveGaugesPerDenom(self, request, context):
        'returns active gauges per denom\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpcomingGauges(self, request, context):
        'returns scheduled gauges\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpcomingGaugesPerDenom(self, request, context):
        'returns scheduled gauges per denom\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RewardsEst(self, request, context):
        'RewardsEst returns an estimate of the rewards at a future specific time.\n        The querier either provides an address or a set of locks\n        for which they want to find the associated rewards.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LockableDurations(self, request, context):
        'returns lockable durations that are valid to give incentives\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'ModuleToDistributeCoins': grpc.unary_unary_rpc_method_handler(servicer.ModuleToDistributeCoins, request_deserializer=osmosis_dot_incentives_dot_query__pb2.ModuleToDistributeCoinsRequest.FromString, response_serializer=osmosis_dot_incentives_dot_query__pb2.ModuleToDistributeCoinsResponse.SerializeToString), 'ModuleDistributedCoins': grpc.unary_unary_rpc_method_handler(servicer.ModuleDistributedCoins, request_deserializer=osmosis_dot_incentives_dot_query__pb2.ModuleDistributedCoinsRequest.FromString, response_serializer=osmosis_dot_incentives_dot_query__pb2.ModuleDistributedCoinsResponse.SerializeToString), 'GaugeByID': grpc.unary_unary_rpc_method_handler(servicer.GaugeByID, request_deserializer=osmosis_dot_incentives_dot_query__pb2.GaugeByIDRequest.FromString, response_serializer=osmosis_dot_incentives_dot_query__pb2.GaugeByIDResponse.SerializeToString), 'Gauges': grpc.unary_unary_rpc_method_handler(servicer.Gauges, request_deserializer=osmosis_dot_incentives_dot_query__pb2.GaugesRequest.FromString, response_serializer=osmosis_dot_incentives_dot_query__pb2.GaugesResponse.SerializeToString), 'ActiveGauges': grpc.unary_unary_rpc_method_handler(servicer.ActiveGauges, request_deserializer=osmosis_dot_incentives_dot_query__pb2.ActiveGaugesRequest.FromString, response_serializer=osmosis_dot_incentives_dot_query__pb2.ActiveGaugesResponse.SerializeToString), 'ActiveGaugesPerDenom': grpc.unary_unary_rpc_method_handler(servicer.ActiveGaugesPerDenom, request_deserializer=osmosis_dot_incentives_dot_query__pb2.ActiveGaugesPerDenomRequest.FromString, response_serializer=osmosis_dot_incentives_dot_query__pb2.ActiveGaugesPerDenomResponse.SerializeToString), 'UpcomingGauges': grpc.unary_unary_rpc_method_handler(servicer.UpcomingGauges, request_deserializer=osmosis_dot_incentives_dot_query__pb2.UpcomingGaugesRequest.FromString, response_serializer=osmosis_dot_incentives_dot_query__pb2.UpcomingGaugesResponse.SerializeToString), 'UpcomingGaugesPerDenom': grpc.unary_unary_rpc_method_handler(servicer.UpcomingGaugesPerDenom, request_deserializer=osmosis_dot_incentives_dot_query__pb2.UpcomingGaugesPerDenomRequest.FromString, response_serializer=osmosis_dot_incentives_dot_query__pb2.UpcomingGaugesPerDenomResponse.SerializeToString), 'RewardsEst': grpc.unary_unary_rpc_method_handler(servicer.RewardsEst, request_deserializer=osmosis_dot_incentives_dot_query__pb2.RewardsEstRequest.FromString, response_serializer=osmosis_dot_incentives_dot_query__pb2.RewardsEstResponse.SerializeToString), 'LockableDurations': grpc.unary_unary_rpc_method_handler(servicer.LockableDurations, request_deserializer=osmosis_dot_incentives_dot_query__pb2.QueryLockableDurationsRequest.FromString, response_serializer=osmosis_dot_incentives_dot_query__pb2.QueryLockableDurationsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('osmosis.incentives.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    'Query defines the gRPC querier service.\n    '

    @staticmethod
    def ModuleToDistributeCoins(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.incentives.Query/ModuleToDistributeCoins', osmosis_dot_incentives_dot_query__pb2.ModuleToDistributeCoinsRequest.SerializeToString, osmosis_dot_incentives_dot_query__pb2.ModuleToDistributeCoinsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ModuleDistributedCoins(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.incentives.Query/ModuleDistributedCoins', osmosis_dot_incentives_dot_query__pb2.ModuleDistributedCoinsRequest.SerializeToString, osmosis_dot_incentives_dot_query__pb2.ModuleDistributedCoinsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GaugeByID(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.incentives.Query/GaugeByID', osmosis_dot_incentives_dot_query__pb2.GaugeByIDRequest.SerializeToString, osmosis_dot_incentives_dot_query__pb2.GaugeByIDResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Gauges(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.incentives.Query/Gauges', osmosis_dot_incentives_dot_query__pb2.GaugesRequest.SerializeToString, osmosis_dot_incentives_dot_query__pb2.GaugesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ActiveGauges(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.incentives.Query/ActiveGauges', osmosis_dot_incentives_dot_query__pb2.ActiveGaugesRequest.SerializeToString, osmosis_dot_incentives_dot_query__pb2.ActiveGaugesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ActiveGaugesPerDenom(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.incentives.Query/ActiveGaugesPerDenom', osmosis_dot_incentives_dot_query__pb2.ActiveGaugesPerDenomRequest.SerializeToString, osmosis_dot_incentives_dot_query__pb2.ActiveGaugesPerDenomResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpcomingGauges(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.incentives.Query/UpcomingGauges', osmosis_dot_incentives_dot_query__pb2.UpcomingGaugesRequest.SerializeToString, osmosis_dot_incentives_dot_query__pb2.UpcomingGaugesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpcomingGaugesPerDenom(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.incentives.Query/UpcomingGaugesPerDenom', osmosis_dot_incentives_dot_query__pb2.UpcomingGaugesPerDenomRequest.SerializeToString, osmosis_dot_incentives_dot_query__pb2.UpcomingGaugesPerDenomResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RewardsEst(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.incentives.Query/RewardsEst', osmosis_dot_incentives_dot_query__pb2.RewardsEstRequest.SerializeToString, osmosis_dot_incentives_dot_query__pb2.RewardsEstResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LockableDurations(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.incentives.Query/LockableDurations', osmosis_dot_incentives_dot_query__pb2.QueryLockableDurationsRequest.SerializeToString, osmosis_dot_incentives_dot_query__pb2.QueryLockableDurationsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
