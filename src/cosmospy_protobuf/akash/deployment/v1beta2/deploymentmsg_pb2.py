
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.deployment.v1beta2 import deployment_pb2 as akash_dot_deployment_dot_v1beta2_dot_deployment__pb2
from ....akash.deployment.v1beta2 import groupspec_pb2 as akash_dot_deployment_dot_v1beta2_dot_groupspec__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,akash/deployment/v1beta2/deploymentmsg.proto\x12\x18akash.deployment.v1beta2\x1a\x14gogoproto/gogo.proto\x1a)akash/deployment/v1beta2/deployment.proto\x1a(akash/deployment/v1beta2/groupspec.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\xf9\x02\n\x13MsgCreateDeployment\x12Q\n\x02id\x18\x01 \x01(\x0b2&.akash.deployment.v1beta2.DeploymentIDB\x1d\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"\x12T\n\x06groups\x18\x02 \x03(\x0b2#.akash.deployment.v1beta2.GroupSpecB\x1f\xc8\xde\x1f\x00\xea\xde\x1f\x06groups\xf2\xde\x1f\ryaml:"groups"\x12.\n\x07version\x18\x03 \x01(\x0cB\x1d\xea\xde\x1f\x07version\xf2\xde\x1f\x0eyaml:"version"\x12M\n\x07deposit\x18\x04 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB!\xc8\xde\x1f\x00\xea\xde\x1f\x07deposit\xf2\xde\x1f\x0eyaml:"deposit"\x124\n\tdepositor\x18\x05 \x01(\tB!\xea\xde\x1f\tdepositor\xf2\xde\x1f\x10yaml:"depositor":\x04\xe8\xa0\x1f\x00"\x1d\n\x1bMsgCreateDeploymentResponse"\xf1\x01\n\x14MsgDepositDeployment\x12Q\n\x02id\x18\x01 \x01(\x0b2&.akash.deployment.v1beta2.DeploymentIDB\x1d\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"\x12J\n\x06amount\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x1f\xc8\xde\x1f\x00\xea\xde\x1f\x06amount\xf2\xde\x1f\ryaml:"amount"\x124\n\tdepositor\x18\x03 \x01(\tB!\xea\xde\x1f\tdepositor\xf2\xde\x1f\x10yaml:"depositor":\x04\xe8\xa0\x1f\x00"\x1e\n\x1cMsgDepositDeploymentResponse"\x9e\x01\n\x13MsgUpdateDeployment\x12Q\n\x02id\x18\x01 \x01(\x0b2&.akash.deployment.v1beta2.DeploymentIDB\x1d\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"\x12.\n\x07version\x18\x03 \x01(\x0cB\x1d\xea\xde\x1f\x07version\xf2\xde\x1f\x0eyaml:"version":\x04\xe8\xa0\x1f\x00"\x1d\n\x1bMsgUpdateDeploymentResponse"m\n\x12MsgCloseDeployment\x12Q\n\x02id\x18\x01 \x01(\x0b2&.akash.deployment.v1beta2.DeploymentIDB\x1d\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id":\x04\xe8\xa0\x1f\x00"\x1c\n\x1aMsgCloseDeploymentResponseB4Z2github.com/ovrclk/akash/x/deployment/types/v1beta2b\x06proto3')
_MSGCREATEDEPLOYMENT = DESCRIPTOR.message_types_by_name['MsgCreateDeployment']
_MSGCREATEDEPLOYMENTRESPONSE = DESCRIPTOR.message_types_by_name['MsgCreateDeploymentResponse']
_MSGDEPOSITDEPLOYMENT = DESCRIPTOR.message_types_by_name['MsgDepositDeployment']
_MSGDEPOSITDEPLOYMENTRESPONSE = DESCRIPTOR.message_types_by_name['MsgDepositDeploymentResponse']
_MSGUPDATEDEPLOYMENT = DESCRIPTOR.message_types_by_name['MsgUpdateDeployment']
_MSGUPDATEDEPLOYMENTRESPONSE = DESCRIPTOR.message_types_by_name['MsgUpdateDeploymentResponse']
_MSGCLOSEDEPLOYMENT = DESCRIPTOR.message_types_by_name['MsgCloseDeployment']
_MSGCLOSEDEPLOYMENTRESPONSE = DESCRIPTOR.message_types_by_name['MsgCloseDeploymentResponse']
MsgCreateDeployment = _reflection.GeneratedProtocolMessageType('MsgCreateDeployment', (_message.Message,), {'DESCRIPTOR': _MSGCREATEDEPLOYMENT, '__module__': 'akash.deployment.v1beta2.deploymentmsg_pb2'})
_sym_db.RegisterMessage(MsgCreateDeployment)
MsgCreateDeploymentResponse = _reflection.GeneratedProtocolMessageType('MsgCreateDeploymentResponse', (_message.Message,), {'DESCRIPTOR': _MSGCREATEDEPLOYMENTRESPONSE, '__module__': 'akash.deployment.v1beta2.deploymentmsg_pb2'})
_sym_db.RegisterMessage(MsgCreateDeploymentResponse)
MsgDepositDeployment = _reflection.GeneratedProtocolMessageType('MsgDepositDeployment', (_message.Message,), {'DESCRIPTOR': _MSGDEPOSITDEPLOYMENT, '__module__': 'akash.deployment.v1beta2.deploymentmsg_pb2'})
_sym_db.RegisterMessage(MsgDepositDeployment)
MsgDepositDeploymentResponse = _reflection.GeneratedProtocolMessageType('MsgDepositDeploymentResponse', (_message.Message,), {'DESCRIPTOR': _MSGDEPOSITDEPLOYMENTRESPONSE, '__module__': 'akash.deployment.v1beta2.deploymentmsg_pb2'})
_sym_db.RegisterMessage(MsgDepositDeploymentResponse)
MsgUpdateDeployment = _reflection.GeneratedProtocolMessageType('MsgUpdateDeployment', (_message.Message,), {'DESCRIPTOR': _MSGUPDATEDEPLOYMENT, '__module__': 'akash.deployment.v1beta2.deploymentmsg_pb2'})
_sym_db.RegisterMessage(MsgUpdateDeployment)
MsgUpdateDeploymentResponse = _reflection.GeneratedProtocolMessageType('MsgUpdateDeploymentResponse', (_message.Message,), {'DESCRIPTOR': _MSGUPDATEDEPLOYMENTRESPONSE, '__module__': 'akash.deployment.v1beta2.deploymentmsg_pb2'})
_sym_db.RegisterMessage(MsgUpdateDeploymentResponse)
MsgCloseDeployment = _reflection.GeneratedProtocolMessageType('MsgCloseDeployment', (_message.Message,), {'DESCRIPTOR': _MSGCLOSEDEPLOYMENT, '__module__': 'akash.deployment.v1beta2.deploymentmsg_pb2'})
_sym_db.RegisterMessage(MsgCloseDeployment)
MsgCloseDeploymentResponse = _reflection.GeneratedProtocolMessageType('MsgCloseDeploymentResponse', (_message.Message,), {'DESCRIPTOR': _MSGCLOSEDEPLOYMENTRESPONSE, '__module__': 'akash.deployment.v1beta2.deploymentmsg_pb2'})
_sym_db.RegisterMessage(MsgCloseDeploymentResponse)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2github.com/ovrclk/akash/x/deployment/types/v1beta2'
    _MSGCREATEDEPLOYMENT.fields_by_name['id']._options = None
    _MSGCREATEDEPLOYMENT.fields_by_name['id']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"'
    _MSGCREATEDEPLOYMENT.fields_by_name['groups']._options = None
    _MSGCREATEDEPLOYMENT.fields_by_name['groups']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x06groups\xf2\xde\x1f\ryaml:"groups"'
    _MSGCREATEDEPLOYMENT.fields_by_name['version']._options = None
    _MSGCREATEDEPLOYMENT.fields_by_name['version']._serialized_options = b'\xea\xde\x1f\x07version\xf2\xde\x1f\x0eyaml:"version"'
    _MSGCREATEDEPLOYMENT.fields_by_name['deposit']._options = None
    _MSGCREATEDEPLOYMENT.fields_by_name['deposit']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x07deposit\xf2\xde\x1f\x0eyaml:"deposit"'
    _MSGCREATEDEPLOYMENT.fields_by_name['depositor']._options = None
    _MSGCREATEDEPLOYMENT.fields_by_name['depositor']._serialized_options = b'\xea\xde\x1f\tdepositor\xf2\xde\x1f\x10yaml:"depositor"'
    _MSGCREATEDEPLOYMENT._options = None
    _MSGCREATEDEPLOYMENT._serialized_options = b'\xe8\xa0\x1f\x00'
    _MSGDEPOSITDEPLOYMENT.fields_by_name['id']._options = None
    _MSGDEPOSITDEPLOYMENT.fields_by_name['id']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"'
    _MSGDEPOSITDEPLOYMENT.fields_by_name['amount']._options = None
    _MSGDEPOSITDEPLOYMENT.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x06amount\xf2\xde\x1f\ryaml:"amount"'
    _MSGDEPOSITDEPLOYMENT.fields_by_name['depositor']._options = None
    _MSGDEPOSITDEPLOYMENT.fields_by_name['depositor']._serialized_options = b'\xea\xde\x1f\tdepositor\xf2\xde\x1f\x10yaml:"depositor"'
    _MSGDEPOSITDEPLOYMENT._options = None
    _MSGDEPOSITDEPLOYMENT._serialized_options = b'\xe8\xa0\x1f\x00'
    _MSGUPDATEDEPLOYMENT.fields_by_name['id']._options = None
    _MSGUPDATEDEPLOYMENT.fields_by_name['id']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"'
    _MSGUPDATEDEPLOYMENT.fields_by_name['version']._options = None
    _MSGUPDATEDEPLOYMENT.fields_by_name['version']._serialized_options = b'\xea\xde\x1f\x07version\xf2\xde\x1f\x0eyaml:"version"'
    _MSGUPDATEDEPLOYMENT._options = None
    _MSGUPDATEDEPLOYMENT._serialized_options = b'\xe8\xa0\x1f\x00'
    _MSGCLOSEDEPLOYMENT.fields_by_name['id']._options = None
    _MSGCLOSEDEPLOYMENT.fields_by_name['id']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"'
    _MSGCLOSEDEPLOYMENT._options = None
    _MSGCLOSEDEPLOYMENT._serialized_options = b'\xe8\xa0\x1f\x00'
    _MSGCREATEDEPLOYMENT._serialized_start = 214
    _MSGCREATEDEPLOYMENT._serialized_end = 591
    _MSGCREATEDEPLOYMENTRESPONSE._serialized_start = 593
    _MSGCREATEDEPLOYMENTRESPONSE._serialized_end = 622
    _MSGDEPOSITDEPLOYMENT._serialized_start = 625
    _MSGDEPOSITDEPLOYMENT._serialized_end = 866
    _MSGDEPOSITDEPLOYMENTRESPONSE._serialized_start = 868
    _MSGDEPOSITDEPLOYMENTRESPONSE._serialized_end = 898
    _MSGUPDATEDEPLOYMENT._serialized_start = 901
    _MSGUPDATEDEPLOYMENT._serialized_end = 1059
    _MSGUPDATEDEPLOYMENTRESPONSE._serialized_start = 1061
    _MSGUPDATEDEPLOYMENTRESPONSE._serialized_end = 1090
    _MSGCLOSEDEPLOYMENT._serialized_start = 1092
    _MSGCLOSEDEPLOYMENT._serialized_end = 1201
    _MSGCLOSEDEPLOYMENTRESPONSE._serialized_start = 1203
    _MSGCLOSEDEPLOYMENTRESPONSE._serialized_end = 1231
