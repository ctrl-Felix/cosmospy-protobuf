
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+bitsong/merkledrop/v1beta1/merkledrop.proto\x12\x1abitsong.merkledrop.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\x98\x02\n\nMerkledrop\x12\n\n\x02id\x18\x01 \x01(\x04\x12+\n\x0bmerkle_root\x18\x02 \x01(\tB\x16\xf2\xde\x1f\x12yaml:"merkle_root"\x12\x14\n\x0cstart_height\x18\x03 \x01(\x03\x12\x12\n\nend_height\x18\x04 \x01(\x03\x12\r\n\x05denom\x18\x05 \x01(\t\x12>\n\x06amount\x18\x06 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12?\n\x07claimed\x18\x07 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12\r\n\x05owner\x18\x08 \x01(\t:\x08\x98\xa0\x1f\x00\x88\xa0\x1f\x00B>Z8github.com/bitsongofficial/go-bitsong/x/merkledrop/types\xc8\xe1\x1e\x00b\x06proto3')
_MERKLEDROP = DESCRIPTOR.message_types_by_name['Merkledrop']
Merkledrop = _reflection.GeneratedProtocolMessageType('Merkledrop', (_message.Message,), {'DESCRIPTOR': _MERKLEDROP, '__module__': 'bitsong.merkledrop.v1beta1.merkledrop_pb2'})
_sym_db.RegisterMessage(Merkledrop)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z8github.com/bitsongofficial/go-bitsong/x/merkledrop/types\xc8\xe1\x1e\x00'
    _MERKLEDROP.fields_by_name['merkle_root']._options = None
    _MERKLEDROP.fields_by_name['merkle_root']._serialized_options = b'\xf2\xde\x1f\x12yaml:"merkle_root"'
    _MERKLEDROP.fields_by_name['amount']._options = None
    _MERKLEDROP.fields_by_name['amount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _MERKLEDROP.fields_by_name['claimed']._options = None
    _MERKLEDROP.fields_by_name['claimed']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _MERKLEDROP._options = None
    _MERKLEDROP._serialized_options = b'\x98\xa0\x1f\x00\x88\xa0\x1f\x00'
    _MERKLEDROP._serialized_start = 163
    _MERKLEDROP._serialized_end = 443
