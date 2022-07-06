
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dosmosis/gamm/v1beta1/tx.proto\x12\x14osmosis.gamm.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\x8b\x02\n\x0bMsgJoinPool\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12"\n\x06poolId\x18\x02 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id"\x12`\n\x0eshareOutAmount\x18\x03 \x01(\tBH\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:"pool_amount_out"\xc8\xde\x1f\x00\x12S\n\x0btokenInMaxs\x18\x04 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB#\xf2\xde\x1f\x1byaml:"token_in_max_amounts"\xc8\xde\x1f\x00"\x15\n\x13MsgJoinPoolResponse"\x8c\x02\n\x0bMsgExitPool\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12"\n\x06poolId\x18\x02 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id"\x12_\n\rshareInAmount\x18\x03 \x01(\tBH\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:"share_in_amount"\xc8\xde\x1f\x00\x12U\n\x0ctokenOutMins\x18\x04 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB$\xf2\xde\x1f\x1cyaml:"token_out_min_amounts"\xc8\xde\x1f\x00"\x15\n\x13MsgExitPoolResponse"j\n\x11SwapAmountInRoute\x12"\n\x06poolId\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id"\x121\n\rtokenOutDenom\x18\x02 \x01(\tB\x1a\xf2\xde\x1f\x16yaml:"token_out_denom""\xa7\x02\n\x14MsgSwapExactAmountIn\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12=\n\x06routes\x18\x02 \x03(\x0b2\'.osmosis.gamm.v1beta1.SwapAmountInRouteB\x04\xc8\xde\x1f\x00\x12C\n\x07tokenIn\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x17\xf2\xde\x1f\x0fyaml:"token_in"\xc8\xde\x1f\x00\x12h\n\x11tokenOutMinAmount\x18\x04 \x01(\tBM\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x1byaml:"token_out_min_amount"\xc8\xde\x1f\x00"\x81\x01\n\x1cMsgSwapExactAmountInResponse\x12a\n\x0etokenOutAmount\x18\x01 \x01(\tBI\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x17yaml:"token_out_amount"\xc8\xde\x1f\x00"j\n\x12SwapAmountOutRoute\x12"\n\x06poolId\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id"\x120\n\x0ctokenInDenom\x18\x02 \x01(\tB\x1a\xf2\xde\x1f\x16yaml:"token_out_denom""\xa9\x02\n\x15MsgSwapExactAmountOut\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12>\n\x06routes\x18\x02 \x03(\x0b2(.osmosis.gamm.v1beta1.SwapAmountOutRouteB\x04\xc8\xde\x1f\x00\x12f\n\x10tokenInMaxAmount\x18\x03 \x01(\tBL\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x1ayaml:"token_in_max_amount"\xc8\xde\x1f\x00\x12E\n\x08tokenOut\x18\x04 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x18\xf2\xde\x1f\x10yaml:"token_out"\xc8\xde\x1f\x00"\x80\x01\n\x1dMsgSwapExactAmountOutResponse\x12_\n\rtokenInAmount\x18\x01 \x01(\tBH\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:"token_in_amount"\xc8\xde\x1f\x00"\x91\x02\n\x19MsgJoinSwapExternAmountIn\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12"\n\x06poolId\x18\x02 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id"\x12C\n\x07tokenIn\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x17\xf2\xde\x1f\x0fyaml:"token_in"\xc8\xde\x1f\x00\x12h\n\x11shareOutMinAmount\x18\x04 \x01(\tBM\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x1byaml:"share_out_min_amount"\xc8\xde\x1f\x00"\x86\x01\n!MsgJoinSwapExternAmountInResponse\x12a\n\x0eshareOutAmount\x18\x01 \x01(\tBI\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x17yaml:"share_out_amount"\xc8\xde\x1f\x00"\xde\x02\n\x19MsgJoinSwapShareAmountOut\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12"\n\x06poolId\x18\x02 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id"\x12/\n\x0ctokenInDenom\x18\x03 \x01(\tB\x19\xf2\xde\x1f\x15yaml:"token_in_denom"\x12a\n\x0eshareOutAmount\x18\x04 \x01(\tBI\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x17yaml:"share_out_amount"\xc8\xde\x1f\x00\x12f\n\x10tokenInMaxAmount\x18\x05 \x01(\tBL\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x1ayaml:"token_in_max_amount"\xc8\xde\x1f\x00"\x84\x01\n!MsgJoinSwapShareAmountOutResponse\x12_\n\rtokenInAmount\x18\x01 \x01(\tBH\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:"token_in_amount"\xc8\xde\x1f\x00"\xdf\x02\n\x18MsgExitSwapShareAmountIn\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12"\n\x06poolId\x18\x02 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id"\x121\n\rtokenOutDenom\x18\x03 \x01(\tB\x1a\xf2\xde\x1f\x16yaml:"token_out_denom"\x12_\n\rshareInAmount\x18\x04 \x01(\tBH\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:"share_in_amount"\xc8\xde\x1f\x00\x12h\n\x11tokenOutMinAmount\x18\x05 \x01(\tBM\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x1byaml:"token_out_min_amount"\xc8\xde\x1f\x00"\x85\x01\n MsgExitSwapShareAmountInResponse\x12a\n\x0etokenOutAmount\x18\x01 \x01(\tBI\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x17yaml:"token_out_amount"\xc8\xde\x1f\x00"\x92\x02\n\x1aMsgExitSwapExternAmountOut\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12"\n\x06poolId\x18\x02 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id"\x12E\n\x08tokenOut\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x18\xf2\xde\x1f\x10yaml:"token_out"\xc8\xde\x1f\x00\x12f\n\x10shareInMaxAmount\x18\x04 \x01(\tBL\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x1ayaml:"share_in_max_amount"\xc8\xde\x1f\x00"\x85\x01\n"MsgExitSwapExternAmountOutResponse\x12_\n\rshareInAmount\x18\x01 \x01(\tBH\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:"share_in_amount"\xc8\xde\x1f\x002\xb9\x07\n\x03Msg\x12X\n\x08JoinPool\x12!.osmosis.gamm.v1beta1.MsgJoinPool\x1a).osmosis.gamm.v1beta1.MsgJoinPoolResponse\x12X\n\x08ExitPool\x12!.osmosis.gamm.v1beta1.MsgExitPool\x1a).osmosis.gamm.v1beta1.MsgExitPoolResponse\x12s\n\x11SwapExactAmountIn\x12*.osmosis.gamm.v1beta1.MsgSwapExactAmountIn\x1a2.osmosis.gamm.v1beta1.MsgSwapExactAmountInResponse\x12v\n\x12SwapExactAmountOut\x12+.osmosis.gamm.v1beta1.MsgSwapExactAmountOut\x1a3.osmosis.gamm.v1beta1.MsgSwapExactAmountOutResponse\x12\x82\x01\n\x16JoinSwapExternAmountIn\x12/.osmosis.gamm.v1beta1.MsgJoinSwapExternAmountIn\x1a7.osmosis.gamm.v1beta1.MsgJoinSwapExternAmountInResponse\x12\x82\x01\n\x16JoinSwapShareAmountOut\x12/.osmosis.gamm.v1beta1.MsgJoinSwapShareAmountOut\x1a7.osmosis.gamm.v1beta1.MsgJoinSwapShareAmountOutResponse\x12\x85\x01\n\x17ExitSwapExternAmountOut\x120.osmosis.gamm.v1beta1.MsgExitSwapExternAmountOut\x1a8.osmosis.gamm.v1beta1.MsgExitSwapExternAmountOutResponse\x12\x7f\n\x15ExitSwapShareAmountIn\x12..osmosis.gamm.v1beta1.MsgExitSwapShareAmountIn\x1a6.osmosis.gamm.v1beta1.MsgExitSwapShareAmountInResponseB1Z/github.com/osmosis-labs/osmosis/v7/x/gamm/typesb\x06proto3')
_MSGJOINPOOL = DESCRIPTOR.message_types_by_name['MsgJoinPool']
_MSGJOINPOOLRESPONSE = DESCRIPTOR.message_types_by_name['MsgJoinPoolResponse']
_MSGEXITPOOL = DESCRIPTOR.message_types_by_name['MsgExitPool']
_MSGEXITPOOLRESPONSE = DESCRIPTOR.message_types_by_name['MsgExitPoolResponse']
_SWAPAMOUNTINROUTE = DESCRIPTOR.message_types_by_name['SwapAmountInRoute']
_MSGSWAPEXACTAMOUNTIN = DESCRIPTOR.message_types_by_name['MsgSwapExactAmountIn']
_MSGSWAPEXACTAMOUNTINRESPONSE = DESCRIPTOR.message_types_by_name['MsgSwapExactAmountInResponse']
_SWAPAMOUNTOUTROUTE = DESCRIPTOR.message_types_by_name['SwapAmountOutRoute']
_MSGSWAPEXACTAMOUNTOUT = DESCRIPTOR.message_types_by_name['MsgSwapExactAmountOut']
_MSGSWAPEXACTAMOUNTOUTRESPONSE = DESCRIPTOR.message_types_by_name['MsgSwapExactAmountOutResponse']
_MSGJOINSWAPEXTERNAMOUNTIN = DESCRIPTOR.message_types_by_name['MsgJoinSwapExternAmountIn']
_MSGJOINSWAPEXTERNAMOUNTINRESPONSE = DESCRIPTOR.message_types_by_name['MsgJoinSwapExternAmountInResponse']
_MSGJOINSWAPSHAREAMOUNTOUT = DESCRIPTOR.message_types_by_name['MsgJoinSwapShareAmountOut']
_MSGJOINSWAPSHAREAMOUNTOUTRESPONSE = DESCRIPTOR.message_types_by_name['MsgJoinSwapShareAmountOutResponse']
_MSGEXITSWAPSHAREAMOUNTIN = DESCRIPTOR.message_types_by_name['MsgExitSwapShareAmountIn']
_MSGEXITSWAPSHAREAMOUNTINRESPONSE = DESCRIPTOR.message_types_by_name['MsgExitSwapShareAmountInResponse']
_MSGEXITSWAPEXTERNAMOUNTOUT = DESCRIPTOR.message_types_by_name['MsgExitSwapExternAmountOut']
_MSGEXITSWAPEXTERNAMOUNTOUTRESPONSE = DESCRIPTOR.message_types_by_name['MsgExitSwapExternAmountOutResponse']
MsgJoinPool = _reflection.GeneratedProtocolMessageType('MsgJoinPool', (_message.Message,), {'DESCRIPTOR': _MSGJOINPOOL, '__module__': 'osmosis.gamm.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgJoinPool)
MsgJoinPoolResponse = _reflection.GeneratedProtocolMessageType('MsgJoinPoolResponse', (_message.Message,), {'DESCRIPTOR': _MSGJOINPOOLRESPONSE, '__module__': 'osmosis.gamm.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgJoinPoolResponse)
MsgExitPool = _reflection.GeneratedProtocolMessageType('MsgExitPool', (_message.Message,), {'DESCRIPTOR': _MSGEXITPOOL, '__module__': 'osmosis.gamm.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgExitPool)
MsgExitPoolResponse = _reflection.GeneratedProtocolMessageType('MsgExitPoolResponse', (_message.Message,), {'DESCRIPTOR': _MSGEXITPOOLRESPONSE, '__module__': 'osmosis.gamm.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgExitPoolResponse)
SwapAmountInRoute = _reflection.GeneratedProtocolMessageType('SwapAmountInRoute', (_message.Message,), {'DESCRIPTOR': _SWAPAMOUNTINROUTE, '__module__': 'osmosis.gamm.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(SwapAmountInRoute)
MsgSwapExactAmountIn = _reflection.GeneratedProtocolMessageType('MsgSwapExactAmountIn', (_message.Message,), {'DESCRIPTOR': _MSGSWAPEXACTAMOUNTIN, '__module__': 'osmosis.gamm.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgSwapExactAmountIn)
MsgSwapExactAmountInResponse = _reflection.GeneratedProtocolMessageType('MsgSwapExactAmountInResponse', (_message.Message,), {'DESCRIPTOR': _MSGSWAPEXACTAMOUNTINRESPONSE, '__module__': 'osmosis.gamm.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgSwapExactAmountInResponse)
SwapAmountOutRoute = _reflection.GeneratedProtocolMessageType('SwapAmountOutRoute', (_message.Message,), {'DESCRIPTOR': _SWAPAMOUNTOUTROUTE, '__module__': 'osmosis.gamm.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(SwapAmountOutRoute)
MsgSwapExactAmountOut = _reflection.GeneratedProtocolMessageType('MsgSwapExactAmountOut', (_message.Message,), {'DESCRIPTOR': _MSGSWAPEXACTAMOUNTOUT, '__module__': 'osmosis.gamm.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgSwapExactAmountOut)
MsgSwapExactAmountOutResponse = _reflection.GeneratedProtocolMessageType('MsgSwapExactAmountOutResponse', (_message.Message,), {'DESCRIPTOR': _MSGSWAPEXACTAMOUNTOUTRESPONSE, '__module__': 'osmosis.gamm.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgSwapExactAmountOutResponse)
MsgJoinSwapExternAmountIn = _reflection.GeneratedProtocolMessageType('MsgJoinSwapExternAmountIn', (_message.Message,), {'DESCRIPTOR': _MSGJOINSWAPEXTERNAMOUNTIN, '__module__': 'osmosis.gamm.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgJoinSwapExternAmountIn)
MsgJoinSwapExternAmountInResponse = _reflection.GeneratedProtocolMessageType('MsgJoinSwapExternAmountInResponse', (_message.Message,), {'DESCRIPTOR': _MSGJOINSWAPEXTERNAMOUNTINRESPONSE, '__module__': 'osmosis.gamm.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgJoinSwapExternAmountInResponse)
MsgJoinSwapShareAmountOut = _reflection.GeneratedProtocolMessageType('MsgJoinSwapShareAmountOut', (_message.Message,), {'DESCRIPTOR': _MSGJOINSWAPSHAREAMOUNTOUT, '__module__': 'osmosis.gamm.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgJoinSwapShareAmountOut)
MsgJoinSwapShareAmountOutResponse = _reflection.GeneratedProtocolMessageType('MsgJoinSwapShareAmountOutResponse', (_message.Message,), {'DESCRIPTOR': _MSGJOINSWAPSHAREAMOUNTOUTRESPONSE, '__module__': 'osmosis.gamm.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgJoinSwapShareAmountOutResponse)
MsgExitSwapShareAmountIn = _reflection.GeneratedProtocolMessageType('MsgExitSwapShareAmountIn', (_message.Message,), {'DESCRIPTOR': _MSGEXITSWAPSHAREAMOUNTIN, '__module__': 'osmosis.gamm.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgExitSwapShareAmountIn)
MsgExitSwapShareAmountInResponse = _reflection.GeneratedProtocolMessageType('MsgExitSwapShareAmountInResponse', (_message.Message,), {'DESCRIPTOR': _MSGEXITSWAPSHAREAMOUNTINRESPONSE, '__module__': 'osmosis.gamm.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgExitSwapShareAmountInResponse)
MsgExitSwapExternAmountOut = _reflection.GeneratedProtocolMessageType('MsgExitSwapExternAmountOut', (_message.Message,), {'DESCRIPTOR': _MSGEXITSWAPEXTERNAMOUNTOUT, '__module__': 'osmosis.gamm.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgExitSwapExternAmountOut)
MsgExitSwapExternAmountOutResponse = _reflection.GeneratedProtocolMessageType('MsgExitSwapExternAmountOutResponse', (_message.Message,), {'DESCRIPTOR': _MSGEXITSWAPEXTERNAMOUNTOUTRESPONSE, '__module__': 'osmosis.gamm.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgExitSwapExternAmountOutResponse)
_MSG = DESCRIPTOR.services_by_name['Msg']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z/github.com/osmosis-labs/osmosis/v7/x/gamm/types'
    _MSGJOINPOOL.fields_by_name['sender']._options = None
    _MSGJOINPOOL.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGJOINPOOL.fields_by_name['poolId']._options = None
    _MSGJOINPOOL.fields_by_name['poolId']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _MSGJOINPOOL.fields_by_name['shareOutAmount']._options = None
    _MSGJOINPOOL.fields_by_name['shareOutAmount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:"pool_amount_out"\xc8\xde\x1f\x00'
    _MSGJOINPOOL.fields_by_name['tokenInMaxs']._options = None
    _MSGJOINPOOL.fields_by_name['tokenInMaxs']._serialized_options = b'\xf2\xde\x1f\x1byaml:"token_in_max_amounts"\xc8\xde\x1f\x00'
    _MSGEXITPOOL.fields_by_name['sender']._options = None
    _MSGEXITPOOL.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGEXITPOOL.fields_by_name['poolId']._options = None
    _MSGEXITPOOL.fields_by_name['poolId']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _MSGEXITPOOL.fields_by_name['shareInAmount']._options = None
    _MSGEXITPOOL.fields_by_name['shareInAmount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:"share_in_amount"\xc8\xde\x1f\x00'
    _MSGEXITPOOL.fields_by_name['tokenOutMins']._options = None
    _MSGEXITPOOL.fields_by_name['tokenOutMins']._serialized_options = b'\xf2\xde\x1f\x1cyaml:"token_out_min_amounts"\xc8\xde\x1f\x00'
    _SWAPAMOUNTINROUTE.fields_by_name['poolId']._options = None
    _SWAPAMOUNTINROUTE.fields_by_name['poolId']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _SWAPAMOUNTINROUTE.fields_by_name['tokenOutDenom']._options = None
    _SWAPAMOUNTINROUTE.fields_by_name['tokenOutDenom']._serialized_options = b'\xf2\xde\x1f\x16yaml:"token_out_denom"'
    _MSGSWAPEXACTAMOUNTIN.fields_by_name['sender']._options = None
    _MSGSWAPEXACTAMOUNTIN.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGSWAPEXACTAMOUNTIN.fields_by_name['routes']._options = None
    _MSGSWAPEXACTAMOUNTIN.fields_by_name['routes']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGSWAPEXACTAMOUNTIN.fields_by_name['tokenIn']._options = None
    _MSGSWAPEXACTAMOUNTIN.fields_by_name['tokenIn']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"token_in"\xc8\xde\x1f\x00'
    _MSGSWAPEXACTAMOUNTIN.fields_by_name['tokenOutMinAmount']._options = None
    _MSGSWAPEXACTAMOUNTIN.fields_by_name['tokenOutMinAmount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x1byaml:"token_out_min_amount"\xc8\xde\x1f\x00'
    _MSGSWAPEXACTAMOUNTINRESPONSE.fields_by_name['tokenOutAmount']._options = None
    _MSGSWAPEXACTAMOUNTINRESPONSE.fields_by_name['tokenOutAmount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x17yaml:"token_out_amount"\xc8\xde\x1f\x00'
    _SWAPAMOUNTOUTROUTE.fields_by_name['poolId']._options = None
    _SWAPAMOUNTOUTROUTE.fields_by_name['poolId']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _SWAPAMOUNTOUTROUTE.fields_by_name['tokenInDenom']._options = None
    _SWAPAMOUNTOUTROUTE.fields_by_name['tokenInDenom']._serialized_options = b'\xf2\xde\x1f\x16yaml:"token_out_denom"'
    _MSGSWAPEXACTAMOUNTOUT.fields_by_name['sender']._options = None
    _MSGSWAPEXACTAMOUNTOUT.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGSWAPEXACTAMOUNTOUT.fields_by_name['routes']._options = None
    _MSGSWAPEXACTAMOUNTOUT.fields_by_name['routes']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGSWAPEXACTAMOUNTOUT.fields_by_name['tokenInMaxAmount']._options = None
    _MSGSWAPEXACTAMOUNTOUT.fields_by_name['tokenInMaxAmount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x1ayaml:"token_in_max_amount"\xc8\xde\x1f\x00'
    _MSGSWAPEXACTAMOUNTOUT.fields_by_name['tokenOut']._options = None
    _MSGSWAPEXACTAMOUNTOUT.fields_by_name['tokenOut']._serialized_options = b'\xf2\xde\x1f\x10yaml:"token_out"\xc8\xde\x1f\x00'
    _MSGSWAPEXACTAMOUNTOUTRESPONSE.fields_by_name['tokenInAmount']._options = None
    _MSGSWAPEXACTAMOUNTOUTRESPONSE.fields_by_name['tokenInAmount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:"token_in_amount"\xc8\xde\x1f\x00'
    _MSGJOINSWAPEXTERNAMOUNTIN.fields_by_name['sender']._options = None
    _MSGJOINSWAPEXTERNAMOUNTIN.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGJOINSWAPEXTERNAMOUNTIN.fields_by_name['poolId']._options = None
    _MSGJOINSWAPEXTERNAMOUNTIN.fields_by_name['poolId']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _MSGJOINSWAPEXTERNAMOUNTIN.fields_by_name['tokenIn']._options = None
    _MSGJOINSWAPEXTERNAMOUNTIN.fields_by_name['tokenIn']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"token_in"\xc8\xde\x1f\x00'
    _MSGJOINSWAPEXTERNAMOUNTIN.fields_by_name['shareOutMinAmount']._options = None
    _MSGJOINSWAPEXTERNAMOUNTIN.fields_by_name['shareOutMinAmount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x1byaml:"share_out_min_amount"\xc8\xde\x1f\x00'
    _MSGJOINSWAPEXTERNAMOUNTINRESPONSE.fields_by_name['shareOutAmount']._options = None
    _MSGJOINSWAPEXTERNAMOUNTINRESPONSE.fields_by_name['shareOutAmount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x17yaml:"share_out_amount"\xc8\xde\x1f\x00'
    _MSGJOINSWAPSHAREAMOUNTOUT.fields_by_name['sender']._options = None
    _MSGJOINSWAPSHAREAMOUNTOUT.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGJOINSWAPSHAREAMOUNTOUT.fields_by_name['poolId']._options = None
    _MSGJOINSWAPSHAREAMOUNTOUT.fields_by_name['poolId']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _MSGJOINSWAPSHAREAMOUNTOUT.fields_by_name['tokenInDenom']._options = None
    _MSGJOINSWAPSHAREAMOUNTOUT.fields_by_name['tokenInDenom']._serialized_options = b'\xf2\xde\x1f\x15yaml:"token_in_denom"'
    _MSGJOINSWAPSHAREAMOUNTOUT.fields_by_name['shareOutAmount']._options = None
    _MSGJOINSWAPSHAREAMOUNTOUT.fields_by_name['shareOutAmount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x17yaml:"share_out_amount"\xc8\xde\x1f\x00'
    _MSGJOINSWAPSHAREAMOUNTOUT.fields_by_name['tokenInMaxAmount']._options = None
    _MSGJOINSWAPSHAREAMOUNTOUT.fields_by_name['tokenInMaxAmount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x1ayaml:"token_in_max_amount"\xc8\xde\x1f\x00'
    _MSGJOINSWAPSHAREAMOUNTOUTRESPONSE.fields_by_name['tokenInAmount']._options = None
    _MSGJOINSWAPSHAREAMOUNTOUTRESPONSE.fields_by_name['tokenInAmount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:"token_in_amount"\xc8\xde\x1f\x00'
    _MSGEXITSWAPSHAREAMOUNTIN.fields_by_name['sender']._options = None
    _MSGEXITSWAPSHAREAMOUNTIN.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGEXITSWAPSHAREAMOUNTIN.fields_by_name['poolId']._options = None
    _MSGEXITSWAPSHAREAMOUNTIN.fields_by_name['poolId']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _MSGEXITSWAPSHAREAMOUNTIN.fields_by_name['tokenOutDenom']._options = None
    _MSGEXITSWAPSHAREAMOUNTIN.fields_by_name['tokenOutDenom']._serialized_options = b'\xf2\xde\x1f\x16yaml:"token_out_denom"'
    _MSGEXITSWAPSHAREAMOUNTIN.fields_by_name['shareInAmount']._options = None
    _MSGEXITSWAPSHAREAMOUNTIN.fields_by_name['shareInAmount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:"share_in_amount"\xc8\xde\x1f\x00'
    _MSGEXITSWAPSHAREAMOUNTIN.fields_by_name['tokenOutMinAmount']._options = None
    _MSGEXITSWAPSHAREAMOUNTIN.fields_by_name['tokenOutMinAmount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x1byaml:"token_out_min_amount"\xc8\xde\x1f\x00'
    _MSGEXITSWAPSHAREAMOUNTINRESPONSE.fields_by_name['tokenOutAmount']._options = None
    _MSGEXITSWAPSHAREAMOUNTINRESPONSE.fields_by_name['tokenOutAmount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x17yaml:"token_out_amount"\xc8\xde\x1f\x00'
    _MSGEXITSWAPEXTERNAMOUNTOUT.fields_by_name['sender']._options = None
    _MSGEXITSWAPEXTERNAMOUNTOUT.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGEXITSWAPEXTERNAMOUNTOUT.fields_by_name['poolId']._options = None
    _MSGEXITSWAPEXTERNAMOUNTOUT.fields_by_name['poolId']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _MSGEXITSWAPEXTERNAMOUNTOUT.fields_by_name['tokenOut']._options = None
    _MSGEXITSWAPEXTERNAMOUNTOUT.fields_by_name['tokenOut']._serialized_options = b'\xf2\xde\x1f\x10yaml:"token_out"\xc8\xde\x1f\x00'
    _MSGEXITSWAPEXTERNAMOUNTOUT.fields_by_name['shareInMaxAmount']._options = None
    _MSGEXITSWAPEXTERNAMOUNTOUT.fields_by_name['shareInMaxAmount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x1ayaml:"share_in_max_amount"\xc8\xde\x1f\x00'
    _MSGEXITSWAPEXTERNAMOUNTOUTRESPONSE.fields_by_name['shareInAmount']._options = None
    _MSGEXITSWAPEXTERNAMOUNTOUTRESPONSE.fields_by_name['shareInAmount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:"share_in_amount"\xc8\xde\x1f\x00'
    _MSGJOINPOOL._serialized_start = 110
    _MSGJOINPOOL._serialized_end = 377
    _MSGJOINPOOLRESPONSE._serialized_start = 379
    _MSGJOINPOOLRESPONSE._serialized_end = 400
    _MSGEXITPOOL._serialized_start = 403
    _MSGEXITPOOL._serialized_end = 671
    _MSGEXITPOOLRESPONSE._serialized_start = 673
    _MSGEXITPOOLRESPONSE._serialized_end = 694
    _SWAPAMOUNTINROUTE._serialized_start = 696
    _SWAPAMOUNTINROUTE._serialized_end = 802
    _MSGSWAPEXACTAMOUNTIN._serialized_start = 805
    _MSGSWAPEXACTAMOUNTIN._serialized_end = 1100
    _MSGSWAPEXACTAMOUNTINRESPONSE._serialized_start = 1103
    _MSGSWAPEXACTAMOUNTINRESPONSE._serialized_end = 1232
    _SWAPAMOUNTOUTROUTE._serialized_start = 1234
    _SWAPAMOUNTOUTROUTE._serialized_end = 1340
    _MSGSWAPEXACTAMOUNTOUT._serialized_start = 1343
    _MSGSWAPEXACTAMOUNTOUT._serialized_end = 1640
    _MSGSWAPEXACTAMOUNTOUTRESPONSE._serialized_start = 1643
    _MSGSWAPEXACTAMOUNTOUTRESPONSE._serialized_end = 1771
    _MSGJOINSWAPEXTERNAMOUNTIN._serialized_start = 1774
    _MSGJOINSWAPEXTERNAMOUNTIN._serialized_end = 2047
    _MSGJOINSWAPEXTERNAMOUNTINRESPONSE._serialized_start = 2050
    _MSGJOINSWAPEXTERNAMOUNTINRESPONSE._serialized_end = 2184
    _MSGJOINSWAPSHAREAMOUNTOUT._serialized_start = 2187
    _MSGJOINSWAPSHAREAMOUNTOUT._serialized_end = 2537
    _MSGJOINSWAPSHAREAMOUNTOUTRESPONSE._serialized_start = 2540
    _MSGJOINSWAPSHAREAMOUNTOUTRESPONSE._serialized_end = 2672
    _MSGEXITSWAPSHAREAMOUNTIN._serialized_start = 2675
    _MSGEXITSWAPSHAREAMOUNTIN._serialized_end = 3026
    _MSGEXITSWAPSHAREAMOUNTINRESPONSE._serialized_start = 3029
    _MSGEXITSWAPSHAREAMOUNTINRESPONSE._serialized_end = 3162
    _MSGEXITSWAPEXTERNAMOUNTOUT._serialized_start = 3165
    _MSGEXITSWAPEXTERNAMOUNTOUT._serialized_end = 3439
    _MSGEXITSWAPEXTERNAMOUNTOUTRESPONSE._serialized_start = 3442
    _MSGEXITSWAPEXTERNAMOUNTOUTRESPONSE._serialized_end = 3575
    _MSG._serialized_start = 3578
    _MSG._serialized_end = 4531
