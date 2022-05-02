
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from .....osmosis.gamm.pool_models.balancer import balancerPool_pb2 as osmosis_dot_gamm_dot_pool__models_dot_balancer_dot_balancerPool__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*osmosis/gamm/pool-models/balancer/tx.proto\x12\x14osmosis.gamm.v1beta1\x1a\x14gogoproto/gogo.proto\x1a4osmosis/gamm/pool-models/balancer/balancerPool.proto"\x82\x02\n\x15MsgCreateBalancerPool\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12L\n\npoolParams\x18\x02 \x01(\x0b2 .osmosis.gamm.v1beta1.PoolParamsB\x16\xf2\xde\x1f\x12yaml:"pool_params"\x129\n\npoolAssets\x18\x03 \x03(\x0b2\x1f.osmosis.gamm.v1beta1.PoolAssetB\x04\xc8\xde\x1f\x00\x12=\n\x14future_pool_governor\x18\x04 \x01(\tB\x1f\xf2\xde\x1f\x1byaml:"future_pool_governor""<\n\x1dMsgCreateBalancerPoolResponse\x12\x1b\n\x07pool_id\x18\x01 \x01(\x04B\n\xe2\xde\x1f\x06PoolID2}\n\x03Msg\x12v\n\x12CreateBalancerPool\x12+.osmosis.gamm.v1beta1.MsgCreateBalancerPool\x1a3.osmosis.gamm.v1beta1.MsgCreateBalancerPoolResponseB@Z>github.com/osmosis-labs/osmosis/v7/x/gamm/pool-models/balancerb\x06proto3')
_MSGCREATEBALANCERPOOL = DESCRIPTOR.message_types_by_name['MsgCreateBalancerPool']
_MSGCREATEBALANCERPOOLRESPONSE = DESCRIPTOR.message_types_by_name['MsgCreateBalancerPoolResponse']
MsgCreateBalancerPool = _reflection.GeneratedProtocolMessageType('MsgCreateBalancerPool', (_message.Message,), {'DESCRIPTOR': _MSGCREATEBALANCERPOOL, '__module__': 'osmosis.gamm.pool_models.balancer.tx_pb2'})
_sym_db.RegisterMessage(MsgCreateBalancerPool)
MsgCreateBalancerPoolResponse = _reflection.GeneratedProtocolMessageType('MsgCreateBalancerPoolResponse', (_message.Message,), {'DESCRIPTOR': _MSGCREATEBALANCERPOOLRESPONSE, '__module__': 'osmosis.gamm.pool_models.balancer.tx_pb2'})
_sym_db.RegisterMessage(MsgCreateBalancerPoolResponse)
_MSG = DESCRIPTOR.services_by_name['Msg']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z>github.com/osmosis-labs/osmosis/v7/x/gamm/pool-models/balancer'
    _MSGCREATEBALANCERPOOL.fields_by_name['sender']._options = None
    _MSGCREATEBALANCERPOOL.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGCREATEBALANCERPOOL.fields_by_name['poolParams']._options = None
    _MSGCREATEBALANCERPOOL.fields_by_name['poolParams']._serialized_options = b'\xf2\xde\x1f\x12yaml:"pool_params"'
    _MSGCREATEBALANCERPOOL.fields_by_name['poolAssets']._options = None
    _MSGCREATEBALANCERPOOL.fields_by_name['poolAssets']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGCREATEBALANCERPOOL.fields_by_name['future_pool_governor']._options = None
    _MSGCREATEBALANCERPOOL.fields_by_name['future_pool_governor']._serialized_options = b'\xf2\xde\x1f\x1byaml:"future_pool_governor"'
    _MSGCREATEBALANCERPOOLRESPONSE.fields_by_name['pool_id']._options = None
    _MSGCREATEBALANCERPOOLRESPONSE.fields_by_name['pool_id']._serialized_options = b'\xe2\xde\x1f\x06PoolID'
    _MSGCREATEBALANCERPOOL._serialized_start = 145
    _MSGCREATEBALANCERPOOL._serialized_end = 403
    _MSGCREATEBALANCERPOOLRESPONSE._serialized_start = 405
    _MSGCREATEBALANCERPOOLRESPONSE._serialized_end = 465
    _MSG._serialized_start = 467
    _MSG._serialized_end = 592
