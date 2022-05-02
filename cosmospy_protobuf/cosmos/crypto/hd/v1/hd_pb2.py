
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ccosmos/crypto/hd/v1/hd.proto\x12\x13cosmos.crypto.hd.v1\x1a\x14gogoproto/gogo.proto"o\n\x0bBIP44Params\x12\x0f\n\x07purpose\x18\x01 \x01(\r\x12\x11\n\tcoin_type\x18\x02 \x01(\r\x12\x0f\n\x07account\x18\x03 \x01(\r\x12\x0e\n\x06change\x18\x04 \x01(\x08\x12\x15\n\raddress_index\x18\x05 \x01(\r:\x04\x98\xa0\x1f\x00B,Z&github.com/cosmos/cosmos-sdk/crypto/hd\xc8\xe1\x1e\x00b\x06proto3')
_BIP44PARAMS = DESCRIPTOR.message_types_by_name['BIP44Params']
BIP44Params = _reflection.GeneratedProtocolMessageType('BIP44Params', (_message.Message,), {'DESCRIPTOR': _BIP44PARAMS, '__module__': 'cosmos.crypto.hd.v1.hd_pb2'})
_sym_db.RegisterMessage(BIP44Params)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z&github.com/cosmos/cosmos-sdk/crypto/hd\xc8\xe1\x1e\x00'
    _BIP44PARAMS._options = None
    _BIP44PARAMS._serialized_options = b'\x98\xa0\x1f\x00'
    _BIP44PARAMS._serialized_start = 75
    _BIP44PARAMS._serialized_end = 186
