
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-cosmos/crypto/multisig/v1beta1/multisig.proto\x12\x1ecosmos.crypto.multisig.v1beta1\x1a\x14gogoproto/gogo.proto"*\n\x0eMultiSignature\x12\x12\n\nsignatures\x18\x01 \x03(\x0c:\x04\xd0\xa1\x1f\x01"A\n\x0fCompactBitArray\x12\x19\n\x11extra_bits_stored\x18\x01 \x01(\r\x12\r\n\x05elems\x18\x02 \x01(\x0c:\x04\x98\xa0\x1f\x00B+Z)github.com/cosmos/cosmos-sdk/crypto/typesb\x06proto3')
_MULTISIGNATURE = DESCRIPTOR.message_types_by_name['MultiSignature']
_COMPACTBITARRAY = DESCRIPTOR.message_types_by_name['CompactBitArray']
MultiSignature = _reflection.GeneratedProtocolMessageType('MultiSignature', (_message.Message,), {'DESCRIPTOR': _MULTISIGNATURE, '__module__': 'cosmos.crypto.multisig.v1beta1.multisig_pb2'})
_sym_db.RegisterMessage(MultiSignature)
CompactBitArray = _reflection.GeneratedProtocolMessageType('CompactBitArray', (_message.Message,), {'DESCRIPTOR': _COMPACTBITARRAY, '__module__': 'cosmos.crypto.multisig.v1beta1.multisig_pb2'})
_sym_db.RegisterMessage(CompactBitArray)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/crypto/types'
    _MULTISIGNATURE._options = None
    _MULTISIGNATURE._serialized_options = b'\xd0\xa1\x1f\x01'
    _COMPACTBITARRAY._options = None
    _COMPACTBITARRAY._serialized_options = b'\x98\xa0\x1f\x00'
    _MULTISIGNATURE._serialized_start = 103
    _MULTISIGNATURE._serialized_end = 145
    _COMPACTBITARRAY._serialized_start = 147
    _COMPACTBITARRAY._serialized_end = 212
