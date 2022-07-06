
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%bitsong/fantoken/v1beta1/events.proto\x12\x18bitsong.fantoken.v1beta1\x1a\x14gogoproto/gogo.proto"\x1b\n\nEventIssue\x12\r\n\x05denom\x18\x01 \x01(\t"!\n\x10EventDisableMint\x12\r\n\x05denom\x18\x01 \x01(\t",\n\tEventMint\x12\x11\n\trecipient\x18\x01 \x01(\t\x12\x0c\n\x04coin\x18\x02 \x01(\t")\n\tEventBurn\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x0c\n\x04coin\x18\x02 \x01(\t"\x84\x01\n\x11EventSetAuthority\x12\r\n\x05denom\x18\x01 \x01(\t\x12/\n\rold_authority\x18\x02 \x01(\tB\x18\xf2\xde\x1f\x14yaml:"old_authority"\x12/\n\rnew_authority\x18\x03 \x01(\tB\x18\xf2\xde\x1f\x14yaml:"new_authority""u\n\x0eEventSetMinter\x12\r\n\x05denom\x18\x01 \x01(\t\x12)\n\nold_minter\x18\x02 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"old_minter"\x12)\n\nnew_minter\x18\x03 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"new_minter""\x1c\n\x0bEventSetUri\x12\r\n\x05denom\x18\x01 \x01(\tB8Z6github.com/bitsongofficial/go-bitsong/x/fantoken/typesb\x06proto3')
_EVENTISSUE = DESCRIPTOR.message_types_by_name['EventIssue']
_EVENTDISABLEMINT = DESCRIPTOR.message_types_by_name['EventDisableMint']
_EVENTMINT = DESCRIPTOR.message_types_by_name['EventMint']
_EVENTBURN = DESCRIPTOR.message_types_by_name['EventBurn']
_EVENTSETAUTHORITY = DESCRIPTOR.message_types_by_name['EventSetAuthority']
_EVENTSETMINTER = DESCRIPTOR.message_types_by_name['EventSetMinter']
_EVENTSETURI = DESCRIPTOR.message_types_by_name['EventSetUri']
EventIssue = _reflection.GeneratedProtocolMessageType('EventIssue', (_message.Message,), {'DESCRIPTOR': _EVENTISSUE, '__module__': 'bitsong.fantoken.v1beta1.events_pb2'})
_sym_db.RegisterMessage(EventIssue)
EventDisableMint = _reflection.GeneratedProtocolMessageType('EventDisableMint', (_message.Message,), {'DESCRIPTOR': _EVENTDISABLEMINT, '__module__': 'bitsong.fantoken.v1beta1.events_pb2'})
_sym_db.RegisterMessage(EventDisableMint)
EventMint = _reflection.GeneratedProtocolMessageType('EventMint', (_message.Message,), {'DESCRIPTOR': _EVENTMINT, '__module__': 'bitsong.fantoken.v1beta1.events_pb2'})
_sym_db.RegisterMessage(EventMint)
EventBurn = _reflection.GeneratedProtocolMessageType('EventBurn', (_message.Message,), {'DESCRIPTOR': _EVENTBURN, '__module__': 'bitsong.fantoken.v1beta1.events_pb2'})
_sym_db.RegisterMessage(EventBurn)
EventSetAuthority = _reflection.GeneratedProtocolMessageType('EventSetAuthority', (_message.Message,), {'DESCRIPTOR': _EVENTSETAUTHORITY, '__module__': 'bitsong.fantoken.v1beta1.events_pb2'})
_sym_db.RegisterMessage(EventSetAuthority)
EventSetMinter = _reflection.GeneratedProtocolMessageType('EventSetMinter', (_message.Message,), {'DESCRIPTOR': _EVENTSETMINTER, '__module__': 'bitsong.fantoken.v1beta1.events_pb2'})
_sym_db.RegisterMessage(EventSetMinter)
EventSetUri = _reflection.GeneratedProtocolMessageType('EventSetUri', (_message.Message,), {'DESCRIPTOR': _EVENTSETURI, '__module__': 'bitsong.fantoken.v1beta1.events_pb2'})
_sym_db.RegisterMessage(EventSetUri)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/bitsongofficial/go-bitsong/x/fantoken/types'
    _EVENTSETAUTHORITY.fields_by_name['old_authority']._options = None
    _EVENTSETAUTHORITY.fields_by_name['old_authority']._serialized_options = b'\xf2\xde\x1f\x14yaml:"old_authority"'
    _EVENTSETAUTHORITY.fields_by_name['new_authority']._options = None
    _EVENTSETAUTHORITY.fields_by_name['new_authority']._serialized_options = b'\xf2\xde\x1f\x14yaml:"new_authority"'
    _EVENTSETMINTER.fields_by_name['old_minter']._options = None
    _EVENTSETMINTER.fields_by_name['old_minter']._serialized_options = b'\xf2\xde\x1f\x11yaml:"old_minter"'
    _EVENTSETMINTER.fields_by_name['new_minter']._options = None
    _EVENTSETMINTER.fields_by_name['new_minter']._serialized_options = b'\xf2\xde\x1f\x11yaml:"new_minter"'
    _EVENTISSUE._serialized_start = 89
    _EVENTISSUE._serialized_end = 116
    _EVENTDISABLEMINT._serialized_start = 118
    _EVENTDISABLEMINT._serialized_end = 151
    _EVENTMINT._serialized_start = 153
    _EVENTMINT._serialized_end = 197
    _EVENTBURN._serialized_start = 199
    _EVENTBURN._serialized_end = 240
    _EVENTSETAUTHORITY._serialized_start = 243
    _EVENTSETAUTHORITY._serialized_end = 375
    _EVENTSETMINTER._serialized_start = 377
    _EVENTSETMINTER._serialized_end = 494
    _EVENTSETURI._serialized_start = 496
    _EVENTSETURI._serialized_end = 524
