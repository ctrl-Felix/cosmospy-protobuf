
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$umee/leverage/v1beta1/leverage.proto\x12!umeenetwork.umee.leverage.v1beta1\x1a\x14gogoproto/gogo.proto"\xda\x03\n\x06Params\x12\x7f\n\x1ecomplete_liquidation_threshold\x18\x02 \x01(\tBW\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xf2\xde\x1f%yaml:"complete_liquidation_threshold"\x12k\n\x14minimum_close_factor\x18\x03 \x01(\tBM\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xf2\xde\x1f\x1byaml:"minimum_close_factor"\x12k\n\x14oracle_reward_factor\x18\x04 \x01(\tBM\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xf2\xde\x1f\x1byaml:"oracle_reward_factor"\x12o\n\x16small_liquidation_size\x18\x05 \x01(\tBO\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xf2\xde\x1f\x1dyaml:"small_liquidation_size":\x04\x98\xa0\x1f\x00"\xd0\x07\n\x05Token\x12)\n\nbase_denom\x18\x01 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"base_denom"\x12_\n\x0ereserve_factor\x18\x02 \x01(\tBG\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xf2\xde\x1f\x15yaml:"reserve_factor"\x12e\n\x11collateral_weight\x18\x03 \x01(\tBJ\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xf2\xde\x1f\x18yaml:"collateral_weight"\x12m\n\x15liquidation_threshold\x18\x04 \x01(\tBN\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xf2\xde\x1f\x1cyaml:"liquidation_threshold"\x12c\n\x10base_borrow_rate\x18\x05 \x01(\tBI\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xf2\xde\x1f\x17yaml:"base_borrow_rate"\x12c\n\x10kink_borrow_rate\x18\x06 \x01(\tBI\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xf2\xde\x1f\x17yaml:"kink_borrow_rate"\x12a\n\x0fmax_borrow_rate\x18\x07 \x01(\tBH\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:"max_borrow_rate"\x12m\n\x15kink_utilization_rate\x18\x08 \x01(\tBN\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xf2\xde\x1f\x1cyaml:"kink_utilization_rate"\x12m\n\x15liquidation_incentive\x18\t \x01(\tBN\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xf2\xde\x1f\x1cyaml:"liquidation_incentive"\x12-\n\x0csymbol_denom\x18\n \x01(\tB\x17\xf2\xde\x1f\x13yaml:"symbol_denom"\x12%\n\x08exponent\x18\x0b \x01(\rB\x13\xf2\xde\x1f\x0fyaml:"exponent":\x04\xe8\xa0\x1f\x01B2Z0github.com/umee-network/umee/v2/x/leverage/typesb\x06proto3')
_PARAMS = DESCRIPTOR.message_types_by_name['Params']
_TOKEN = DESCRIPTOR.message_types_by_name['Token']
Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {'DESCRIPTOR': _PARAMS, '__module__': 'umee.leverage.v1beta1.leverage_pb2'})
_sym_db.RegisterMessage(Params)
Token = _reflection.GeneratedProtocolMessageType('Token', (_message.Message,), {'DESCRIPTOR': _TOKEN, '__module__': 'umee.leverage.v1beta1.leverage_pb2'})
_sym_db.RegisterMessage(Token)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z0github.com/umee-network/umee/v2/x/leverage/types'
    _PARAMS.fields_by_name['complete_liquidation_threshold']._options = None
    _PARAMS.fields_by_name['complete_liquidation_threshold']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xf2\xde\x1f%yaml:"complete_liquidation_threshold"'
    _PARAMS.fields_by_name['minimum_close_factor']._options = None
    _PARAMS.fields_by_name['minimum_close_factor']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xf2\xde\x1f\x1byaml:"minimum_close_factor"'
    _PARAMS.fields_by_name['oracle_reward_factor']._options = None
    _PARAMS.fields_by_name['oracle_reward_factor']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xf2\xde\x1f\x1byaml:"oracle_reward_factor"'
    _PARAMS.fields_by_name['small_liquidation_size']._options = None
    _PARAMS.fields_by_name['small_liquidation_size']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xf2\xde\x1f\x1dyaml:"small_liquidation_size"'
    _PARAMS._options = None
    _PARAMS._serialized_options = b'\x98\xa0\x1f\x00'
    _TOKEN.fields_by_name['base_denom']._options = None
    _TOKEN.fields_by_name['base_denom']._serialized_options = b'\xf2\xde\x1f\x11yaml:"base_denom"'
    _TOKEN.fields_by_name['reserve_factor']._options = None
    _TOKEN.fields_by_name['reserve_factor']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xf2\xde\x1f\x15yaml:"reserve_factor"'
    _TOKEN.fields_by_name['collateral_weight']._options = None
    _TOKEN.fields_by_name['collateral_weight']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xf2\xde\x1f\x18yaml:"collateral_weight"'
    _TOKEN.fields_by_name['liquidation_threshold']._options = None
    _TOKEN.fields_by_name['liquidation_threshold']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xf2\xde\x1f\x1cyaml:"liquidation_threshold"'
    _TOKEN.fields_by_name['base_borrow_rate']._options = None
    _TOKEN.fields_by_name['base_borrow_rate']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xf2\xde\x1f\x17yaml:"base_borrow_rate"'
    _TOKEN.fields_by_name['kink_borrow_rate']._options = None
    _TOKEN.fields_by_name['kink_borrow_rate']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xf2\xde\x1f\x17yaml:"kink_borrow_rate"'
    _TOKEN.fields_by_name['max_borrow_rate']._options = None
    _TOKEN.fields_by_name['max_borrow_rate']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:"max_borrow_rate"'
    _TOKEN.fields_by_name['kink_utilization_rate']._options = None
    _TOKEN.fields_by_name['kink_utilization_rate']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xf2\xde\x1f\x1cyaml:"kink_utilization_rate"'
    _TOKEN.fields_by_name['liquidation_incentive']._options = None
    _TOKEN.fields_by_name['liquidation_incentive']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xf2\xde\x1f\x1cyaml:"liquidation_incentive"'
    _TOKEN.fields_by_name['symbol_denom']._options = None
    _TOKEN.fields_by_name['symbol_denom']._serialized_options = b'\xf2\xde\x1f\x13yaml:"symbol_denom"'
    _TOKEN.fields_by_name['exponent']._options = None
    _TOKEN.fields_by_name['exponent']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"exponent"'
    _TOKEN._options = None
    _TOKEN._serialized_options = b'\xe8\xa0\x1f\x01'
    _PARAMS._serialized_start = 98
    _PARAMS._serialized_end = 572
    _TOKEN._serialized_start = 575
    _TOKEN._serialized_end = 1551
