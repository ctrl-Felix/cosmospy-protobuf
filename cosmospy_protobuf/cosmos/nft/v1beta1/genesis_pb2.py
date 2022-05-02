
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....cosmos.nft.v1beta1 import nft_pb2 as cosmos_dot_nft_dot_v1beta1_dot_nft__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/nft/v1beta1/genesis.proto\x12\x12cosmos.nft.v1beta1\x1a\x1ccosmos/nft/v1beta1/nft.proto"f\n\x0cGenesisState\x12*\n\x07classes\x18\x01 \x03(\x0b2\x19.cosmos.nft.v1beta1.Class\x12*\n\x07entries\x18\x02 \x03(\x0b2\x19.cosmos.nft.v1beta1.Entry"=\n\x05Entry\x12\r\n\x05owner\x18\x01 \x01(\t\x12%\n\x04nfts\x18\x02 \x03(\x0b2\x17.cosmos.nft.v1beta1.NFTB$Z"github.com/cosmos/cosmos-sdk/x/nftb\x06proto3')
_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
_ENTRY = DESCRIPTOR.message_types_by_name['Entry']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {'DESCRIPTOR': _GENESISSTATE, '__module__': 'cosmos.nft.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(GenesisState)
Entry = _reflection.GeneratedProtocolMessageType('Entry', (_message.Message,), {'DESCRIPTOR': _ENTRY, '__module__': 'cosmos.nft.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(Entry)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z"github.com/cosmos/cosmos-sdk/x/nft'
    _GENESISSTATE._serialized_start = 86
    _GENESISSTATE._serialized_end = 188
    _ENTRY._serialized_start = 190
    _ENTRY._serialized_end = 251
