
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ....akash.audit.v1beta2 import query_pb2 as akash_dot_audit_dot_v1beta2_dot_query__pb2

class QueryStub(object):
    'Query defines the gRPC querier service\n    '

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.AllProvidersAttributes = channel.unary_unary('/akash.audit.v1beta2.Query/AllProvidersAttributes', request_serializer=akash_dot_audit_dot_v1beta2_dot_query__pb2.QueryAllProvidersAttributesRequest.SerializeToString, response_deserializer=akash_dot_audit_dot_v1beta2_dot_query__pb2.QueryProvidersResponse.FromString)
        self.ProviderAttributes = channel.unary_unary('/akash.audit.v1beta2.Query/ProviderAttributes', request_serializer=akash_dot_audit_dot_v1beta2_dot_query__pb2.QueryProviderAttributesRequest.SerializeToString, response_deserializer=akash_dot_audit_dot_v1beta2_dot_query__pb2.QueryProvidersResponse.FromString)
        self.ProviderAuditorAttributes = channel.unary_unary('/akash.audit.v1beta2.Query/ProviderAuditorAttributes', request_serializer=akash_dot_audit_dot_v1beta2_dot_query__pb2.QueryProviderAuditorRequest.SerializeToString, response_deserializer=akash_dot_audit_dot_v1beta2_dot_query__pb2.QueryProvidersResponse.FromString)
        self.AuditorAttributes = channel.unary_unary('/akash.audit.v1beta2.Query/AuditorAttributes', request_serializer=akash_dot_audit_dot_v1beta2_dot_query__pb2.QueryAuditorAttributesRequest.SerializeToString, response_deserializer=akash_dot_audit_dot_v1beta2_dot_query__pb2.QueryProvidersResponse.FromString)

class QueryServicer(object):
    'Query defines the gRPC querier service\n    '

    def AllProvidersAttributes(self, request, context):
        'AllProvidersAttributes queries all providers\n        buf:lint:ignore RPC_REQUEST_RESPONSE_UNIQUE\n        buf:lint:ignore RPC_RESPONSE_STANDARD_NAME\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ProviderAttributes(self, request, context):
        'ProviderAttributes queries all provider signed attributes\n        buf:lint:ignore RPC_REQUEST_RESPONSE_UNIQUE\n        buf:lint:ignore RPC_RESPONSE_STANDARD_NAME\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ProviderAuditorAttributes(self, request, context):
        'ProviderAuditorAttributes queries provider signed attributes by specific auditor\n        buf:lint:ignore RPC_REQUEST_RESPONSE_UNIQUE\n        buf:lint:ignore RPC_RESPONSE_STANDARD_NAME\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AuditorAttributes(self, request, context):
        'AuditorAttributes queries all providers signed by this auditor\n        buf:lint:ignore RPC_REQUEST_RESPONSE_UNIQUE\n        buf:lint:ignore RPC_RESPONSE_STANDARD_NAME\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'AllProvidersAttributes': grpc.unary_unary_rpc_method_handler(servicer.AllProvidersAttributes, request_deserializer=akash_dot_audit_dot_v1beta2_dot_query__pb2.QueryAllProvidersAttributesRequest.FromString, response_serializer=akash_dot_audit_dot_v1beta2_dot_query__pb2.QueryProvidersResponse.SerializeToString), 'ProviderAttributes': grpc.unary_unary_rpc_method_handler(servicer.ProviderAttributes, request_deserializer=akash_dot_audit_dot_v1beta2_dot_query__pb2.QueryProviderAttributesRequest.FromString, response_serializer=akash_dot_audit_dot_v1beta2_dot_query__pb2.QueryProvidersResponse.SerializeToString), 'ProviderAuditorAttributes': grpc.unary_unary_rpc_method_handler(servicer.ProviderAuditorAttributes, request_deserializer=akash_dot_audit_dot_v1beta2_dot_query__pb2.QueryProviderAuditorRequest.FromString, response_serializer=akash_dot_audit_dot_v1beta2_dot_query__pb2.QueryProvidersResponse.SerializeToString), 'AuditorAttributes': grpc.unary_unary_rpc_method_handler(servicer.AuditorAttributes, request_deserializer=akash_dot_audit_dot_v1beta2_dot_query__pb2.QueryAuditorAttributesRequest.FromString, response_serializer=akash_dot_audit_dot_v1beta2_dot_query__pb2.QueryProvidersResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('akash.audit.v1beta2.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    'Query defines the gRPC querier service\n    '

    @staticmethod
    def AllProvidersAttributes(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.audit.v1beta2.Query/AllProvidersAttributes', akash_dot_audit_dot_v1beta2_dot_query__pb2.QueryAllProvidersAttributesRequest.SerializeToString, akash_dot_audit_dot_v1beta2_dot_query__pb2.QueryProvidersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ProviderAttributes(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.audit.v1beta2.Query/ProviderAttributes', akash_dot_audit_dot_v1beta2_dot_query__pb2.QueryProviderAttributesRequest.SerializeToString, akash_dot_audit_dot_v1beta2_dot_query__pb2.QueryProvidersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ProviderAuditorAttributes(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.audit.v1beta2.Query/ProviderAuditorAttributes', akash_dot_audit_dot_v1beta2_dot_query__pb2.QueryProviderAuditorRequest.SerializeToString, akash_dot_audit_dot_v1beta2_dot_query__pb2.QueryProvidersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AuditorAttributes(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.audit.v1beta2.Query/AuditorAttributes', akash_dot_audit_dot_v1beta2_dot_query__pb2.QueryAuditorAttributesRequest.SerializeToString, akash_dot_audit_dot_v1beta2_dot_query__pb2.QueryProvidersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
