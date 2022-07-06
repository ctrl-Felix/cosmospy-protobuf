
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ....akash.provider.v1beta2 import query_pb2 as akash_dot_provider_dot_v1beta2_dot_query__pb2

class QueryStub(object):
    'Query defines the gRPC querier service\n    '

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.Providers = channel.unary_unary('/akash.provider.v1beta2.Query/Providers', request_serializer=akash_dot_provider_dot_v1beta2_dot_query__pb2.QueryProvidersRequest.SerializeToString, response_deserializer=akash_dot_provider_dot_v1beta2_dot_query__pb2.QueryProvidersResponse.FromString)
        self.Provider = channel.unary_unary('/akash.provider.v1beta2.Query/Provider', request_serializer=akash_dot_provider_dot_v1beta2_dot_query__pb2.QueryProviderRequest.SerializeToString, response_deserializer=akash_dot_provider_dot_v1beta2_dot_query__pb2.QueryProviderResponse.FromString)

class QueryServicer(object):
    'Query defines the gRPC querier service\n    '

    def Providers(self, request, context):
        'Providers queries providers\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Provider(self, request, context):
        'Provider queries provider details\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Providers': grpc.unary_unary_rpc_method_handler(servicer.Providers, request_deserializer=akash_dot_provider_dot_v1beta2_dot_query__pb2.QueryProvidersRequest.FromString, response_serializer=akash_dot_provider_dot_v1beta2_dot_query__pb2.QueryProvidersResponse.SerializeToString), 'Provider': grpc.unary_unary_rpc_method_handler(servicer.Provider, request_deserializer=akash_dot_provider_dot_v1beta2_dot_query__pb2.QueryProviderRequest.FromString, response_serializer=akash_dot_provider_dot_v1beta2_dot_query__pb2.QueryProviderResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('akash.provider.v1beta2.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    'Query defines the gRPC querier service\n    '

    @staticmethod
    def Providers(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.provider.v1beta2.Query/Providers', akash_dot_provider_dot_v1beta2_dot_query__pb2.QueryProvidersRequest.SerializeToString, akash_dot_provider_dot_v1beta2_dot_query__pb2.QueryProvidersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Provider(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.provider.v1beta2.Query/Provider', akash_dot_provider_dot_v1beta2_dot_query__pb2.QueryProviderRequest.SerializeToString, akash_dot_provider_dot_v1beta2_dot_query__pb2.QueryProviderResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
