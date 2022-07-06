
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ....akash.deployment.v1beta2 import query_pb2 as akash_dot_deployment_dot_v1beta2_dot_query__pb2

class QueryStub(object):
    'Query defines the gRPC querier service\n    '

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.Deployments = channel.unary_unary('/akash.deployment.v1beta2.Query/Deployments', request_serializer=akash_dot_deployment_dot_v1beta2_dot_query__pb2.QueryDeploymentsRequest.SerializeToString, response_deserializer=akash_dot_deployment_dot_v1beta2_dot_query__pb2.QueryDeploymentsResponse.FromString)
        self.Deployment = channel.unary_unary('/akash.deployment.v1beta2.Query/Deployment', request_serializer=akash_dot_deployment_dot_v1beta2_dot_query__pb2.QueryDeploymentRequest.SerializeToString, response_deserializer=akash_dot_deployment_dot_v1beta2_dot_query__pb2.QueryDeploymentResponse.FromString)
        self.Group = channel.unary_unary('/akash.deployment.v1beta2.Query/Group', request_serializer=akash_dot_deployment_dot_v1beta2_dot_query__pb2.QueryGroupRequest.SerializeToString, response_deserializer=akash_dot_deployment_dot_v1beta2_dot_query__pb2.QueryGroupResponse.FromString)

class QueryServicer(object):
    'Query defines the gRPC querier service\n    '

    def Deployments(self, request, context):
        'Deployments queries deployments\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Deployment(self, request, context):
        'Deployment queries deployment details\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Group(self, request, context):
        'Group queries group details\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Deployments': grpc.unary_unary_rpc_method_handler(servicer.Deployments, request_deserializer=akash_dot_deployment_dot_v1beta2_dot_query__pb2.QueryDeploymentsRequest.FromString, response_serializer=akash_dot_deployment_dot_v1beta2_dot_query__pb2.QueryDeploymentsResponse.SerializeToString), 'Deployment': grpc.unary_unary_rpc_method_handler(servicer.Deployment, request_deserializer=akash_dot_deployment_dot_v1beta2_dot_query__pb2.QueryDeploymentRequest.FromString, response_serializer=akash_dot_deployment_dot_v1beta2_dot_query__pb2.QueryDeploymentResponse.SerializeToString), 'Group': grpc.unary_unary_rpc_method_handler(servicer.Group, request_deserializer=akash_dot_deployment_dot_v1beta2_dot_query__pb2.QueryGroupRequest.FromString, response_serializer=akash_dot_deployment_dot_v1beta2_dot_query__pb2.QueryGroupResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('akash.deployment.v1beta2.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    'Query defines the gRPC querier service\n    '

    @staticmethod
    def Deployments(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.deployment.v1beta2.Query/Deployments', akash_dot_deployment_dot_v1beta2_dot_query__pb2.QueryDeploymentsRequest.SerializeToString, akash_dot_deployment_dot_v1beta2_dot_query__pb2.QueryDeploymentsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Deployment(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.deployment.v1beta2.Query/Deployment', akash_dot_deployment_dot_v1beta2_dot_query__pb2.QueryDeploymentRequest.SerializeToString, akash_dot_deployment_dot_v1beta2_dot_query__pb2.QueryDeploymentResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Group(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.deployment.v1beta2.Query/Group', akash_dot_deployment_dot_v1beta2_dot_query__pb2.QueryGroupRequest.SerializeToString, akash_dot_deployment_dot_v1beta2_dot_query__pb2.QueryGroupResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
