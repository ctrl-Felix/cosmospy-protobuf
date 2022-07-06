
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.inflation.v1beta2 import params_pb2 as akash_dot_inflation_dot_v1beta2_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%akash/inflation/v1beta2/genesis.proto\x12\x17akash.inflation.v1beta2\x1a\x14gogoproto/gogo.proto\x1a$akash/inflation/v1beta2/params.proto"`\n\x0cGenesisState\x12P\n\x06params\x18\x01 \x01(\x0b2\x1f.akash.inflation.v1beta2.ParamsB\x1f\xc8\xde\x1f\x00\xea\xde\x1f\x06params\xf2\xde\x1f\ryaml:"params"B3Z1github.com/ovrclk/akash/x/inflation/types/v1beta2b\x06proto3')
_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {'DESCRIPTOR': _GENESISSTATE, '__module__': 'akash.inflation.v1beta2.genesis_pb2'})
_sym_db.RegisterMessage(GenesisState)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z1github.com/ovrclk/akash/x/inflation/types/v1beta2'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x06params\xf2\xde\x1f\ryaml:"params"'
    _GENESISSTATE._serialized_start = 126
    _GENESISSTATE._serialized_end = 222
