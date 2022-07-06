
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.deployment.v1beta1 import group_pb2 as akash_dot_deployment_dot_v1beta1_dot_group__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)akash/deployment/v1beta1/deployment.proto\x12\x18akash.deployment.v1beta1\x1a\x14gogoproto/gogo.proto\x1a$akash/deployment/v1beta1/group.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\xc3\x02\n\x13MsgCreateDeployment\x12Q\n\x02id\x18\x01 \x01(\x0b2&.akash.deployment.v1beta1.DeploymentIDB\x1d\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"\x12T\n\x06groups\x18\x02 \x03(\x0b2#.akash.deployment.v1beta1.GroupSpecB\x1f\xc8\xde\x1f\x00\xea\xde\x1f\x06groups\xf2\xde\x1f\ryaml:"groups"\x12.\n\x07version\x18\x03 \x01(\x0cB\x1d\xea\xde\x1f\x07version\xf2\xde\x1f\x0eyaml:"version"\x12M\n\x07deposit\x18\x04 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB!\xc8\xde\x1f\x00\xea\xde\x1f\x07deposit\xf2\xde\x1f\x0eyaml:"deposit":\x04\xe8\xa0\x1f\x00"\x1d\n\x1bMsgCreateDeploymentResponse"\xbb\x01\n\x14MsgDepositDeployment\x12Q\n\x02id\x18\x01 \x01(\x0b2&.akash.deployment.v1beta1.DeploymentIDB\x1d\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"\x12J\n\x06amount\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x1f\xc8\xde\x1f\x00\xea\xde\x1f\x06amount\xf2\xde\x1f\ryaml:"amount":\x04\xe8\xa0\x1f\x00"\x1e\n\x1cMsgDepositDeploymentResponse"\xf4\x01\n\x13MsgUpdateDeployment\x12Q\n\x02id\x18\x01 \x01(\x0b2&.akash.deployment.v1beta1.DeploymentIDB\x1d\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"\x12T\n\x06groups\x18\x02 \x03(\x0b2#.akash.deployment.v1beta1.GroupSpecB\x1f\xc8\xde\x1f\x00\xea\xde\x1f\x06groups\xf2\xde\x1f\ryaml:"groups"\x12.\n\x07version\x18\x03 \x01(\x0cB\x1d\xea\xde\x1f\x07version\xf2\xde\x1f\x0eyaml:"version":\x04\xe8\xa0\x1f\x00"\x1d\n\x1bMsgUpdateDeploymentResponse"m\n\x12MsgCloseDeployment\x12Q\n\x02id\x18\x01 \x01(\x0b2&.akash.deployment.v1beta1.DeploymentIDB\x1d\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id":\x04\xe8\xa0\x1f\x00"\x1c\n\x1aMsgCloseDeploymentResponse"q\n\x0cDeploymentID\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12-\n\x04dseq\x18\x02 \x01(\x04B\x1f\xe2\xde\x1f\x04DSeq\xea\xde\x1f\x04dseq\xf2\xde\x1f\x0byaml:"dseq":\x08\xe8\xa0\x1f\x00\x98\xa0\x1f\x00"\x90\x03\n\nDeployment\x12f\n\rdeployment_id\x18\x01 \x01(\x0b2&.akash.deployment.v1beta1.DeploymentIDB\'\xc8\xde\x1f\x00\xe2\xde\x1f\x0cDeploymentID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"\x12T\n\x05state\x18\x02 \x01(\x0e2*.akash.deployment.v1beta1.Deployment.StateB\x19\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state"\x12.\n\x07version\x18\x03 \x01(\x0cB\x1d\xea\xde\x1f\x07version\xf2\xde\x1f\x0eyaml:"version"\x12\x12\n\ncreated_at\x18\x04 \x01(\x03"z\n\x05State\x12\'\n\x07invalid\x10\x00\x1a\x1a\x8a\x9d \x16DeploymentStateInvalid\x12 \n\x06active\x10\x01\x1a\x14\x8a\x9d \x10DeploymentActive\x12 \n\x06closed\x10\x02\x1a\x14\x8a\x9d \x10DeploymentClosed\x1a\x04\x88\xa3\x1e\x00:\x04\xe8\xa0\x1f\x00"\x9c\x01\n\x11DeploymentFilters\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12-\n\x04dseq\x18\x02 \x01(\x04B\x1f\xe2\xde\x1f\x04DSeq\xea\xde\x1f\x04dseq\xf2\xde\x1f\x0byaml:"dseq"\x12(\n\x05state\x18\x03 \x01(\tB\x19\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state":\x04\xe8\xa0\x1f\x002\xa5\x06\n\x03Msg\x12x\n\x10CreateDeployment\x12-.akash.deployment.v1beta1.MsgCreateDeployment\x1a5.akash.deployment.v1beta1.MsgCreateDeploymentResponse\x12{\n\x11DepositDeployment\x12..akash.deployment.v1beta1.MsgDepositDeployment\x1a6.akash.deployment.v1beta1.MsgDepositDeploymentResponse\x12x\n\x10UpdateDeployment\x12-.akash.deployment.v1beta1.MsgUpdateDeployment\x1a5.akash.deployment.v1beta1.MsgUpdateDeploymentResponse\x12u\n\x0fCloseDeployment\x12,.akash.deployment.v1beta1.MsgCloseDeployment\x1a4.akash.deployment.v1beta1.MsgCloseDeploymentResponse\x12f\n\nCloseGroup\x12\'.akash.deployment.v1beta1.MsgCloseGroup\x1a/.akash.deployment.v1beta1.MsgCloseGroupResponse\x12f\n\nPauseGroup\x12\'.akash.deployment.v1beta1.MsgPauseGroup\x1a/.akash.deployment.v1beta1.MsgPauseGroupResponse\x12f\n\nStartGroup\x12\'.akash.deployment.v1beta1.MsgStartGroup\x1a/.akash.deployment.v1beta1.MsgStartGroupResponseB4Z2github.com/ovrclk/akash/x/deployment/types/v1beta1b\x06proto3')
_MSGCREATEDEPLOYMENT = DESCRIPTOR.message_types_by_name['MsgCreateDeployment']
_MSGCREATEDEPLOYMENTRESPONSE = DESCRIPTOR.message_types_by_name['MsgCreateDeploymentResponse']
_MSGDEPOSITDEPLOYMENT = DESCRIPTOR.message_types_by_name['MsgDepositDeployment']
_MSGDEPOSITDEPLOYMENTRESPONSE = DESCRIPTOR.message_types_by_name['MsgDepositDeploymentResponse']
_MSGUPDATEDEPLOYMENT = DESCRIPTOR.message_types_by_name['MsgUpdateDeployment']
_MSGUPDATEDEPLOYMENTRESPONSE = DESCRIPTOR.message_types_by_name['MsgUpdateDeploymentResponse']
_MSGCLOSEDEPLOYMENT = DESCRIPTOR.message_types_by_name['MsgCloseDeployment']
_MSGCLOSEDEPLOYMENTRESPONSE = DESCRIPTOR.message_types_by_name['MsgCloseDeploymentResponse']
_DEPLOYMENTID = DESCRIPTOR.message_types_by_name['DeploymentID']
_DEPLOYMENT = DESCRIPTOR.message_types_by_name['Deployment']
_DEPLOYMENTFILTERS = DESCRIPTOR.message_types_by_name['DeploymentFilters']
_DEPLOYMENT_STATE = _DEPLOYMENT.enum_types_by_name['State']
MsgCreateDeployment = _reflection.GeneratedProtocolMessageType('MsgCreateDeployment', (_message.Message,), {'DESCRIPTOR': _MSGCREATEDEPLOYMENT, '__module__': 'akash.deployment.v1beta1.deployment_pb2'})
_sym_db.RegisterMessage(MsgCreateDeployment)
MsgCreateDeploymentResponse = _reflection.GeneratedProtocolMessageType('MsgCreateDeploymentResponse', (_message.Message,), {'DESCRIPTOR': _MSGCREATEDEPLOYMENTRESPONSE, '__module__': 'akash.deployment.v1beta1.deployment_pb2'})
_sym_db.RegisterMessage(MsgCreateDeploymentResponse)
MsgDepositDeployment = _reflection.GeneratedProtocolMessageType('MsgDepositDeployment', (_message.Message,), {'DESCRIPTOR': _MSGDEPOSITDEPLOYMENT, '__module__': 'akash.deployment.v1beta1.deployment_pb2'})
_sym_db.RegisterMessage(MsgDepositDeployment)
MsgDepositDeploymentResponse = _reflection.GeneratedProtocolMessageType('MsgDepositDeploymentResponse', (_message.Message,), {'DESCRIPTOR': _MSGDEPOSITDEPLOYMENTRESPONSE, '__module__': 'akash.deployment.v1beta1.deployment_pb2'})
_sym_db.RegisterMessage(MsgDepositDeploymentResponse)
MsgUpdateDeployment = _reflection.GeneratedProtocolMessageType('MsgUpdateDeployment', (_message.Message,), {'DESCRIPTOR': _MSGUPDATEDEPLOYMENT, '__module__': 'akash.deployment.v1beta1.deployment_pb2'})
_sym_db.RegisterMessage(MsgUpdateDeployment)
MsgUpdateDeploymentResponse = _reflection.GeneratedProtocolMessageType('MsgUpdateDeploymentResponse', (_message.Message,), {'DESCRIPTOR': _MSGUPDATEDEPLOYMENTRESPONSE, '__module__': 'akash.deployment.v1beta1.deployment_pb2'})
_sym_db.RegisterMessage(MsgUpdateDeploymentResponse)
MsgCloseDeployment = _reflection.GeneratedProtocolMessageType('MsgCloseDeployment', (_message.Message,), {'DESCRIPTOR': _MSGCLOSEDEPLOYMENT, '__module__': 'akash.deployment.v1beta1.deployment_pb2'})
_sym_db.RegisterMessage(MsgCloseDeployment)
MsgCloseDeploymentResponse = _reflection.GeneratedProtocolMessageType('MsgCloseDeploymentResponse', (_message.Message,), {'DESCRIPTOR': _MSGCLOSEDEPLOYMENTRESPONSE, '__module__': 'akash.deployment.v1beta1.deployment_pb2'})
_sym_db.RegisterMessage(MsgCloseDeploymentResponse)
DeploymentID = _reflection.GeneratedProtocolMessageType('DeploymentID', (_message.Message,), {'DESCRIPTOR': _DEPLOYMENTID, '__module__': 'akash.deployment.v1beta1.deployment_pb2'})
_sym_db.RegisterMessage(DeploymentID)
Deployment = _reflection.GeneratedProtocolMessageType('Deployment', (_message.Message,), {'DESCRIPTOR': _DEPLOYMENT, '__module__': 'akash.deployment.v1beta1.deployment_pb2'})
_sym_db.RegisterMessage(Deployment)
DeploymentFilters = _reflection.GeneratedProtocolMessageType('DeploymentFilters', (_message.Message,), {'DESCRIPTOR': _DEPLOYMENTFILTERS, '__module__': 'akash.deployment.v1beta1.deployment_pb2'})
_sym_db.RegisterMessage(DeploymentFilters)
_MSG = DESCRIPTOR.services_by_name['Msg']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2github.com/ovrclk/akash/x/deployment/types/v1beta1'
    _MSGCREATEDEPLOYMENT.fields_by_name['id']._options = None
    _MSGCREATEDEPLOYMENT.fields_by_name['id']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"'
    _MSGCREATEDEPLOYMENT.fields_by_name['groups']._options = None
    _MSGCREATEDEPLOYMENT.fields_by_name['groups']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x06groups\xf2\xde\x1f\ryaml:"groups"'
    _MSGCREATEDEPLOYMENT.fields_by_name['version']._options = None
    _MSGCREATEDEPLOYMENT.fields_by_name['version']._serialized_options = b'\xea\xde\x1f\x07version\xf2\xde\x1f\x0eyaml:"version"'
    _MSGCREATEDEPLOYMENT.fields_by_name['deposit']._options = None
    _MSGCREATEDEPLOYMENT.fields_by_name['deposit']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x07deposit\xf2\xde\x1f\x0eyaml:"deposit"'
    _MSGCREATEDEPLOYMENT._options = None
    _MSGCREATEDEPLOYMENT._serialized_options = b'\xe8\xa0\x1f\x00'
    _MSGDEPOSITDEPLOYMENT.fields_by_name['id']._options = None
    _MSGDEPOSITDEPLOYMENT.fields_by_name['id']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"'
    _MSGDEPOSITDEPLOYMENT.fields_by_name['amount']._options = None
    _MSGDEPOSITDEPLOYMENT.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x06amount\xf2\xde\x1f\ryaml:"amount"'
    _MSGDEPOSITDEPLOYMENT._options = None
    _MSGDEPOSITDEPLOYMENT._serialized_options = b'\xe8\xa0\x1f\x00'
    _MSGUPDATEDEPLOYMENT.fields_by_name['id']._options = None
    _MSGUPDATEDEPLOYMENT.fields_by_name['id']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"'
    _MSGUPDATEDEPLOYMENT.fields_by_name['groups']._options = None
    _MSGUPDATEDEPLOYMENT.fields_by_name['groups']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x06groups\xf2\xde\x1f\ryaml:"groups"'
    _MSGUPDATEDEPLOYMENT.fields_by_name['version']._options = None
    _MSGUPDATEDEPLOYMENT.fields_by_name['version']._serialized_options = b'\xea\xde\x1f\x07version\xf2\xde\x1f\x0eyaml:"version"'
    _MSGUPDATEDEPLOYMENT._options = None
    _MSGUPDATEDEPLOYMENT._serialized_options = b'\xe8\xa0\x1f\x00'
    _MSGCLOSEDEPLOYMENT.fields_by_name['id']._options = None
    _MSGCLOSEDEPLOYMENT.fields_by_name['id']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"'
    _MSGCLOSEDEPLOYMENT._options = None
    _MSGCLOSEDEPLOYMENT._serialized_options = b'\xe8\xa0\x1f\x00'
    _DEPLOYMENTID.fields_by_name['owner']._options = None
    _DEPLOYMENTID.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _DEPLOYMENTID.fields_by_name['dseq']._options = None
    _DEPLOYMENTID.fields_by_name['dseq']._serialized_options = b'\xe2\xde\x1f\x04DSeq\xea\xde\x1f\x04dseq\xf2\xde\x1f\x0byaml:"dseq"'
    _DEPLOYMENTID._options = None
    _DEPLOYMENTID._serialized_options = b'\xe8\xa0\x1f\x00\x98\xa0\x1f\x00'
    _DEPLOYMENT_STATE._options = None
    _DEPLOYMENT_STATE._serialized_options = b'\x88\xa3\x1e\x00'
    _DEPLOYMENT_STATE.values_by_name['invalid']._options = None
    _DEPLOYMENT_STATE.values_by_name['invalid']._serialized_options = b'\x8a\x9d \x16DeploymentStateInvalid'
    _DEPLOYMENT_STATE.values_by_name['active']._options = None
    _DEPLOYMENT_STATE.values_by_name['active']._serialized_options = b'\x8a\x9d \x10DeploymentActive'
    _DEPLOYMENT_STATE.values_by_name['closed']._options = None
    _DEPLOYMENT_STATE.values_by_name['closed']._serialized_options = b'\x8a\x9d \x10DeploymentClosed'
    _DEPLOYMENT.fields_by_name['deployment_id']._options = None
    _DEPLOYMENT.fields_by_name['deployment_id']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x0cDeploymentID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"'
    _DEPLOYMENT.fields_by_name['state']._options = None
    _DEPLOYMENT.fields_by_name['state']._serialized_options = b'\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state"'
    _DEPLOYMENT.fields_by_name['version']._options = None
    _DEPLOYMENT.fields_by_name['version']._serialized_options = b'\xea\xde\x1f\x07version\xf2\xde\x1f\x0eyaml:"version"'
    _DEPLOYMENT._options = None
    _DEPLOYMENT._serialized_options = b'\xe8\xa0\x1f\x00'
    _DEPLOYMENTFILTERS.fields_by_name['owner']._options = None
    _DEPLOYMENTFILTERS.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _DEPLOYMENTFILTERS.fields_by_name['dseq']._options = None
    _DEPLOYMENTFILTERS.fields_by_name['dseq']._serialized_options = b'\xe2\xde\x1f\x04DSeq\xea\xde\x1f\x04dseq\xf2\xde\x1f\x0byaml:"dseq"'
    _DEPLOYMENTFILTERS.fields_by_name['state']._options = None
    _DEPLOYMENTFILTERS.fields_by_name['state']._serialized_options = b'\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state"'
    _DEPLOYMENTFILTERS._options = None
    _DEPLOYMENTFILTERS._serialized_options = b'\xe8\xa0\x1f\x00'
    _MSGCREATEDEPLOYMENT._serialized_start = 164
    _MSGCREATEDEPLOYMENT._serialized_end = 487
    _MSGCREATEDEPLOYMENTRESPONSE._serialized_start = 489
    _MSGCREATEDEPLOYMENTRESPONSE._serialized_end = 518
    _MSGDEPOSITDEPLOYMENT._serialized_start = 521
    _MSGDEPOSITDEPLOYMENT._serialized_end = 708
    _MSGDEPOSITDEPLOYMENTRESPONSE._serialized_start = 710
    _MSGDEPOSITDEPLOYMENTRESPONSE._serialized_end = 740
    _MSGUPDATEDEPLOYMENT._serialized_start = 743
    _MSGUPDATEDEPLOYMENT._serialized_end = 987
    _MSGUPDATEDEPLOYMENTRESPONSE._serialized_start = 989
    _MSGUPDATEDEPLOYMENTRESPONSE._serialized_end = 1018
    _MSGCLOSEDEPLOYMENT._serialized_start = 1020
    _MSGCLOSEDEPLOYMENT._serialized_end = 1129
    _MSGCLOSEDEPLOYMENTRESPONSE._serialized_start = 1131
    _MSGCLOSEDEPLOYMENTRESPONSE._serialized_end = 1159
    _DEPLOYMENTID._serialized_start = 1161
    _DEPLOYMENTID._serialized_end = 1274
    _DEPLOYMENT._serialized_start = 1277
    _DEPLOYMENT._serialized_end = 1677
    _DEPLOYMENT_STATE._serialized_start = 1549
    _DEPLOYMENT_STATE._serialized_end = 1671
    _DEPLOYMENTFILTERS._serialized_start = 1680
    _DEPLOYMENTFILTERS._serialized_end = 1836
    _MSG._serialized_start = 1839
    _MSG._serialized_end = 2644
