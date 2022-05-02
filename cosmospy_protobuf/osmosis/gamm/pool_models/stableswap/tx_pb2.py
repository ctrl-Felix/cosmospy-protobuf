
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from .....osmosis.gamm.pool_models.stableswap import stableswap_pool_pb2 as osmosis_dot_gamm_dot_pool__models_dot_stableswap_dot_stableswap__pool__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,osmosis/gamm/pool-models/stableswap/tx.proto\x12\x1fosmosis.gamm.stableswap.v1beta1\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\x1a9osmosis/gamm/pool-models/stableswap/stableswap_pool.proto"\xc1\x02\n\x17MsgCreateStableswapPool\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12W\n\npoolParams\x18\x02 \x01(\x0b2+.osmosis.gamm.stableswap.v1beta1.PoolParamsB\x16\xf2\xde\x1f\x12yaml:"pool_params"\x12k\n\x16initial_pool_liquidity\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12=\n\x14future_pool_governor\x18\x04 \x01(\tB\x1f\xf2\xde\x1f\x1byaml:"future_pool_governor"">\n\x1fMsgCreateStableswapPoolResponse\x12\x1b\n\x07pool_id\x18\x01 \x01(\x04B\n\xe2\xde\x1f\x06PoolID2\x9a\x01\n\x03Msg\x12\x92\x01\n\x14CreateStableswapPool\x128.osmosis.gamm.stableswap.v1beta1.MsgCreateStableswapPool\x1a@.osmosis.gamm.stableswap.v1beta1.MsgCreateStableswapPoolResponseBBZ@github.com/osmosis-labs/osmosis/v7/x/gamm/pool-models/stableswapb\x06proto3')
_MSGCREATESTABLESWAPPOOL = DESCRIPTOR.message_types_by_name['MsgCreateStableswapPool']
_MSGCREATESTABLESWAPPOOLRESPONSE = DESCRIPTOR.message_types_by_name['MsgCreateStableswapPoolResponse']
MsgCreateStableswapPool = _reflection.GeneratedProtocolMessageType('MsgCreateStableswapPool', (_message.Message,), {'DESCRIPTOR': _MSGCREATESTABLESWAPPOOL, '__module__': 'osmosis.gamm.pool_models.stableswap.tx_pb2'})
_sym_db.RegisterMessage(MsgCreateStableswapPool)
MsgCreateStableswapPoolResponse = _reflection.GeneratedProtocolMessageType('MsgCreateStableswapPoolResponse', (_message.Message,), {'DESCRIPTOR': _MSGCREATESTABLESWAPPOOLRESPONSE, '__module__': 'osmosis.gamm.pool_models.stableswap.tx_pb2'})
_sym_db.RegisterMessage(MsgCreateStableswapPoolResponse)
_MSG = DESCRIPTOR.services_by_name['Msg']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z@github.com/osmosis-labs/osmosis/v7/x/gamm/pool-models/stableswap'
    _MSGCREATESTABLESWAPPOOL.fields_by_name['sender']._options = None
    _MSGCREATESTABLESWAPPOOL.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGCREATESTABLESWAPPOOL.fields_by_name['poolParams']._options = None
    _MSGCREATESTABLESWAPPOOL.fields_by_name['poolParams']._serialized_options = b'\xf2\xde\x1f\x12yaml:"pool_params"'
    _MSGCREATESTABLESWAPPOOL.fields_by_name['initial_pool_liquidity']._options = None
    _MSGCREATESTABLESWAPPOOL.fields_by_name['initial_pool_liquidity']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _MSGCREATESTABLESWAPPOOL.fields_by_name['future_pool_governor']._options = None
    _MSGCREATESTABLESWAPPOOL.fields_by_name['future_pool_governor']._serialized_options = b'\xf2\xde\x1f\x1byaml:"future_pool_governor"'
    _MSGCREATESTABLESWAPPOOLRESPONSE.fields_by_name['pool_id']._options = None
    _MSGCREATESTABLESWAPPOOLRESPONSE.fields_by_name['pool_id']._serialized_options = b'\xe2\xde\x1f\x06PoolID'
    _MSGCREATESTABLESWAPPOOL._serialized_start = 195
    _MSGCREATESTABLESWAPPOOL._serialized_end = 516
    _MSGCREATESTABLESWAPPOOLRESPONSE._serialized_start = 518
    _MSGCREATESTABLESWAPPOOLRESPONSE._serialized_end = 580
    _MSG._serialized_start = 583
    _MSG._serialized_end = 737
