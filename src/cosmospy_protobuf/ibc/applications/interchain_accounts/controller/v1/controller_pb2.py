
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCibc/applications/interchain_accounts/controller/v1/controller.proto\x122ibc.applications.interchain_accounts.controller.v1\x1a\x14gogoproto/gogo.proto"C\n\x06Params\x129\n\x12controller_enabled\x18\x01 \x01(\x08B\x1d\xf2\xde\x1f\x19yaml:"controller_enabled"BRZPgithub.com/cosmos/ibc-go/v3/modules/apps/27-interchain-accounts/controller/typesb\x06proto3')
_PARAMS = DESCRIPTOR.message_types_by_name['Params']
Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {'DESCRIPTOR': _PARAMS, '__module__': 'ibc.applications.interchain_accounts.controller.v1.controller_pb2'})
_sym_db.RegisterMessage(Params)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZPgithub.com/cosmos/ibc-go/v3/modules/apps/27-interchain-accounts/controller/types'
    _PARAMS.fields_by_name['controller_enabled']._options = None
    _PARAMS.fields_by_name['controller_enabled']._serialized_options = b'\xf2\xde\x1f\x19yaml:"controller_enabled"'
    _PARAMS._serialized_start = 145
    _PARAMS._serialized_end = 212
