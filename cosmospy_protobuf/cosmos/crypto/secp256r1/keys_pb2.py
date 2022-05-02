
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"cosmos/crypto/secp256r1/keys.proto\x12\x17cosmos.crypto.secp256r1\x1a\x14gogoproto/gogo.proto""\n\x06PubKey\x12\x18\n\x03key\x18\x01 \x01(\x0cB\x0b\xda\xde\x1f\x07ecdsaPK"&\n\x07PrivKey\x12\x1b\n\x06secret\x18\x01 \x01(\x0cB\x0b\xda\xde\x1f\x07ecdsaSKB@Z2github.com/cosmos/cosmos-sdk/crypto/keys/secp256r1\xc8\xe3\x1e\x01\xd8\xe1\x1e\x00\xc8\xe1\x1e\x00b\x06proto3')
_PUBKEY = DESCRIPTOR.message_types_by_name['PubKey']
_PRIVKEY = DESCRIPTOR.message_types_by_name['PrivKey']
PubKey = _reflection.GeneratedProtocolMessageType('PubKey', (_message.Message,), {'DESCRIPTOR': _PUBKEY, '__module__': 'cosmos.crypto.secp256r1.keys_pb2'})
_sym_db.RegisterMessage(PubKey)
PrivKey = _reflection.GeneratedProtocolMessageType('PrivKey', (_message.Message,), {'DESCRIPTOR': _PRIVKEY, '__module__': 'cosmos.crypto.secp256r1.keys_pb2'})
_sym_db.RegisterMessage(PrivKey)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2github.com/cosmos/cosmos-sdk/crypto/keys/secp256r1\xc8\xe3\x1e\x01\xd8\xe1\x1e\x00\xc8\xe1\x1e\x00'
    _PUBKEY.fields_by_name['key']._options = None
    _PUBKEY.fields_by_name['key']._serialized_options = b'\xda\xde\x1f\x07ecdsaPK'
    _PRIVKEY.fields_by_name['secret']._options = None
    _PRIVKEY.fields_by_name['secret']._serialized_options = b'\xda\xde\x1f\x07ecdsaSK'
    _PUBKEY._serialized_start = 85
    _PUBKEY._serialized_end = 119
    _PRIVKEY._serialized_start = 121
    _PRIVKEY._serialized_end = 159
