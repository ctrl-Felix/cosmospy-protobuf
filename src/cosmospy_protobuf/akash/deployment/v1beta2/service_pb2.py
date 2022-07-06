
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....akash.deployment.v1beta2 import deploymentmsg_pb2 as akash_dot_deployment_dot_v1beta2_dot_deploymentmsg__pb2
from ....akash.deployment.v1beta2 import groupmsg_pb2 as akash_dot_deployment_dot_v1beta2_dot_groupmsg__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b"\n&akash/deployment/v1beta2/service.proto\x12\x18akash.deployment.v1beta2\x1a,akash/deployment/v1beta2/deploymentmsg.proto\x1a'akash/deployment/v1beta2/groupmsg.proto2\xa5\x06\n\x03Msg\x12x\n\x10CreateDeployment\x12-.akash.deployment.v1beta2.MsgCreateDeployment\x1a5.akash.deployment.v1beta2.MsgCreateDeploymentResponse\x12{\n\x11DepositDeployment\x12..akash.deployment.v1beta2.MsgDepositDeployment\x1a6.akash.deployment.v1beta2.MsgDepositDeploymentResponse\x12x\n\x10UpdateDeployment\x12-.akash.deployment.v1beta2.MsgUpdateDeployment\x1a5.akash.deployment.v1beta2.MsgUpdateDeploymentResponse\x12u\n\x0fCloseDeployment\x12,.akash.deployment.v1beta2.MsgCloseDeployment\x1a4.akash.deployment.v1beta2.MsgCloseDeploymentResponse\x12f\n\nCloseGroup\x12'.akash.deployment.v1beta2.MsgCloseGroup\x1a/.akash.deployment.v1beta2.MsgCloseGroupResponse\x12f\n\nPauseGroup\x12'.akash.deployment.v1beta2.MsgPauseGroup\x1a/.akash.deployment.v1beta2.MsgPauseGroupResponse\x12f\n\nStartGroup\x12'.akash.deployment.v1beta2.MsgStartGroup\x1a/.akash.deployment.v1beta2.MsgStartGroupResponseB4Z2github.com/ovrclk/akash/x/deployment/types/v1beta2b\x06proto3")
_MSG = DESCRIPTOR.services_by_name['Msg']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2github.com/ovrclk/akash/x/deployment/types/v1beta2'
    _MSG._serialized_start = 156
    _MSG._serialized_end = 961
