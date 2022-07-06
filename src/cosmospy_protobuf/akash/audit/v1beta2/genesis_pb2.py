
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.audit.v1beta2 import audit_pb2 as akash_dot_audit_dot_v1beta2_dot_audit__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!akash/audit/v1beta2/genesis.proto\x12\x13akash.audit.v1beta2\x1a\x14gogoproto/gogo.proto\x1a\x1fakash/audit/v1beta2/audit.proto"s\n\x0cGenesisState\x12c\n\nattributes\x18\x01 \x03(\x0b2&.akash.audit.v1beta2.AuditedAttributesB\'\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes"B/Z-github.com/ovrclk/akash/x/audit/types/v1beta2b\x06proto3')
_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {'DESCRIPTOR': _GENESISSTATE, '__module__': 'akash.audit.v1beta2.genesis_pb2'})
_sym_db.RegisterMessage(GenesisState)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z-github.com/ovrclk/akash/x/audit/types/v1beta2'
    _GENESISSTATE.fields_by_name['attributes']._options = None
    _GENESISSTATE.fields_by_name['attributes']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes"'
    _GENESISSTATE._serialized_start = 113
    _GENESISSTATE._serialized_end = 228
