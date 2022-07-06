
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ecosmos/auth/v1beta1/auth.proto\x12\x13cosmos.auth.v1beta1\x1a\x19cosmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto"\xbd\x01\n\x0bBaseAccount\x12)\n\x07address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12?\n\x07pub_key\x18\x02 \x01(\x0b2\x14.google.protobuf.AnyB\x18\xea\xde\x1f\x14public_key,omitempty\x12\x16\n\x0eaccount_number\x18\x03 \x01(\x04\x12\x10\n\x08sequence\x18\x04 \x01(\x04:\x18\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x08AccountI"\x8c\x01\n\rModuleAccount\x12<\n\x0cbase_account\x18\x01 \x01(\x0b2 .cosmos.auth.v1beta1.BaseAccountB\x04\xd0\xde\x1f\x01\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0bpermissions\x18\x03 \x03(\t:\x1a\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xca\xb4-\x0eModuleAccountI"\xde\x01\n\x06Params\x12\x1b\n\x13max_memo_characters\x18\x01 \x01(\x04\x12\x14\n\x0ctx_sig_limit\x18\x02 \x01(\x04\x12\x1d\n\x15tx_size_cost_per_byte\x18\x03 \x01(\x04\x129\n\x17sig_verify_cost_ed25519\x18\x04 \x01(\x04B\x18\xe2\xde\x1f\x14SigVerifyCostED25519\x12=\n\x19sig_verify_cost_secp256k1\x18\x05 \x01(\x04B\x1a\xe2\xde\x1f\x16SigVerifyCostSecp256k1:\x08\xe8\xa0\x1f\x01\x98\xa0\x1f\x00B+Z)github.com/cosmos/cosmos-sdk/x/auth/typesb\x06proto3')
_BASEACCOUNT = DESCRIPTOR.message_types_by_name['BaseAccount']
_MODULEACCOUNT = DESCRIPTOR.message_types_by_name['ModuleAccount']
_PARAMS = DESCRIPTOR.message_types_by_name['Params']
BaseAccount = _reflection.GeneratedProtocolMessageType('BaseAccount', (_message.Message,), {'DESCRIPTOR': _BASEACCOUNT, '__module__': 'cosmos.auth.v1beta1.auth_pb2'})
_sym_db.RegisterMessage(BaseAccount)
ModuleAccount = _reflection.GeneratedProtocolMessageType('ModuleAccount', (_message.Message,), {'DESCRIPTOR': _MODULEACCOUNT, '__module__': 'cosmos.auth.v1beta1.auth_pb2'})
_sym_db.RegisterMessage(ModuleAccount)
Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {'DESCRIPTOR': _PARAMS, '__module__': 'cosmos.auth.v1beta1.auth_pb2'})
_sym_db.RegisterMessage(Params)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/auth/types'
    _BASEACCOUNT.fields_by_name['address']._options = None
    _BASEACCOUNT.fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _BASEACCOUNT.fields_by_name['pub_key']._options = None
    _BASEACCOUNT.fields_by_name['pub_key']._serialized_options = b'\xea\xde\x1f\x14public_key,omitempty'
    _BASEACCOUNT._options = None
    _BASEACCOUNT._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x08AccountI'
    _MODULEACCOUNT.fields_by_name['base_account']._options = None
    _MODULEACCOUNT.fields_by_name['base_account']._serialized_options = b'\xd0\xde\x1f\x01'
    _MODULEACCOUNT._options = None
    _MODULEACCOUNT._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xca\xb4-\x0eModuleAccountI'
    _PARAMS.fields_by_name['sig_verify_cost_ed25519']._options = None
    _PARAMS.fields_by_name['sig_verify_cost_ed25519']._serialized_options = b'\xe2\xde\x1f\x14SigVerifyCostED25519'
    _PARAMS.fields_by_name['sig_verify_cost_secp256k1']._options = None
    _PARAMS.fields_by_name['sig_verify_cost_secp256k1']._serialized_options = b'\xe2\xde\x1f\x16SigVerifyCostSecp256k1'
    _PARAMS._options = None
    _PARAMS._serialized_options = b'\xe8\xa0\x1f\x01\x98\xa0\x1f\x00'
    _BASEACCOUNT._serialized_start = 132
    _BASEACCOUNT._serialized_end = 321
    _MODULEACCOUNT._serialized_start = 324
    _MODULEACCOUNT._serialized_end = 464
    _PARAMS._serialized_start = 467
    _PARAMS._serialized_end = 689
