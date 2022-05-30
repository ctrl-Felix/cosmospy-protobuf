
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ....umee.oracle.v1beta1 import query_pb2 as umee_dot_oracle_dot_v1beta1_dot_query__pb2

class QueryStub(object):
    'Query defines the gRPC querier service.\n    '

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.ExchangeRates = channel.unary_unary('/umeenetwork.umee.oracle.v1beta1.Query/ExchangeRates', request_serializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryExchangeRatesRequest.SerializeToString, response_deserializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryExchangeRatesResponse.FromString)
        self.ActiveExchangeRates = channel.unary_unary('/umeenetwork.umee.oracle.v1beta1.Query/ActiveExchangeRates', request_serializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryActiveExchangeRatesRequest.SerializeToString, response_deserializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryActiveExchangeRatesResponse.FromString)
        self.FeederDelegation = channel.unary_unary('/umeenetwork.umee.oracle.v1beta1.Query/FeederDelegation', request_serializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryFeederDelegationRequest.SerializeToString, response_deserializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryFeederDelegationResponse.FromString)
        self.MissCounter = channel.unary_unary('/umeenetwork.umee.oracle.v1beta1.Query/MissCounter', request_serializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryMissCounterRequest.SerializeToString, response_deserializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryMissCounterResponse.FromString)
        self.AggregatePrevote = channel.unary_unary('/umeenetwork.umee.oracle.v1beta1.Query/AggregatePrevote', request_serializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryAggregatePrevoteRequest.SerializeToString, response_deserializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryAggregatePrevoteResponse.FromString)
        self.AggregatePrevotes = channel.unary_unary('/umeenetwork.umee.oracle.v1beta1.Query/AggregatePrevotes', request_serializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryAggregatePrevotesRequest.SerializeToString, response_deserializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryAggregatePrevotesResponse.FromString)
        self.AggregateVote = channel.unary_unary('/umeenetwork.umee.oracle.v1beta1.Query/AggregateVote', request_serializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryAggregateVoteRequest.SerializeToString, response_deserializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryAggregateVoteResponse.FromString)
        self.AggregateVotes = channel.unary_unary('/umeenetwork.umee.oracle.v1beta1.Query/AggregateVotes', request_serializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryAggregateVotesRequest.SerializeToString, response_deserializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryAggregateVotesResponse.FromString)
        self.Params = channel.unary_unary('/umeenetwork.umee.oracle.v1beta1.Query/Params', request_serializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, response_deserializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString)

class QueryServicer(object):
    'Query defines the gRPC querier service.\n    '

    def ExchangeRates(self, request, context):
        'ExchangeRates returns exchange rates of all denoms,\n        or, if specified, returns a single denom\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ActiveExchangeRates(self, request, context):
        'ActiveExchangeRates returns all active denoms\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FeederDelegation(self, request, context):
        'FeederDelegation returns feeder delegation of a validator\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MissCounter(self, request, context):
        'MissCounter returns oracle miss counter of a validator\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AggregatePrevote(self, request, context):
        'AggregatePrevote returns an aggregate prevote of a validator\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AggregatePrevotes(self, request, context):
        'AggregatePrevotes returns aggregate prevotes of all validators\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AggregateVote(self, request, context):
        'AggregateVote returns an aggregate vote of a validator\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AggregateVotes(self, request, context):
        'AggregateVotes returns aggregate votes of all validators\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Params(self, request, context):
        'Params queries all parameters.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'ExchangeRates': grpc.unary_unary_rpc_method_handler(servicer.ExchangeRates, request_deserializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryExchangeRatesRequest.FromString, response_serializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryExchangeRatesResponse.SerializeToString), 'ActiveExchangeRates': grpc.unary_unary_rpc_method_handler(servicer.ActiveExchangeRates, request_deserializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryActiveExchangeRatesRequest.FromString, response_serializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryActiveExchangeRatesResponse.SerializeToString), 'FeederDelegation': grpc.unary_unary_rpc_method_handler(servicer.FeederDelegation, request_deserializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryFeederDelegationRequest.FromString, response_serializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryFeederDelegationResponse.SerializeToString), 'MissCounter': grpc.unary_unary_rpc_method_handler(servicer.MissCounter, request_deserializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryMissCounterRequest.FromString, response_serializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryMissCounterResponse.SerializeToString), 'AggregatePrevote': grpc.unary_unary_rpc_method_handler(servicer.AggregatePrevote, request_deserializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryAggregatePrevoteRequest.FromString, response_serializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryAggregatePrevoteResponse.SerializeToString), 'AggregatePrevotes': grpc.unary_unary_rpc_method_handler(servicer.AggregatePrevotes, request_deserializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryAggregatePrevotesRequest.FromString, response_serializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryAggregatePrevotesResponse.SerializeToString), 'AggregateVote': grpc.unary_unary_rpc_method_handler(servicer.AggregateVote, request_deserializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryAggregateVoteRequest.FromString, response_serializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryAggregateVoteResponse.SerializeToString), 'AggregateVotes': grpc.unary_unary_rpc_method_handler(servicer.AggregateVotes, request_deserializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryAggregateVotesRequest.FromString, response_serializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryAggregateVotesResponse.SerializeToString), 'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryParamsRequest.FromString, response_serializer=umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryParamsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('umeenetwork.umee.oracle.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    'Query defines the gRPC querier service.\n    '

    @staticmethod
    def ExchangeRates(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/umeenetwork.umee.oracle.v1beta1.Query/ExchangeRates', umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryExchangeRatesRequest.SerializeToString, umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryExchangeRatesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ActiveExchangeRates(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/umeenetwork.umee.oracle.v1beta1.Query/ActiveExchangeRates', umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryActiveExchangeRatesRequest.SerializeToString, umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryActiveExchangeRatesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FeederDelegation(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/umeenetwork.umee.oracle.v1beta1.Query/FeederDelegation', umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryFeederDelegationRequest.SerializeToString, umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryFeederDelegationResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MissCounter(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/umeenetwork.umee.oracle.v1beta1.Query/MissCounter', umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryMissCounterRequest.SerializeToString, umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryMissCounterResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AggregatePrevote(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/umeenetwork.umee.oracle.v1beta1.Query/AggregatePrevote', umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryAggregatePrevoteRequest.SerializeToString, umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryAggregatePrevoteResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AggregatePrevotes(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/umeenetwork.umee.oracle.v1beta1.Query/AggregatePrevotes', umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryAggregatePrevotesRequest.SerializeToString, umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryAggregatePrevotesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AggregateVote(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/umeenetwork.umee.oracle.v1beta1.Query/AggregateVote', umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryAggregateVoteRequest.SerializeToString, umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryAggregateVoteResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AggregateVotes(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/umeenetwork.umee.oracle.v1beta1.Query/AggregateVotes', umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryAggregateVotesRequest.SerializeToString, umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryAggregateVotesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/umeenetwork.umee.oracle.v1beta1.Query/Params', umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, umee_dot_oracle_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
