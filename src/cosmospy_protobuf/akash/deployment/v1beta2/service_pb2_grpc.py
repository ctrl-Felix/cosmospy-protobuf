
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ....akash.deployment.v1beta2 import deploymentmsg_pb2 as akash_dot_deployment_dot_v1beta2_dot_deploymentmsg__pb2
from ....akash.deployment.v1beta2 import groupmsg_pb2 as akash_dot_deployment_dot_v1beta2_dot_groupmsg__pb2

class MsgStub(object):
    'Msg defines the deployment Msg service.\n    '

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.CreateDeployment = channel.unary_unary('/akash.deployment.v1beta2.Msg/CreateDeployment', request_serializer=akash_dot_deployment_dot_v1beta2_dot_deploymentmsg__pb2.MsgCreateDeployment.SerializeToString, response_deserializer=akash_dot_deployment_dot_v1beta2_dot_deploymentmsg__pb2.MsgCreateDeploymentResponse.FromString)
        self.DepositDeployment = channel.unary_unary('/akash.deployment.v1beta2.Msg/DepositDeployment', request_serializer=akash_dot_deployment_dot_v1beta2_dot_deploymentmsg__pb2.MsgDepositDeployment.SerializeToString, response_deserializer=akash_dot_deployment_dot_v1beta2_dot_deploymentmsg__pb2.MsgDepositDeploymentResponse.FromString)
        self.UpdateDeployment = channel.unary_unary('/akash.deployment.v1beta2.Msg/UpdateDeployment', request_serializer=akash_dot_deployment_dot_v1beta2_dot_deploymentmsg__pb2.MsgUpdateDeployment.SerializeToString, response_deserializer=akash_dot_deployment_dot_v1beta2_dot_deploymentmsg__pb2.MsgUpdateDeploymentResponse.FromString)
        self.CloseDeployment = channel.unary_unary('/akash.deployment.v1beta2.Msg/CloseDeployment', request_serializer=akash_dot_deployment_dot_v1beta2_dot_deploymentmsg__pb2.MsgCloseDeployment.SerializeToString, response_deserializer=akash_dot_deployment_dot_v1beta2_dot_deploymentmsg__pb2.MsgCloseDeploymentResponse.FromString)
        self.CloseGroup = channel.unary_unary('/akash.deployment.v1beta2.Msg/CloseGroup', request_serializer=akash_dot_deployment_dot_v1beta2_dot_groupmsg__pb2.MsgCloseGroup.SerializeToString, response_deserializer=akash_dot_deployment_dot_v1beta2_dot_groupmsg__pb2.MsgCloseGroupResponse.FromString)
        self.PauseGroup = channel.unary_unary('/akash.deployment.v1beta2.Msg/PauseGroup', request_serializer=akash_dot_deployment_dot_v1beta2_dot_groupmsg__pb2.MsgPauseGroup.SerializeToString, response_deserializer=akash_dot_deployment_dot_v1beta2_dot_groupmsg__pb2.MsgPauseGroupResponse.FromString)
        self.StartGroup = channel.unary_unary('/akash.deployment.v1beta2.Msg/StartGroup', request_serializer=akash_dot_deployment_dot_v1beta2_dot_groupmsg__pb2.MsgStartGroup.SerializeToString, response_deserializer=akash_dot_deployment_dot_v1beta2_dot_groupmsg__pb2.MsgStartGroupResponse.FromString)

