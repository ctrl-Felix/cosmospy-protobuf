
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$cosmos/upgrade/v1beta1/upgrade.proto\x12\x16cosmos.upgrade.v1beta1\x1a\x19google/protobuf/any.proto\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xab\x01\n\x04Plan\x12\x0c\n\x04name\x18\x01 \x01(\t\x124\n\x04time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\n\x18\x01\x90\xdf\x1f\x01\xc8\xde\x1f\x00\x12\x0e\n\x06height\x18\x03 \x01(\x03\x12\x0c\n\x04info\x18\x04 \x01(\t\x127\n\x15upgraded_client_state\x18\x05 \x01(\x0b2\x14.google.protobuf.AnyB\x02\x18\x01:\x08\xe8\xa0\x1f\x01\x98\xa0\x1f\x00"{\n\x17SoftwareUpgradeProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x120\n\x04plan\x18\x03 \x01(\x0b2\x1c.cosmos.upgrade.v1beta1.PlanB\x04\xc8\xde\x1f\x00:\n\x18\x01\xe8\xa0\x1f\x01\x98\xa0\x1f\x00"O\n\x1dCancelSoftwareUpgradeProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t:\n\x18\x01\xe8\xa0\x1f\x01\x98\xa0\x1f\x00"8\n\rModuleVersion\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x04:\x08\xe8\xa0\x1f\x01\x98\xa0\x1f\x01B2Z,github.com/cosmos/cosmos-sdk/x/upgrade/types\xc8\xe1\x1e\x00b\x06proto3')
_PLAN = DESCRIPTOR.message_types_by_name['Plan']
_SOFTWAREUPGRADEPROPOSAL = DESCRIPTOR.message_types_by_name['SoftwareUpgradeProposal']
_CANCELSOFTWAREUPGRADEPROPOSAL = DESCRIPTOR.message_types_by_name['CancelSoftwareUpgradeProposal']
_MODULEVERSION = DESCRIPTOR.message_types_by_name['ModuleVersion']
Plan = _reflection.GeneratedProtocolMessageType('Plan', (_message.Message,), {'DESCRIPTOR': _PLAN, '__module__': 'cosmos.upgrade.v1beta1.upgrade_pb2'})
_sym_db.RegisterMessage(Plan)
SoftwareUpgradeProposal = _reflection.GeneratedProtocolMessageType('SoftwareUpgradeProposal', (_message.Message,), {'DESCRIPTOR': _SOFTWAREUPGRADEPROPOSAL, '__module__': 'cosmos.upgrade.v1beta1.upgrade_pb2'})
_sym_db.RegisterMessage(SoftwareUpgradeProposal)
CancelSoftwareUpgradeProposal = _reflection.GeneratedProtocolMessageType('CancelSoftwareUpgradeProposal', (_message.Message,), {'DESCRIPTOR': _CANCELSOFTWAREUPGRADEPROPOSAL, '__module__': 'cosmos.upgrade.v1beta1.upgrade_pb2'})
_sym_db.RegisterMessage(CancelSoftwareUpgradeProposal)
ModuleVersion = _reflection.GeneratedProtocolMessageType('ModuleVersion', (_message.Message,), {'DESCRIPTOR': _MODULEVERSION, '__module__': 'cosmos.upgrade.v1beta1.upgrade_pb2'})
_sym_db.RegisterMessage(ModuleVersion)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z,github.com/cosmos/cosmos-sdk/x/upgrade/types\xc8\xe1\x1e\x00'
    _PLAN.fields_by_name['time']._options = None
    _PLAN.fields_by_name['time']._serialized_options = b'\x18\x01\x90\xdf\x1f\x01\xc8\xde\x1f\x00'
    _PLAN.fields_by_name['upgraded_client_state']._options = None
    _PLAN.fields_by_name['upgraded_client_state']._serialized_options = b'\x18\x01'
    _PLAN._options = None
    _PLAN._serialized_options = b'\xe8\xa0\x1f\x01\x98\xa0\x1f\x00'
    _SOFTWAREUPGRADEPROPOSAL.fields_by_name['plan']._options = None
    _SOFTWAREUPGRADEPROPOSAL.fields_by_name['plan']._serialized_options = b'\xc8\xde\x1f\x00'
    _SOFTWAREUPGRADEPROPOSAL._options = None
    _SOFTWAREUPGRADEPROPOSAL._serialized_options = b'\x18\x01\xe8\xa0\x1f\x01\x98\xa0\x1f\x00'
    _CANCELSOFTWAREUPGRADEPROPOSAL._options = None
    _CANCELSOFTWAREUPGRADEPROPOSAL._serialized_options = b'\x18\x01\xe8\xa0\x1f\x01\x98\xa0\x1f\x00'
    _MODULEVERSION._options = None
    _MODULEVERSION._serialized_options = b'\xe8\xa0\x1f\x01\x98\xa0\x1f\x01'
    _PLAN._serialized_start = 147
    _PLAN._serialized_end = 318
    _SOFTWAREUPGRADEPROPOSAL._serialized_start = 320
    _SOFTWAREUPGRADEPROPOSAL._serialized_end = 443
    _CANCELSOFTWAREUPGRADEPROPOSAL._serialized_start = 445
    _CANCELSOFTWAREUPGRADEPROPOSAL._serialized_end = 524
    _MODULEVERSION._serialized_start = 526
    _MODULEVERSION._serialized_end = 582
