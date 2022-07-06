
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.staking.v1beta1 import staking_pb2 as cosmos_dot_staking_dot_v1beta1_dot_staking__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$cosmos/staking/v1beta1/genesis.proto\x12\x16cosmos.staking.v1beta1\x1a\x14gogoproto/gogo.proto\x1a$cosmos/staking/v1beta1/staking.proto\x1a\x19cosmos_proto/cosmos.proto"\x82\x04\n\x0cGenesisState\x124\n\x06params\x18\x01 \x01(\x0b2\x1e.cosmos.staking.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12H\n\x10last_total_power\x18\x02 \x01(\x0cB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12O\n\x15last_validator_powers\x18\x03 \x03(\x0b2*.cosmos.staking.v1beta1.LastValidatorPowerB\x04\xc8\xde\x1f\x00\x12;\n\nvalidators\x18\x04 \x03(\x0b2!.cosmos.staking.v1beta1.ValidatorB\x04\xc8\xde\x1f\x00\x12=\n\x0bdelegations\x18\x05 \x03(\x0b2".cosmos.staking.v1beta1.DelegationB\x04\xc8\xde\x1f\x00\x12P\n\x15unbonding_delegations\x18\x06 \x03(\x0b2+.cosmos.staking.v1beta1.UnbondingDelegationB\x04\xc8\xde\x1f\x00\x12A\n\rredelegations\x18\x07 \x03(\x0b2$.cosmos.staking.v1beta1.RedelegationB\x04\xc8\xde\x1f\x00\x12\x10\n\x08exported\x18\x08 \x01(\x08"X\n\x12LastValidatorPower\x12)\n\x07address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12\r\n\x05power\x18\x02 \x01(\x03:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00B.Z,github.com/cosmos/cosmos-sdk/x/staking/typesb\x06proto3')
_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
_LASTVALIDATORPOWER = DESCRIPTOR.message_types_by_name['LastValidatorPower']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {'DESCRIPTOR': _GENESISSTATE, '__module__': 'cosmos.staking.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(GenesisState)
LastValidatorPower = _reflection.GeneratedProtocolMessageType('LastValidatorPower', (_message.Message,), {'DESCRIPTOR': _LASTVALIDATORPOWER, '__module__': 'cosmos.staking.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(LastValidatorPower)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z,github.com/cosmos/cosmos-sdk/x/staking/types'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['last_total_power']._options = None
    _GENESISSTATE.fields_by_name['last_total_power']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['last_validator_powers']._options = None
    _GENESISSTATE.fields_by_name['last_validator_powers']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['validators']._options = None
    _GENESISSTATE.fields_by_name['validators']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['delegations']._options = None
    _GENESISSTATE.fields_by_name['delegations']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['unbonding_delegations']._options = None
    _GENESISSTATE.fields_by_name['unbonding_delegations']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['redelegations']._options = None
    _GENESISSTATE.fields_by_name['redelegations']._serialized_options = b'\xc8\xde\x1f\x00'
    _LASTVALIDATORPOWER.fields_by_name['address']._options = None
    _LASTVALIDATORPOWER.fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _LASTVALIDATORPOWER._options = None
    _LASTVALIDATORPOWER._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _GENESISSTATE._serialized_start = 152
    _GENESISSTATE._serialized_end = 666
    _LASTVALIDATORPOWER._serialized_start = 668
    _LASTVALIDATORPOWER._serialized_end = 756
