
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....cosmos.group.v1 import types_pb2 as cosmos_dot_group_dot_v1_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ccosmos/group/v1/events.proto\x12\x0fcosmos.group.v1\x1a\x19cosmos_proto/cosmos.proto\x1a\x1bcosmos/group/v1/types.proto"$\n\x10EventCreateGroup\x12\x10\n\x08group_id\x18\x01 \x01(\x04"$\n\x10EventUpdateGroup\x12\x10\n\x08group_id\x18\x01 \x01(\x04"C\n\x16EventCreateGroupPolicy\x12)\n\x07address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString"C\n\x16EventUpdateGroupPolicy\x12)\n\x07address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString"*\n\x13EventSubmitProposal\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04",\n\x15EventWithdrawProposal\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04" \n\tEventVote\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04"g\n\tEventExec\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x127\n\x06result\x18\x02 \x01(\x0e2\'.cosmos.group.v1.ProposalExecutorResult\x12\x0c\n\x04logs\x18\x03 \x01(\t"N\n\x0fEventLeaveGroup\x12\x10\n\x08group_id\x18\x01 \x01(\x04\x12)\n\x07address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressStringB&Z$github.com/cosmos/cosmos-sdk/x/groupb\x06proto3')
_EVENTCREATEGROUP = DESCRIPTOR.message_types_by_name['EventCreateGroup']
_EVENTUPDATEGROUP = DESCRIPTOR.message_types_by_name['EventUpdateGroup']
_EVENTCREATEGROUPPOLICY = DESCRIPTOR.message_types_by_name['EventCreateGroupPolicy']
_EVENTUPDATEGROUPPOLICY = DESCRIPTOR.message_types_by_name['EventUpdateGroupPolicy']
_EVENTSUBMITPROPOSAL = DESCRIPTOR.message_types_by_name['EventSubmitProposal']
_EVENTWITHDRAWPROPOSAL = DESCRIPTOR.message_types_by_name['EventWithdrawProposal']
_EVENTVOTE = DESCRIPTOR.message_types_by_name['EventVote']
_EVENTEXEC = DESCRIPTOR.message_types_by_name['EventExec']
_EVENTLEAVEGROUP = DESCRIPTOR.message_types_by_name['EventLeaveGroup']
EventCreateGroup = _reflection.GeneratedProtocolMessageType('EventCreateGroup', (_message.Message,), {'DESCRIPTOR': _EVENTCREATEGROUP, '__module__': 'cosmos.group.v1.events_pb2'})
_sym_db.RegisterMessage(EventCreateGroup)
EventUpdateGroup = _reflection.GeneratedProtocolMessageType('EventUpdateGroup', (_message.Message,), {'DESCRIPTOR': _EVENTUPDATEGROUP, '__module__': 'cosmos.group.v1.events_pb2'})
_sym_db.RegisterMessage(EventUpdateGroup)
EventCreateGroupPolicy = _reflection.GeneratedProtocolMessageType('EventCreateGroupPolicy', (_message.Message,), {'DESCRIPTOR': _EVENTCREATEGROUPPOLICY, '__module__': 'cosmos.group.v1.events_pb2'})
_sym_db.RegisterMessage(EventCreateGroupPolicy)
EventUpdateGroupPolicy = _reflection.GeneratedProtocolMessageType('EventUpdateGroupPolicy', (_message.Message,), {'DESCRIPTOR': _EVENTUPDATEGROUPPOLICY, '__module__': 'cosmos.group.v1.events_pb2'})
_sym_db.RegisterMessage(EventUpdateGroupPolicy)
EventSubmitProposal = _reflection.GeneratedProtocolMessageType('EventSubmitProposal', (_message.Message,), {'DESCRIPTOR': _EVENTSUBMITPROPOSAL, '__module__': 'cosmos.group.v1.events_pb2'})
_sym_db.RegisterMessage(EventSubmitProposal)
EventWithdrawProposal = _reflection.GeneratedProtocolMessageType('EventWithdrawProposal', (_message.Message,), {'DESCRIPTOR': _EVENTWITHDRAWPROPOSAL, '__module__': 'cosmos.group.v1.events_pb2'})
_sym_db.RegisterMessage(EventWithdrawProposal)
EventVote = _reflection.GeneratedProtocolMessageType('EventVote', (_message.Message,), {'DESCRIPTOR': _EVENTVOTE, '__module__': 'cosmos.group.v1.events_pb2'})
_sym_db.RegisterMessage(EventVote)
EventExec = _reflection.GeneratedProtocolMessageType('EventExec', (_message.Message,), {'DESCRIPTOR': _EVENTEXEC, '__module__': 'cosmos.group.v1.events_pb2'})
_sym_db.RegisterMessage(EventExec)
EventLeaveGroup = _reflection.GeneratedProtocolMessageType('EventLeaveGroup', (_message.Message,), {'DESCRIPTOR': _EVENTLEAVEGROUP, '__module__': 'cosmos.group.v1.events_pb2'})
_sym_db.RegisterMessage(EventLeaveGroup)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z$github.com/cosmos/cosmos-sdk/x/group'
    _EVENTCREATEGROUPPOLICY.fields_by_name['address']._options = None
    _EVENTCREATEGROUPPOLICY.fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _EVENTUPDATEGROUPPOLICY.fields_by_name['address']._options = None
    _EVENTUPDATEGROUPPOLICY.fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _EVENTLEAVEGROUP.fields_by_name['address']._options = None
    _EVENTLEAVEGROUP.fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _EVENTCREATEGROUP._serialized_start = 105
    _EVENTCREATEGROUP._serialized_end = 141
    _EVENTUPDATEGROUP._serialized_start = 143
    _EVENTUPDATEGROUP._serialized_end = 179
    _EVENTCREATEGROUPPOLICY._serialized_start = 181
    _EVENTCREATEGROUPPOLICY._serialized_end = 248
    _EVENTUPDATEGROUPPOLICY._serialized_start = 250
    _EVENTUPDATEGROUPPOLICY._serialized_end = 317
    _EVENTSUBMITPROPOSAL._serialized_start = 319
    _EVENTSUBMITPROPOSAL._serialized_end = 361
    _EVENTWITHDRAWPROPOSAL._serialized_start = 363
    _EVENTWITHDRAWPROPOSAL._serialized_end = 407
    _EVENTVOTE._serialized_start = 409
    _EVENTVOTE._serialized_end = 441
    _EVENTEXEC._serialized_start = 443
    _EVENTEXEC._serialized_end = 546
    _EVENTLEAVEGROUP._serialized_start = 548
    _EVENTLEAVEGROUP._serialized_end = 626
