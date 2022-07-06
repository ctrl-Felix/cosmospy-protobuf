
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n tendermint/libs/bits/types.proto\x12\x14tendermint.libs.bits"\'\n\x08BitArray\x12\x0c\n\x04bits\x18\x01 \x01(\x03\x12\r\n\x05elems\x18\x02 \x03(\x04B=Z;github.com/tendermint/tendermint/proto/tendermint/libs/bitsb\x06proto3')
_BITARRAY = DESCRIPTOR.message_types_by_name['BitArray']
BitArray = _reflection.GeneratedProtocolMessageType('BitArray', (_message.Message,), {'DESCRIPTOR': _BITARRAY, '__module__': 'tendermint.libs.bits.types_pb2'})
_sym_db.RegisterMessage(BitArray)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z;github.com/tendermint/tendermint/proto/tendermint/libs/bits'
    _BITARRAY._serialized_start = 58
    _BITARRAY._serialized_end = 97
