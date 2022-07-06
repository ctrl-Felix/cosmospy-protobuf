
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!akash/market/v1beta2/params.proto\x12\x14akash.market.v1beta2\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\xd5\x01\n\x06Params\x12v\n\x0fbid_min_deposit\x18\x01 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinBB\xe2\xde\x1f\rBidMinDeposit\xc8\xde\x1f\x00\xea\xde\x1f\x0fbid_min_deposit\xf2\xde\x1f\x16yaml:"bid_min_deposit"\x12S\n\x0eorder_max_bids\x18\x02 \x01(\rB;\xe2\xde\x1f\x0cOrderMaxBids\xea\xde\x1f\x0eorder_max_bids\xf2\xde\x1f\x15yaml:"order_max_bids"B0Z.github.com/ovrclk/akash/x/market/types/v1beta2b\x06proto3')
_PARAMS = DESCRIPTOR.message_types_by_name['Params']
Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {'DESCRIPTOR': _PARAMS, '__module__': 'akash.market.v1beta2.params_pb2'})
_sym_db.RegisterMessage(Params)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z.github.com/ovrclk/akash/x/market/types/v1beta2'
    _PARAMS.fields_by_name['bid_min_deposit']._options = None
    _PARAMS.fields_by_name['bid_min_deposit']._serialized_options = b'\xe2\xde\x1f\rBidMinDeposit\xc8\xde\x1f\x00\xea\xde\x1f\x0fbid_min_deposit\xf2\xde\x1f\x16yaml:"bid_min_deposit"'
    _PARAMS.fields_by_name['order_max_bids']._options = None
    _PARAMS.fields_by_name['order_max_bids']._serialized_options = b'\xe2\xde\x1f\x0cOrderMaxBids\xea\xde\x1f\x0eorder_max_bids\xf2\xde\x1f\x15yaml:"order_max_bids"'
    _PARAMS._serialized_start = 114
    _PARAMS._serialized_end = 327
