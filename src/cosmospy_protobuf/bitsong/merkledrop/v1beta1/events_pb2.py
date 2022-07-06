
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'bitsong/merkledrop/v1beta1/events.proto\x12\x1abitsong.merkledrop.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"3\n\x0bEventCreate\x12\r\n\x05owner\x18\x01 \x01(\t\x12\x15\n\rmerkledrop_id\x18\x02 \x01(\x04"\x8c\x01\n\nEventClaim\x12\x15\n\rmerkledrop_id\x18\x01 \x01(\x04\x12\r\n\x05index\x18\x02 \x01(\x04\x12X\n\x04coin\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Coin\xc8\xde\x1f\x00"\x80\x01\n\rEventWithdraw\x12\x15\n\rmerkledrop_id\x18\x01 \x01(\x04\x12X\n\x04coin\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Coin\xc8\xde\x1f\x00B>Z8github.com/bitsongofficial/go-bitsong/x/merkledrop/types\xc8\xe1\x1e\x00b\x06proto3')
_EVENTCREATE = DESCRIPTOR.message_types_by_name['EventCreate']
_EVENTCLAIM = DESCRIPTOR.message_types_by_name['EventClaim']
_EVENTWITHDRAW = DESCRIPTOR.message_types_by_name['EventWithdraw']
EventCreate = _reflection.GeneratedProtocolMessageType('EventCreate', (_message.Message,), {'DESCRIPTOR': _EVENTCREATE, '__module__': 'bitsong.merkledrop.v1beta1.events_pb2'})
_sym_db.RegisterMessage(EventCreate)
EventClaim = _reflection.GeneratedProtocolMessageType('EventClaim', (_message.Message,), {'DESCRIPTOR': _EVENTCLAIM, '__module__': 'bitsong.merkledrop.v1beta1.events_pb2'})
_sym_db.RegisterMessage(EventClaim)
EventWithdraw = _reflection.GeneratedProtocolMessageType('EventWithdraw', (_message.Message,), {'DESCRIPTOR': _EVENTWITHDRAW, '__module__': 'bitsong.merkledrop.v1beta1.events_pb2'})
_sym_db.RegisterMessage(EventWithdraw)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z8github.com/bitsongofficial/go-bitsong/x/merkledrop/types\xc8\xe1\x1e\x00'
    _EVENTCLAIM.fields_by_name['coin']._options = None
    _EVENTCLAIM.fields_by_name['coin']._serialized_options = b"\xda\xde\x1f'github.com/cosmos/cosmos-sdk/types.Coin\xc8\xde\x1f\x00"
    _EVENTWITHDRAW.fields_by_name['coin']._options = None
    _EVENTWITHDRAW.fields_by_name['coin']._serialized_options = b"\xda\xde\x1f'github.com/cosmos/cosmos-sdk/types.Coin\xc8\xde\x1f\x00"
    _EVENTCREATE._serialized_start = 125
    _EVENTCREATE._serialized_end = 176
    _EVENTCLAIM._serialized_start = 179
    _EVENTCLAIM._serialized_end = 319
    _EVENTWITHDRAW._serialized_start = 322
    _EVENTWITHDRAW._serialized_end = 450
