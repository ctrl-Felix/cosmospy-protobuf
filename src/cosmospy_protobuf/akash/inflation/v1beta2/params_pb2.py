
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$akash/inflation/v1beta2/params.proto\x12\x17akash.inflation.v1beta2\x1a\x14gogoproto/gogo.proto"\xab\x03\n\x06Params\x12\xa2\x01\n\x16inflation_decay_factor\x18\x01 \x01(\tB\x81\x01\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xe2\xde\x1f\x14InflationDecayFactor\xea\xde\x1f\x16inflation_decay_factor\xf2\xde\x1f\x1dyaml:"inflation_decay_factor"\x12\x8e\x01\n\x11initial_inflation\x18\x02 \x01(\tBs\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xe2\xde\x1f\x10InitialInflation\xea\xde\x1f\x11initial_inflation\xf2\xde\x1f\x18yaml:"initial_inflation"\x12k\n\x08variance\x18\x03 \x01(\tBY\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xe2\xde\x1f\x08Variance\xea\xde\x1f\x08variance\xf2\xde\x1f\x0fyaml:"variance"B3Z1github.com/ovrclk/akash/x/inflation/types/v1beta2b\x06proto3')
_PARAMS = DESCRIPTOR.message_types_by_name['Params']
Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {'DESCRIPTOR': _PARAMS, '__module__': 'akash.inflation.v1beta2.params_pb2'})
_sym_db.RegisterMessage(Params)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z1github.com/ovrclk/akash/x/inflation/types/v1beta2'
    _PARAMS.fields_by_name['inflation_decay_factor']._options = None
    _PARAMS.fields_by_name['inflation_decay_factor']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xe2\xde\x1f\x14InflationDecayFactor\xea\xde\x1f\x16inflation_decay_factor\xf2\xde\x1f\x1dyaml:"inflation_decay_factor"'
    _PARAMS.fields_by_name['initial_inflation']._options = None
    _PARAMS.fields_by_name['initial_inflation']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xe2\xde\x1f\x10InitialInflation\xea\xde\x1f\x11initial_inflation\xf2\xde\x1f\x18yaml:"initial_inflation"'
    _PARAMS.fields_by_name['variance']._options = None
    _PARAMS.fields_by_name['variance']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\xe2\xde\x1f\x08Variance\xea\xde\x1f\x08variance\xf2\xde\x1f\x0fyaml:"variance"'
    _PARAMS._serialized_start = 88
    _PARAMS._serialized_end = 515
