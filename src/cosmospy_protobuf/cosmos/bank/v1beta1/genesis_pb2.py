
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!cosmos/bank/v1beta1/genesis.proto\x12\x13cosmos.bank.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x1ecosmos/bank/v1beta1/bank.proto\x1a\x19cosmos_proto/cosmos.proto"\x91\x02\n\x0cGenesisState\x121\n\x06params\x18\x01 \x01(\x0b2\x1b.cosmos.bank.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x124\n\x08balances\x18\x02 \x03(\x0b2\x1c.cosmos.bank.v1beta1.BalanceB\x04\xc8\xde\x1f\x00\x12[\n\x06supply\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xc8\xde\x1f\x00\x12;\n\x0edenom_metadata\x18\x04 \x03(\x0b2\x1d.cosmos.bank.v1beta1.MetadataB\x04\xc8\xde\x1f\x00"\x9a\x01\n\x07Balance\x12)\n\x07address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12Z\n\x05coins\x18\x02 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00B+Z)github.com/cosmos/cosmos-sdk/x/bank/typesb\x06proto3')
_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
_BALANCE = DESCRIPTOR.message_types_by_name['Balance']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {'DESCRIPTOR': _GENESISSTATE, '__module__': 'cosmos.bank.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(GenesisState)
Balance = _reflection.GeneratedProtocolMessageType('Balance', (_message.Message,), {'DESCRIPTOR': _BALANCE, '__module__': 'cosmos.bank.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(Balance)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/bank/types'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['balances']._options = None
    _GENESISSTATE.fields_by_name['balances']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['supply']._options = None
    _GENESISSTATE.fields_by_name['supply']._serialized_options = b'\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['denom_metadata']._options = None
    _GENESISSTATE.fields_by_name['denom_metadata']._serialized_options = b'\xc8\xde\x1f\x00'
    _BALANCE.fields_by_name['address']._options = None
    _BALANCE.fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _BALANCE.fields_by_name['coins']._options = None
    _BALANCE.fields_by_name['coins']._serialized_options = b'\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xc8\xde\x1f\x00'
    _BALANCE._options = None
    _BALANCE._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _GENESISSTATE._serialized_start = 172
    _GENESISSTATE._serialized_end = 445
    _BALANCE._serialized_start = 448
    _BALANCE._serialized_end = 602
