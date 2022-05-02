
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ....osmosis.pool_incentives.v1beta1 import query_pb2 as osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2

class QueryStub(object):
    'Missing associated documentation comment in .proto file.'

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.GaugeIds = channel.unary_unary('/osmosis.poolincentives.v1beta1.Query/GaugeIds', request_serializer=osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryGaugeIdsRequest.SerializeToString, response_deserializer=osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryGaugeIdsResponse.FromString)
        self.DistrInfo = channel.unary_unary('/osmosis.poolincentives.v1beta1.Query/DistrInfo', request_serializer=osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryDistrInfoRequest.SerializeToString, response_deserializer=osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryDistrInfoResponse.FromString)
        self.Params = channel.unary_unary('/osmosis.poolincentives.v1beta1.Query/Params', request_serializer=osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, response_deserializer=osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString)
        self.LockableDurations = channel.unary_unary('/osmosis.poolincentives.v1beta1.Query/LockableDurations', request_serializer=osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryLockableDurationsRequest.SerializeToString, response_deserializer=osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryLockableDurationsResponse.FromString)
        self.IncentivizedPools = channel.unary_unary('/osmosis.poolincentives.v1beta1.Query/IncentivizedPools', request_serializer=osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryIncentivizedPoolsRequest.SerializeToString, response_deserializer=osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryIncentivizedPoolsResponse.FromString)
        self.ExternalIncentiveGauges = channel.unary_unary('/osmosis.poolincentives.v1beta1.Query/ExternalIncentiveGauges', request_serializer=osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryExternalIncentiveGaugesRequest.SerializeToString, response_deserializer=osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryExternalIncentiveGaugesResponse.FromString)

class QueryServicer(object):
    'Missing associated documentation comment in .proto file.'

    def GaugeIds(self, request, context):
        'GaugeIds takes the pool id and returns the matching gauge ids and durations\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DistrInfo(self, request, context):
        'Missing associated documentation comment in .proto file.'
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Params(self, request, context):
        'Missing associated documentation comment in .proto file.'
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LockableDurations(self, request, context):
        'Missing associated documentation comment in .proto file.'
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IncentivizedPools(self, request, context):
        'Missing associated documentation comment in .proto file.'
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExternalIncentiveGauges(self, request, context):
        'Missing associated documentation comment in .proto file.'
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'GaugeIds': grpc.unary_unary_rpc_method_handler(servicer.GaugeIds, request_deserializer=osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryGaugeIdsRequest.FromString, response_serializer=osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryGaugeIdsResponse.SerializeToString), 'DistrInfo': grpc.unary_unary_rpc_method_handler(servicer.DistrInfo, request_deserializer=osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryDistrInfoRequest.FromString, response_serializer=osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryDistrInfoResponse.SerializeToString), 'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryParamsRequest.FromString, response_serializer=osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryParamsResponse.SerializeToString), 'LockableDurations': grpc.unary_unary_rpc_method_handler(servicer.LockableDurations, request_deserializer=osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryLockableDurationsRequest.FromString, response_serializer=osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryLockableDurationsResponse.SerializeToString), 'IncentivizedPools': grpc.unary_unary_rpc_method_handler(servicer.IncentivizedPools, request_deserializer=osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryIncentivizedPoolsRequest.FromString, response_serializer=osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryIncentivizedPoolsResponse.SerializeToString), 'ExternalIncentiveGauges': grpc.unary_unary_rpc_method_handler(servicer.ExternalIncentiveGauges, request_deserializer=osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryExternalIncentiveGaugesRequest.FromString, response_serializer=osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryExternalIncentiveGaugesResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('osmosis.poolincentives.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    'Missing associated documentation comment in .proto file.'

    @staticmethod
    def GaugeIds(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.poolincentives.v1beta1.Query/GaugeIds', osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryGaugeIdsRequest.SerializeToString, osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryGaugeIdsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DistrInfo(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.poolincentives.v1beta1.Query/DistrInfo', osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryDistrInfoRequest.SerializeToString, osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryDistrInfoResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.poolincentives.v1beta1.Query/Params', osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LockableDurations(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.poolincentives.v1beta1.Query/LockableDurations', osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryLockableDurationsRequest.SerializeToString, osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryLockableDurationsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IncentivizedPools(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.poolincentives.v1beta1.Query/IncentivizedPools', osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryIncentivizedPoolsRequest.SerializeToString, osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryIncentivizedPoolsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExternalIncentiveGauges(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.poolincentives.v1beta1.Query/ExternalIncentiveGauges', osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryExternalIncentiveGaugesRequest.SerializeToString, osmosis_dot_pool__incentives_dot_v1beta1_dot_query__pb2.QueryExternalIncentiveGaugesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