class MsgServicer(object):
    'Msg defines the deployment Msg service.\n    '

    def CreateDeployment(self, request, context):
        'CreateDeployment defines a method to create new deployment given proper inputs.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DepositDeployment(self, request, context):
        'DepositDeployment deposits more funds into the deployment account\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateDeployment(self, request, context):
        'UpdateDeployment defines a method to update a deployment given proper inputs.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloseDeployment(self, request, context):
        'CloseDeployment defines a method to close a deployment given proper inputs.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloseGroup(self, request, context):
        'CloseGroup defines a method to close a group of a deployment given proper inputs.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PauseGroup(self, request, context):
        'PauseGroup defines a method to close a group of a deployment given proper inputs.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartGroup(self, request, context):
        'StartGroup defines a method to close a group of a deployment given proper inputs.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {'CreateDeployment': grpc.unary_unary_rpc_method_handler(servicer.CreateDeployment, request_deserializer=akash_dot_deployment_dot_v1beta2_dot_deploymentmsg__pb2.MsgCreateDeployment.FromString, response_serializer=akash_dot_deployment_dot_v1beta2_dot_deploymentmsg__pb2.MsgCreateDeploymentResponse.SerializeToString), 'DepositDeployment': grpc.unary_unary_rpc_method_handler(servicer.DepositDeployment, request_deserializer=akash_dot_deployment_dot_v1beta2_dot_deploymentmsg__pb2.MsgDepositDeployment.FromString, response_serializer=akash_dot_deployment_dot_v1beta2_dot_deploymentmsg__pb2.MsgDepositDeploymentResponse.SerializeToString), 'UpdateDeployment': grpc.unary_unary_rpc_method_handler(servicer.UpdateDeployment, request_deserializer=akash_dot_deployment_dot_v1beta2_dot_deploymentmsg__pb2.MsgUpdateDeployment.FromString, response_serializer=akash_dot_deployment_dot_v1beta2_dot_deploymentmsg__pb2.MsgUpdateDeploymentResponse.SerializeToString), 'CloseDeployment': grpc.unary_unary_rpc_method_handler(servicer.CloseDeployment, request_deserializer=akash_dot_deployment_dot_v1beta2_dot_deploymentmsg__pb2.MsgCloseDeployment.FromString, response_serializer=akash_dot_deployment_dot_v1beta2_dot_deploymentmsg__pb2.MsgCloseDeploymentResponse.SerializeToString), 'CloseGroup': grpc.unary_unary_rpc_method_handler(servicer.CloseGroup, request_deserializer=akash_dot_deployment_dot_v1beta2_dot_groupmsg__pb2.MsgCloseGroup.FromString, response_serializer=akash_dot_deployment_dot_v1beta2_dot_groupmsg__pb2.MsgCloseGroupResponse.SerializeToString), 'PauseGroup': grpc.unary_unary_rpc_method_handler(servicer.PauseGroup, request_deserializer=akash_dot_deployment_dot_v1beta2_dot_groupmsg__pb2.MsgPauseGroup.FromString, response_serializer=akash_dot_deployment_dot_v1beta2_dot_groupmsg__pb2.MsgPauseGroupResponse.SerializeToString), 'StartGroup': grpc.unary_unary_rpc_method_handler(servicer.StartGroup, request_deserializer=akash_dot_deployment_dot_v1beta2_dot_groupmsg__pb2.MsgStartGroup.FromString, response_serializer=akash_dot_deployment_dot_v1beta2_dot_groupmsg__pb2.MsgStartGroupResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('akash.deployment.v1beta2.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Msg(object):
    'Msg defines the deployment Msg service.\n    '

    @staticmethod
    def CreateDeployment(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.deployment.v1beta2.Msg/CreateDeployment', akash_dot_deployment_dot_v1beta2_dot_deploymentmsg__pb2.MsgCreateDeployment.SerializeToString, akash_dot_deployment_dot_v1beta2_dot_deploymentmsg__pb2.MsgCreateDeploymentResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DepositDeployment(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.deployment.v1beta2.Msg/DepositDeployment', akash_dot_deployment_dot_v1beta2_dot_deploymentmsg__pb2.MsgDepositDeployment.SerializeToString, akash_dot_deployment_dot_v1beta2_dot_deploymentmsg__pb2.MsgDepositDeploymentResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateDeployment(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.deployment.v1beta2.Msg/UpdateDeployment', akash_dot_deployment_dot_v1beta2_dot_deploymentmsg__pb2.MsgUpdateDeployment.SerializeToString, akash_dot_deployment_dot_v1beta2_dot_deploymentmsg__pb2.MsgUpdateDeploymentResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CloseDeployment(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.deployment.v1beta2.Msg/CloseDeployment', akash_dot_deployment_dot_v1beta2_dot_deploymentmsg__pb2.MsgCloseDeployment.SerializeToString, akash_dot_deployment_dot_v1beta2_dot_deploymentmsg__pb2.MsgCloseDeploymentResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CloseGroup(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.deployment.v1beta2.Msg/CloseGroup', akash_dot_deployment_dot_v1beta2_dot_groupmsg__pb2.MsgCloseGroup.SerializeToString, akash_dot_deployment_dot_v1beta2_dot_groupmsg__pb2.MsgCloseGroupResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PauseGroup(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.deployment.v1beta2.Msg/PauseGroup', akash_dot_deployment_dot_v1beta2_dot_groupmsg__pb2.MsgPauseGroup.SerializeToString, akash_dot_deployment_dot_v1beta2_dot_groupmsg__pb2.MsgPauseGroupResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartGroup(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.deployment.v1beta2.Msg/StartGroup', akash_dot_deployment_dot_v1beta2_dot_groupmsg__pb2.MsgStartGroup.SerializeToString, akash_dot_deployment_dot_v1beta2_dot_groupmsg__pb2.MsgStartGroupResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
