
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ecosmos/nft/v1beta1/event.proto\x12\x12cosmos.nft.v1beta1"K\n\tEventSend\x12\x10\n\x08class_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0e\n\x06sender\x18\x03 \x01(\t\x12\x10\n\x08receiver\x18\x04 \x01(\t"8\n\tEventMint\x12\x10\n\x08class_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x01(\t"8\n\tEventBurn\x12\x10\n\x08class_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x01(\tB$Z"github.com/cosmos/cosmos-sdk/x/nftb\x06proto3')
_EVENTSEND = DESCRIPTOR.message_types_by_name['EventSend']
_EVENTMINT = DESCRIPTOR.message_types_by_name['EventMint']
_EVENTBURN = DESCRIPTOR.message_types_by_name['EventBurn']
EventSend = _reflection.GeneratedProtocolMessageType('EventSend', (_message.Message,), {'DESCRIPTOR': _EVENTSEND, '__module__': 'cosmos.nft.v1beta1.event_pb2'})
_sym_db.RegisterMessage(EventSend)
EventMint = _reflection.GeneratedProtocolMessageType('EventMint', (_message.Message,), {'DESCRIPTOR': _EVENTMINT, '__module__': 'cosmos.nft.v1beta1.event_pb2'})
_sym_db.RegisterMessage(EventMint)
EventBurn = _reflection.GeneratedProtocolMessageType('EventBurn', (_message.Message,), {'DESCRIPTOR': _EVENTBURN, '__module__': 'cosmos.nft.v1beta1.event_pb2'})
_sym_db.RegisterMessage(EventBurn)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z"github.com/cosmos/cosmos-sdk/x/nft'
    _EVENTSEND._serialized_start = 54
    _EVENTSEND._serialized_end = 129
    _EVENTMINT._serialized_start = 131
    _EVENTMINT._serialized_end = 187
    _EVENTBURN._serialized_start = 189
    _EVENTBURN._serialized_end = 245
