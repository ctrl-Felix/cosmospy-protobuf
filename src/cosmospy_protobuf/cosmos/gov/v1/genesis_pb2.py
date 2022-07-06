
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....cosmos.gov.v1 import gov_pb2 as cosmos_dot_gov_dot_v1_dot_gov__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bcosmos/gov/v1/genesis.proto\x12\rcosmos.gov.v1\x1a\x17cosmos/gov/v1/gov.proto"\xc2\x02\n\x0cGenesisState\x12\x1c\n\x14starting_proposal_id\x18\x01 \x01(\x04\x12(\n\x08deposits\x18\x02 \x03(\x0b2\x16.cosmos.gov.v1.Deposit\x12"\n\x05votes\x18\x03 \x03(\x0b2\x13.cosmos.gov.v1.Vote\x12*\n\tproposals\x18\x04 \x03(\x0b2\x17.cosmos.gov.v1.Proposal\x124\n\x0edeposit_params\x18\x05 \x01(\x0b2\x1c.cosmos.gov.v1.DepositParams\x122\n\rvoting_params\x18\x06 \x01(\x0b2\x1b.cosmos.gov.v1.VotingParams\x120\n\x0ctally_params\x18\x07 \x01(\x0b2\x1a.cosmos.gov.v1.TallyParamsB-Z+github.com/cosmos/cosmos-sdk/x/gov/types/v1b\x06proto3')
_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {'DESCRIPTOR': _GENESISSTATE, '__module__': 'cosmos.gov.v1.genesis_pb2'})
_sym_db.RegisterMessage(GenesisState)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z+github.com/cosmos/cosmos-sdk/x/gov/types/v1'
    _GENESISSTATE._serialized_start = 72
    _GENESISSTATE._serialized_end = 394
