
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ....cosmos.app.v1alpha1 import query_pb2 as cosmos_dot_app_dot_v1alpha1_dot_query__pb2

class QueryStub(object):
    'Query is the app module query service.\n    '

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.Config = channel.unary_unary('/cosmos.app.v1alpha1.Query/Config', request_serializer=cosmos_dot_app_dot_v1alpha1_dot_query__pb2.QueryConfigRequest.SerializeToString, response_deserializer=cosmos_dot_app_dot_v1alpha1_dot_query__pb2.QueryConfigResponse.FromString)

class QueryServicer(object):
    'Query is the app module query service.\n    '

    def Config(self, request, context):
        'Config returns the current app config.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Config': grpc.unary_unary_rpc_method_handler(servicer.Config, request_deserializer=cosmos_dot_app_dot_v1alpha1_dot_query__pb2.QueryConfigRequest.FromString, response_serializer=cosmos_dot_app_dot_v1alpha1_dot_query__pb2.QueryConfigResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('cosmos.app.v1alpha1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    'Query is the app module query service.\n    '

    @staticmethod
    def Config(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.app.v1alpha1.Query/Config', cosmos_dot_app_dot_v1alpha1_dot_query__pb2.QueryConfigRequest.SerializeToString, cosmos_dot_app_dot_v1alpha1_dot_query__pb2.QueryConfigResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
