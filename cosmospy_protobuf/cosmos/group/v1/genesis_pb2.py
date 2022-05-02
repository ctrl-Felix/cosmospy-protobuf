
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....cosmos.group.v1 import types_pb2 as cosmos_dot_group_dot_v1_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dcosmos/group/v1/genesis.proto\x12\x0fcosmos.group.v1\x1a\x1bcosmos/group/v1/types.proto"\xc0\x02\n\x0cGenesisState\x12\x11\n\tgroup_seq\x18\x01 \x01(\x04\x12*\n\x06groups\x18\x02 \x03(\x0b2\x1a.cosmos.group.v1.GroupInfo\x123\n\rgroup_members\x18\x03 \x03(\x0b2\x1c.cosmos.group.v1.GroupMember\x12\x18\n\x10group_policy_seq\x18\x04 \x01(\x04\x128\n\x0egroup_policies\x18\x05 \x03(\x0b2 .cosmos.group.v1.GroupPolicyInfo\x12\x14\n\x0cproposal_seq\x18\x06 \x01(\x04\x12,\n\tproposals\x18\x07 \x03(\x0b2\x19.cosmos.group.v1.Proposal\x12$\n\x05votes\x18\x08 \x03(\x0b2\x15.cosmos.group.v1.VoteB&Z$github.com/cosmos/cosmos-sdk/x/groupb\x06proto3')
_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {'DESCRIPTOR': _GENESISSTATE, '__module__': 'cosmos.group.v1.genesis_pb2'})
_sym_db.RegisterMessage(GenesisState)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z$github.com/cosmos/cosmos-sdk/x/group'
    _GENESISSTATE._serialized_start = 80
    _GENESISSTATE._serialized_end = 400
