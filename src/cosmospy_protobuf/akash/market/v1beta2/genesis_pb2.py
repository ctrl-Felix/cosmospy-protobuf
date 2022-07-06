
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.market.v1beta2 import order_pb2 as akash_dot_market_dot_v1beta2_dot_order__pb2
from ....akash.market.v1beta2 import lease_pb2 as akash_dot_market_dot_v1beta2_dot_lease__pb2
from ....akash.market.v1beta2 import params_pb2 as akash_dot_market_dot_v1beta2_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"akash/market/v1beta2/genesis.proto\x12\x14akash.market.v1beta2\x1a\x14gogoproto/gogo.proto\x1a akash/market/v1beta2/order.proto\x1a akash/market/v1beta2/lease.proto\x1a!akash/market/v1beta2/params.proto"\xf9\x01\n\x0cGenesisState\x12L\n\x06orders\x18\x01 \x03(\x0b2\x1b.akash.market.v1beta2.OrderB\x1f\xc8\xde\x1f\x00\xea\xde\x1f\x06orders\xf2\xde\x1f\ryaml:"orders"\x12L\n\x06leases\x18\x02 \x03(\x0b2\x1b.akash.market.v1beta2.LeaseB\x1f\xc8\xde\x1f\x00\xea\xde\x1f\x06leases\xf2\xde\x1f\ryaml:"leases"\x12M\n\x06params\x18\x03 \x01(\x0b2\x1c.akash.market.v1beta2.ParamsB\x1f\xc8\xde\x1f\x00\xea\xde\x1f\x06params\xf2\xde\x1f\ryaml:"params"B0Z.github.com/ovrclk/akash/x/market/types/v1beta2b\x06proto3')
_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {'DESCRIPTOR': _GENESISSTATE, '__module__': 'akash.market.v1beta2.genesis_pb2'})
_sym_db.RegisterMessage(GenesisState)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z.github.com/ovrclk/akash/x/market/types/v1beta2'
    _GENESISSTATE.fields_by_name['orders']._options = None
    _GENESISSTATE.fields_by_name['orders']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x06orders\xf2\xde\x1f\ryaml:"orders"'
    _GENESISSTATE.fields_by_name['leases']._options = None
    _GENESISSTATE.fields_by_name['leases']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x06leases\xf2\xde\x1f\ryaml:"leases"'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x06params\xf2\xde\x1f\ryaml:"params"'
    _GENESISSTATE._serialized_start = 186
    _GENESISSTATE._serialized_end = 435
