
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6ibc/applications/interchain_accounts/v1/metadata.proto\x12\'ibc.applications.interchain_accounts.v1\x1a\x14gogoproto/gogo.proto"\xd1\x01\n\x08Metadata\x12\x0f\n\x07version\x18\x01 \x01(\t\x12E\n\x18controller_connection_id\x18\x02 \x01(\tB#\xf2\xde\x1f\x1fyaml:"controller_connection_id"\x129\n\x12host_connection_id\x18\x03 \x01(\tB\x1d\xf2\xde\x1f\x19yaml:"host_connection_id"\x12\x0f\n\x07address\x18\x04 \x01(\t\x12\x10\n\x08encoding\x18\x05 \x01(\t\x12\x0f\n\x07tx_type\x18\x06 \x01(\tBGZEgithub.com/cosmos/ibc-go/v3/modules/apps/27-interchain-accounts/typesb\x06proto3')
_METADATA = DESCRIPTOR.message_types_by_name['Metadata']
Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), {'DESCRIPTOR': _METADATA, '__module__': 'ibc.applications.interchain_accounts.v1.metadata_pb2'})
_sym_db.RegisterMessage(Metadata)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZEgithub.com/cosmos/ibc-go/v3/modules/apps/27-interchain-accounts/types'
    _METADATA.fields_by_name['controller_connection_id']._options = None
    _METADATA.fields_by_name['controller_connection_id']._serialized_options = b'\xf2\xde\x1f\x1fyaml:"controller_connection_id"'
    _METADATA.fields_by_name['host_connection_id']._options = None
    _METADATA.fields_by_name['host_connection_id']._serialized_options = b'\xf2\xde\x1f\x19yaml:"host_connection_id"'
    _METADATA._serialized_start = 122
    _METADATA._serialized_end = 331
