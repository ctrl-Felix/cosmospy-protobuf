
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.deployment.v1beta2 import groupid_pb2 as akash_dot_deployment_dot_v1beta2_dot_groupid__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'akash/deployment/v1beta2/groupmsg.proto\x12\x18akash.deployment.v1beta2\x1a\x14gogoproto/gogo.proto\x1a&akash/deployment/v1beta2/groupid.proto"c\n\rMsgCloseGroup\x12L\n\x02id\x18\x01 \x01(\x0b2!.akash.deployment.v1beta2.GroupIDB\x1d\xe2\xde\x1f\x02ID\xc8\xde\x1f\x00\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id":\x04\xe8\xa0\x1f\x00"\x17\n\x15MsgCloseGroupResponse"c\n\rMsgPauseGroup\x12L\n\x02id\x18\x01 \x01(\x0b2!.akash.deployment.v1beta2.GroupIDB\x1d\xe2\xde\x1f\x02ID\xc8\xde\x1f\x00\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id":\x04\xe8\xa0\x1f\x00"\x17\n\x15MsgPauseGroupResponse"c\n\rMsgStartGroup\x12L\n\x02id\x18\x01 \x01(\x0b2!.akash.deployment.v1beta2.GroupIDB\x1d\xe2\xde\x1f\x02ID\xc8\xde\x1f\x00\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id":\x04\xe8\xa0\x1f\x00"\x17\n\x15MsgStartGroupResponseB4Z2github.com/ovrclk/akash/x/deployment/types/v1beta2b\x06proto3')
_MSGCLOSEGROUP = DESCRIPTOR.message_types_by_name['MsgCloseGroup']
_MSGCLOSEGROUPRESPONSE = DESCRIPTOR.message_types_by_name['MsgCloseGroupResponse']
_MSGPAUSEGROUP = DESCRIPTOR.message_types_by_name['MsgPauseGroup']
_MSGPAUSEGROUPRESPONSE = DESCRIPTOR.message_types_by_name['MsgPauseGroupResponse']
_MSGSTARTGROUP = DESCRIPTOR.message_types_by_name['MsgStartGroup']
_MSGSTARTGROUPRESPONSE = DESCRIPTOR.message_types_by_name['MsgStartGroupResponse']
MsgCloseGroup = _reflection.GeneratedProtocolMessageType('MsgCloseGroup', (_message.Message,), {'DESCRIPTOR': _MSGCLOSEGROUP, '__module__': 'akash.deployment.v1beta2.groupmsg_pb2'})
_sym_db.RegisterMessage(MsgCloseGroup)
MsgCloseGroupResponse = _reflection.GeneratedProtocolMessageType('MsgCloseGroupResponse', (_message.Message,), {'DESCRIPTOR': _MSGCLOSEGROUPRESPONSE, '__module__': 'akash.deployment.v1beta2.groupmsg_pb2'})
_sym_db.RegisterMessage(MsgCloseGroupResponse)
MsgPauseGroup = _reflection.GeneratedProtocolMessageType('MsgPauseGroup', (_message.Message,), {'DESCRIPTOR': _MSGPAUSEGROUP, '__module__': 'akash.deployment.v1beta2.groupmsg_pb2'})
_sym_db.RegisterMessage(MsgPauseGroup)
MsgPauseGroupResponse = _reflection.GeneratedProtocolMessageType('MsgPauseGroupResponse', (_message.Message,), {'DESCRIPTOR': _MSGPAUSEGROUPRESPONSE, '__module__': 'akash.deployment.v1beta2.groupmsg_pb2'})
_sym_db.RegisterMessage(MsgPauseGroupResponse)
MsgStartGroup = _reflection.GeneratedProtocolMessageType('MsgStartGroup', (_message.Message,), {'DESCRIPTOR': _MSGSTARTGROUP, '__module__': 'akash.deployment.v1beta2.groupmsg_pb2'})
_sym_db.RegisterMessage(MsgStartGroup)
MsgStartGroupResponse = _reflection.GeneratedProtocolMessageType('MsgStartGroupResponse', (_message.Message,), {'DESCRIPTOR': _MSGSTARTGROUPRESPONSE, '__module__': 'akash.deployment.v1beta2.groupmsg_pb2'})
_sym_db.RegisterMessage(MsgStartGroupResponse)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2github.com/ovrclk/akash/x/deployment/types/v1beta2'
    _MSGCLOSEGROUP.fields_by_name['id']._options = None
    _MSGCLOSEGROUP.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID\xc8\xde\x1f\x00\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"'
    _MSGCLOSEGROUP._options = None
    _MSGCLOSEGROUP._serialized_options = b'\xe8\xa0\x1f\x00'
    _MSGPAUSEGROUP.fields_by_name['id']._options = None
    _MSGPAUSEGROUP.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID\xc8\xde\x1f\x00\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"'
    _MSGPAUSEGROUP._options = None
    _MSGPAUSEGROUP._serialized_options = b'\xe8\xa0\x1f\x00'
    _MSGSTARTGROUP.fields_by_name['id']._options = None
    _MSGSTARTGROUP.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID\xc8\xde\x1f\x00\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"'
    _MSGSTARTGROUP._options = None
    _MSGSTARTGROUP._serialized_options = b'\xe8\xa0\x1f\x00'
    _MSGCLOSEGROUP._serialized_start = 131
    _MSGCLOSEGROUP._serialized_end = 230
    _MSGCLOSEGROUPRESPONSE._serialized_start = 232
    _MSGCLOSEGROUPRESPONSE._serialized_end = 255
    _MSGPAUSEGROUP._serialized_start = 257
    _MSGPAUSEGROUP._serialized_end = 356
    _MSGPAUSEGROUPRESPONSE._serialized_start = 358
    _MSGPAUSEGROUPRESPONSE._serialized_end = 381
    _MSGSTARTGROUP._serialized_start = 383
    _MSGSTARTGROUP._serialized_end = 482
    _MSGSTARTGROUPRESPONSE._serialized_start = 484
    _MSGSTARTGROUPRESPONSE._serialized_end = 507
