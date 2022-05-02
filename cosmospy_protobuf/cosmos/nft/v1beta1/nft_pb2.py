
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ccosmos/nft/v1beta1/nft.proto\x12\x12cosmos.nft.v1beta1\x1a\x19google/protobuf/any.proto"\x89\x01\n\x05Class\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06symbol\x18\x03 \x01(\t\x12\x13\n\x0bdescription\x18\x04 \x01(\t\x12\x0b\n\x03uri\x18\x05 \x01(\t\x12\x10\n\x08uri_hash\x18\x06 \x01(\t\x12"\n\x04data\x18\x07 \x01(\x0b2\x14.google.protobuf.Any"f\n\x03NFT\x12\x10\n\x08class_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0b\n\x03uri\x18\x03 \x01(\t\x12\x10\n\x08uri_hash\x18\x04 \x01(\t\x12"\n\x04data\x18\n \x01(\x0b2\x14.google.protobuf.AnyB$Z"github.com/cosmos/cosmos-sdk/x/nftb\x06proto3')
_CLASS = DESCRIPTOR.message_types_by_name['Class']
_NFT = DESCRIPTOR.message_types_by_name['NFT']
Class = _reflection.GeneratedProtocolMessageType('Class', (_message.Message,), {'DESCRIPTOR': _CLASS, '__module__': 'cosmos.nft.v1beta1.nft_pb2'})
_sym_db.RegisterMessage(Class)
NFT = _reflection.GeneratedProtocolMessageType('NFT', (_message.Message,), {'DESCRIPTOR': _NFT, '__module__': 'cosmos.nft.v1beta1.nft_pb2'})
_sym_db.RegisterMessage(NFT)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z"github.com/cosmos/cosmos-sdk/x/nft'
    _CLASS._serialized_start = 80
    _CLASS._serialized_end = 217
    _NFT._serialized_start = 219
    _NFT._serialized_end = 321
