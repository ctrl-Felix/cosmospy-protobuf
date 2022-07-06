
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.deployment.v1beta2 import groupid_pb2 as akash_dot_deployment_dot_v1beta2_dot_groupid__pb2
from ....akash.deployment.v1beta2 import groupspec_pb2 as akash_dot_deployment_dot_v1beta2_dot_groupspec__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$akash/deployment/v1beta2/group.proto\x12\x18akash.deployment.v1beta2\x1a\x14gogoproto/gogo.proto\x1a&akash/deployment/v1beta2/groupid.proto\x1a(akash/deployment/v1beta2/groupspec.proto"\xdc\x03\n\x05Group\x12W\n\x08group_id\x18\x01 \x01(\x0b2!.akash.deployment.v1beta2.GroupIDB"\xe2\xde\x1f\x07GroupID\xc8\xde\x1f\x00\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"\x12O\n\x05state\x18\x02 \x01(\x0e2%.akash.deployment.v1beta2.Group.StateB\x19\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state"\x12T\n\ngroup_spec\x18\x03 \x01(\x0b2#.akash.deployment.v1beta2.GroupSpecB\x1b\xc8\xde\x1f\x00\xea\xde\x1f\x04spec\xf2\xde\x1f\x0byaml:"spec"\x12\x12\n\ncreated_at\x18\x04 \x01(\x03"\xb8\x01\n\x05State\x12"\n\x07invalid\x10\x00\x1a\x15\x8a\x9d \x11GroupStateInvalid\x12\x17\n\x04open\x10\x01\x1a\r\x8a\x9d \tGroupOpen\x12\x1b\n\x06paused\x10\x02\x1a\x0f\x8a\x9d \x0bGroupPaused\x122\n\x12insufficient_funds\x10\x03\x1a\x1a\x8a\x9d \x16GroupInsufficientFunds\x12\x1b\n\x06closed\x10\x04\x1a\x0f\x8a\x9d \x0bGroupClosed\x1a\x04\x88\xa3\x1e\x00:\x04\xe8\xa0\x1f\x00B4Z2github.com/ovrclk/akash/x/deployment/types/v1beta2b\x06proto3')
_GROUP = DESCRIPTOR.message_types_by_name['Group']
_GROUP_STATE = _GROUP.enum_types_by_name['State']
Group = _reflection.GeneratedProtocolMessageType('Group', (_message.Message,), {'DESCRIPTOR': _GROUP, '__module__': 'akash.deployment.v1beta2.group_pb2'})
_sym_db.RegisterMessage(Group)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2github.com/ovrclk/akash/x/deployment/types/v1beta2'
    _GROUP_STATE._options = None
    _GROUP_STATE._serialized_options = b'\x88\xa3\x1e\x00'
    _GROUP_STATE.values_by_name['invalid']._options = None
    _GROUP_STATE.values_by_name['invalid']._serialized_options = b'\x8a\x9d \x11GroupStateInvalid'
    _GROUP_STATE.values_by_name['open']._options = None
    _GROUP_STATE.values_by_name['open']._serialized_options = b'\x8a\x9d \tGroupOpen'
    _GROUP_STATE.values_by_name['paused']._options = None
    _GROUP_STATE.values_by_name['paused']._serialized_options = b'\x8a\x9d \x0bGroupPaused'
    _GROUP_STATE.values_by_name['insufficient_funds']._options = None
    _GROUP_STATE.values_by_name['insufficient_funds']._serialized_options = b'\x8a\x9d \x16GroupInsufficientFunds'
    _GROUP_STATE.values_by_name['closed']._options = None
    _GROUP_STATE.values_by_name['closed']._serialized_options = b'\x8a\x9d \x0bGroupClosed'
    _GROUP.fields_by_name['group_id']._options = None
    _GROUP.fields_by_name['group_id']._serialized_options = b'\xe2\xde\x1f\x07GroupID\xc8\xde\x1f\x00\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"'
    _GROUP.fields_by_name['state']._options = None
    _GROUP.fields_by_name['state']._serialized_options = b'\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state"'
    _GROUP.fields_by_name['group_spec']._options = None
    _GROUP.fields_by_name['group_spec']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x04spec\xf2\xde\x1f\x0byaml:"spec"'
    _GROUP._options = None
    _GROUP._serialized_options = b'\xe8\xa0\x1f\x00'
    _GROUP._serialized_start = 171
    _GROUP._serialized_end = 647
    _GROUP_STATE._serialized_start = 457
    _GROUP_STATE._serialized_end = 641
