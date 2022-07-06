
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....umee.leverage.v1beta1 import leverage_pb2 as umee_dot_leverage_dot_v1beta1_dot_leverage__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#umee/leverage/v1beta1/genesis.proto\x12!umeenetwork.umee.leverage.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a$umee/leverage/v1beta1/leverage.proto"\xfd\x05\n\x0cGenesisState\x12?\n\x06params\x18\x01 \x01(\x0b2).umeenetwork.umee.leverage.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12@\n\x08registry\x18\x02 \x03(\x0b2(.umeenetwork.umee.leverage.v1beta1.TokenB\x04\xc8\xde\x1f\x00\x12Q\n\x10adjusted_borrows\x18\x03 \x03(\x0b21.umeenetwork.umee.leverage.v1beta1.AdjustedBorrowB\x04\xc8\xde\x1f\x00\x12W\n\x13collateral_settings\x18\x04 \x03(\x0b24.umeenetwork.umee.leverage.v1beta1.CollateralSettingB\x04\xc8\xde\x1f\x00\x12G\n\ncollateral\x18\x05 \x03(\x0b2-.umeenetwork.umee.leverage.v1beta1.CollateralB\x04\xc8\xde\x1f\x00\x12]\n\x08reserves\x18\x06 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12\x1a\n\x12last_interest_time\x18\x07 \x01(\x03\x12C\n\tbad_debts\x18\x08 \x03(\x0b2*.umeenetwork.umee.leverage.v1beta1.BadDebtB\x04\xc8\xde\x1f\x00\x12Q\n\x10interest_scalars\x18\t \x03(\x0b21.umeenetwork.umee.leverage.v1beta1.InterestScalarB\x04\xc8\xde\x1f\x00\x12b\n\rutoken_supply\x18\n \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"U\n\x0eAdjustedBorrow\x12\x0f\n\x07address\x18\x01 \x01(\t\x122\n\x06amount\x18\x02 \x01(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB\x04\xc8\xde\x1f\x00"3\n\x11CollateralSetting\x12\x0f\n\x07address\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t"N\n\nCollateral\x12\x0f\n\x07address\x18\x01 \x01(\t\x12/\n\x06amount\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00")\n\x07BadDebt\x12\x0f\n\x07address\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t"_\n\x0eInterestScalar\x12\r\n\x05denom\x18\x01 \x01(\t\x12>\n\x06scalar\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00B2Z0github.com/umee-network/umee/v2/x/leverage/typesb\x06proto3')
_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
_ADJUSTEDBORROW = DESCRIPTOR.message_types_by_name['AdjustedBorrow']
_COLLATERALSETTING = DESCRIPTOR.message_types_by_name['CollateralSetting']
_COLLATERAL = DESCRIPTOR.message_types_by_name['Collateral']
_BADDEBT = DESCRIPTOR.message_types_by_name['BadDebt']
_INTERESTSCALAR = DESCRIPTOR.message_types_by_name['InterestScalar']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {'DESCRIPTOR': _GENESISSTATE, '__module__': 'umee.leverage.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(GenesisState)
AdjustedBorrow = _reflection.GeneratedProtocolMessageType('AdjustedBorrow', (_message.Message,), {'DESCRIPTOR': _ADJUSTEDBORROW, '__module__': 'umee.leverage.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(AdjustedBorrow)
CollateralSetting = _reflection.GeneratedProtocolMessageType('CollateralSetting', (_message.Message,), {'DESCRIPTOR': _COLLATERALSETTING, '__module__': 'umee.leverage.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(CollateralSetting)
Collateral = _reflection.GeneratedProtocolMessageType('Collateral', (_message.Message,), {'DESCRIPTOR': _COLLATERAL, '__module__': 'umee.leverage.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(Collateral)
BadDebt = _reflection.GeneratedProtocolMessageType('BadDebt', (_message.Message,), {'DESCRIPTOR': _BADDEBT, '__module__': 'umee.leverage.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(BadDebt)
InterestScalar = _reflection.GeneratedProtocolMessageType('InterestScalar', (_message.Message,), {'DESCRIPTOR': _INTERESTSCALAR, '__module__': 'umee.leverage.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(InterestScalar)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z0github.com/umee-network/umee/v2/x/leverage/types'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['registry']._options = None
    _GENESISSTATE.fields_by_name['registry']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['adjusted_borrows']._options = None
    _GENESISSTATE.fields_by_name['adjusted_borrows']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['collateral_settings']._options = None
    _GENESISSTATE.fields_by_name['collateral_settings']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['collateral']._options = None
    _GENESISSTATE.fields_by_name['collateral']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['reserves']._options = None
    _GENESISSTATE.fields_by_name['reserves']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _GENESISSTATE.fields_by_name['bad_debts']._options = None
    _GENESISSTATE.fields_by_name['bad_debts']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['interest_scalars']._options = None
    _GENESISSTATE.fields_by_name['interest_scalars']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['utoken_supply']._options = None
    _GENESISSTATE.fields_by_name['utoken_supply']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _ADJUSTEDBORROW.fields_by_name['amount']._options = None
    _ADJUSTEDBORROW.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00'
    _COLLATERAL.fields_by_name['amount']._options = None
    _COLLATERAL.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00'
    _INTERESTSCALAR.fields_by_name['scalar']._options = None
    _INTERESTSCALAR.fields_by_name['scalar']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _GENESISSTATE._serialized_start = 167
    _GENESISSTATE._serialized_end = 932
    _ADJUSTEDBORROW._serialized_start = 934
    _ADJUSTEDBORROW._serialized_end = 1019
    _COLLATERALSETTING._serialized_start = 1021
    _COLLATERALSETTING._serialized_end = 1072
    _COLLATERAL._serialized_start = 1074
    _COLLATERAL._serialized_end = 1152
    _BADDEBT._serialized_start = 1154
    _BADDEBT._serialized_end = 1195
    _INTERESTSCALAR._serialized_start = 1197
    _INTERESTSCALAR._serialized_end = 1292
