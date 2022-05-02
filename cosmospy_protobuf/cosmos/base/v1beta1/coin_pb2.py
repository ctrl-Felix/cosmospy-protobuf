
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ecosmos/base/v1beta1/coin.proto\x12\x13cosmos.base.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19cosmos_proto/cosmos.proto"F\n\x04Coin\x12\r\n\x05denom\x18\x01 \x01(\t\x12)\n\x06amount\x18\x02 \x01(\tB\x19\xd2\xb4-\ncosmos.Int\xda\xde\x1f\x03Int\xc8\xde\x1f\x00:\x04\xe8\xa0\x1f\x01"I\n\x07DecCoin\x12\r\n\x05denom\x18\x01 \x01(\t\x12)\n\x06amount\x18\x02 \x01(\tB\x19\xd2\xb4-\ncosmos.Dec\xda\xde\x1f\x03Dec\xc8\xde\x1f\x00:\x04\xe8\xa0\x1f\x01"2\n\x08IntProto\x12&\n\x03int\x18\x01 \x01(\tB\x19\xd2\xb4-\ncosmos.Int\xda\xde\x1f\x03Int\xc8\xde\x1f\x00"2\n\x08DecProto\x12&\n\x03dec\x18\x01 \x01(\tB\x19\xd2\xb4-\ncosmos.Dec\xda\xde\x1f\x03Dec\xc8\xde\x1f\x00B,Z"github.com/cosmos/cosmos-sdk/types\xd8\xe1\x1e\x00\x80\xe2\x1e\x00b\x06proto3')
_COIN = DESCRIPTOR.message_types_by_name['Coin']
_DECCOIN = DESCRIPTOR.message_types_by_name['DecCoin']
_INTPROTO = DESCRIPTOR.message_types_by_name['IntProto']
_DECPROTO = DESCRIPTOR.message_types_by_name['DecProto']
Coin = _reflection.GeneratedProtocolMessageType('Coin', (_message.Message,), {'DESCRIPTOR': _COIN, '__module__': 'cosmos.base.v1beta1.coin_pb2'})
_sym_db.RegisterMessage(Coin)
DecCoin = _reflection.GeneratedProtocolMessageType('DecCoin', (_message.Message,), {'DESCRIPTOR': _DECCOIN, '__module__': 'cosmos.base.v1beta1.coin_pb2'})
_sym_db.RegisterMessage(DecCoin)
IntProto = _reflection.GeneratedProtocolMessageType('IntProto', (_message.Message,), {'DESCRIPTOR': _INTPROTO, '__module__': 'cosmos.base.v1beta1.coin_pb2'})
_sym_db.RegisterMessage(IntProto)
DecProto = _reflection.GeneratedProtocolMessageType('DecProto', (_message.Message,), {'DESCRIPTOR': _DECPROTO, '__module__': 'cosmos.base.v1beta1.coin_pb2'})
_sym_db.RegisterMessage(DecProto)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z"github.com/cosmos/cosmos-sdk/types\xd8\xe1\x1e\x00\x80\xe2\x1e\x00'
    _COIN.fields_by_name['amount']._options = None
    _COIN.fields_by_name['amount']._serialized_options = b'\xd2\xb4-\ncosmos.Int\xda\xde\x1f\x03Int\xc8\xde\x1f\x00'
    _COIN._options = None
    _COIN._serialized_options = b'\xe8\xa0\x1f\x01'
    _DECCOIN.fields_by_name['amount']._options = None
    _DECCOIN.fields_by_name['amount']._serialized_options = b'\xd2\xb4-\ncosmos.Dec\xda\xde\x1f\x03Dec\xc8\xde\x1f\x00'
    _DECCOIN._options = None
    _DECCOIN._serialized_options = b'\xe8\xa0\x1f\x01'
    _INTPROTO.fields_by_name['int']._options = None
    _INTPROTO.fields_by_name['int']._serialized_options = b'\xd2\xb4-\ncosmos.Int\xda\xde\x1f\x03Int\xc8\xde\x1f\x00'
    _DECPROTO.fields_by_name['dec']._options = None
    _DECPROTO.fields_by_name['dec']._serialized_options = b'\xd2\xb4-\ncosmos.Dec\xda\xde\x1f\x03Dec\xc8\xde\x1f\x00'
    _COIN._serialized_start = 104
    _COIN._serialized_end = 174
    _DECCOIN._serialized_start = 176
    _DECCOIN._serialized_end = 249
    _INTPROTO._serialized_start = 251
    _INTPROTO._serialized_end = 301
    _DECPROTO._serialized_start = 303
    _DECPROTO._serialized_end = 353
