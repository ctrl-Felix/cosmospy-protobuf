
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ....akash.escrow.v1beta2 import query_pb2 as akash_dot_escrow_dot_v1beta2_dot_query__pb2

class QueryStub(object):
    'Query defines the gRPC querier service\n    '

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.Accounts = channel.unary_unary('/akash.escrow.v1beta2.Query/Accounts', request_serializer=akash_dot_escrow_dot_v1beta2_dot_query__pb2.QueryAccountsRequest.SerializeToString, response_deserializer=akash_dot_escrow_dot_v1beta2_dot_query__pb2.QueryAccountsResponse.FromString)
        self.Payments = channel.unary_unary('/akash.escrow.v1beta2.Query/Payments', request_serializer=akash_dot_escrow_dot_v1beta2_dot_query__pb2.QueryPaymentsRequest.SerializeToString, response_deserializer=akash_dot_escrow_dot_v1beta2_dot_query__pb2.QueryPaymentsResponse.FromString)

class QueryServicer(object):
    'Query defines the gRPC querier service\n    '

    def Accounts(self, request, context):
        'buf:lint:ignore RPC_REQUEST_RESPONSE_UNIQUE\n        buf:lint:ignore RPC_RESPONSE_STANDARD_NAME\n        Accounts queries all accounts\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Payments(self, request, context):
        'buf:lint:ignore RPC_REQUEST_RESPONSE_UNIQUE\n        buf:lint:ignore RPC_RESPONSE_STANDARD_NAME\n        Payments queries all payments\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Accounts': grpc.unary_unary_rpc_method_handler(servicer.Accounts, request_deserializer=akash_dot_escrow_dot_v1beta2_dot_query__pb2.QueryAccountsRequest.FromString, response_serializer=akash_dot_escrow_dot_v1beta2_dot_query__pb2.QueryAccountsResponse.SerializeToString), 'Payments': grpc.unary_unary_rpc_method_handler(servicer.Payments, request_deserializer=akash_dot_escrow_dot_v1beta2_dot_query__pb2.QueryPaymentsRequest.FromString, response_serializer=akash_dot_escrow_dot_v1beta2_dot_query__pb2.QueryPaymentsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('akash.escrow.v1beta2.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    'Query defines the gRPC querier service\n    '

    @staticmethod
    def Accounts(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.escrow.v1beta2.Query/Accounts', akash_dot_escrow_dot_v1beta2_dot_query__pb2.QueryAccountsRequest.SerializeToString, akash_dot_escrow_dot_v1beta2_dot_query__pb2.QueryAccountsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Payments(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.escrow.v1beta2.Query/Payments', akash_dot_escrow_dot_v1beta2_dot_query__pb2.QueryPaymentsRequest.SerializeToString, akash_dot_escrow_dot_v1beta2_dot_query__pb2.QueryPaymentsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
