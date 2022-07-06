
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eumee/leverage/v1beta1/tx.proto\x12!umeenetwork.umee.leverage.v1beta1\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto"O\n\x0cMsgLendAsset\x12\x0e\n\x06lender\x18\x01 \x01(\t\x12/\n\x06amount\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00"S\n\x10MsgWithdrawAsset\x12\x0e\n\x06lender\x18\x01 \x01(\t\x12/\n\x06amount\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00"C\n\x10MsgSetCollateral\x12\x10\n\x08borrower\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t\x12\x0e\n\x06enable\x18\x03 \x01(\x08"S\n\x0eMsgBorrowAsset\x12\x10\n\x08borrower\x18\x01 \x01(\t\x12/\n\x06amount\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00"R\n\rMsgRepayAsset\x12\x10\n\x08borrower\x18\x01 \x01(\t\x12/\n\x06amount\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00"\x99\x01\n\x0cMsgLiquidate\x12\x12\n\nliquidator\x18\x01 \x01(\t\x12\x10\n\x08borrower\x18\x02 \x01(\t\x122\n\trepayment\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12/\n\x06reward\x18\x04 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00"\x16\n\x14MsgLendAssetResponse"\x1a\n\x18MsgWithdrawAssetResponse"\x1a\n\x18MsgSetCollateralResponse"\x18\n\x16MsgBorrowAssetResponse"H\n\x15MsgRepayAssetResponse\x12/\n\x06repaid\x18\x01 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00"x\n\x14MsgLiquidateResponse\x12/\n\x06repaid\x18\x01 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12/\n\x06reward\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x002\xf2\x05\n\x03Msg\x12u\n\tLendAsset\x12/.umeenetwork.umee.leverage.v1beta1.MsgLendAsset\x1a7.umeenetwork.umee.leverage.v1beta1.MsgLendAssetResponse\x12\x81\x01\n\rWithdrawAsset\x123.umeenetwork.umee.leverage.v1beta1.MsgWithdrawAsset\x1a;.umeenetwork.umee.leverage.v1beta1.MsgWithdrawAssetResponse\x12\x81\x01\n\rSetCollateral\x123.umeenetwork.umee.leverage.v1beta1.MsgSetCollateral\x1a;.umeenetwork.umee.leverage.v1beta1.MsgSetCollateralResponse\x12{\n\x0bBorrowAsset\x121.umeenetwork.umee.leverage.v1beta1.MsgBorrowAsset\x1a9.umeenetwork.umee.leverage.v1beta1.MsgBorrowAssetResponse\x12x\n\nRepayAsset\x120.umeenetwork.umee.leverage.v1beta1.MsgRepayAsset\x1a8.umeenetwork.umee.leverage.v1beta1.MsgRepayAssetResponse\x12u\n\tLiquidate\x12/.umeenetwork.umee.leverage.v1beta1.MsgLiquidate\x1a7.umeenetwork.umee.leverage.v1beta1.MsgLiquidateResponseB2Z0github.com/umee-network/umee/v2/x/leverage/typesb\x06proto3')
_MSGLENDASSET = DESCRIPTOR.message_types_by_name['MsgLendAsset']
_MSGWITHDRAWASSET = DESCRIPTOR.message_types_by_name['MsgWithdrawAsset']
_MSGSETCOLLATERAL = DESCRIPTOR.message_types_by_name['MsgSetCollateral']
_MSGBORROWASSET = DESCRIPTOR.message_types_by_name['MsgBorrowAsset']
_MSGREPAYASSET = DESCRIPTOR.message_types_by_name['MsgRepayAsset']
_MSGLIQUIDATE = DESCRIPTOR.message_types_by_name['MsgLiquidate']
_MSGLENDASSETRESPONSE = DESCRIPTOR.message_types_by_name['MsgLendAssetResponse']
_MSGWITHDRAWASSETRESPONSE = DESCRIPTOR.message_types_by_name['MsgWithdrawAssetResponse']
_MSGSETCOLLATERALRESPONSE = DESCRIPTOR.message_types_by_name['MsgSetCollateralResponse']
_MSGBORROWASSETRESPONSE = DESCRIPTOR.message_types_by_name['MsgBorrowAssetResponse']
_MSGREPAYASSETRESPONSE = DESCRIPTOR.message_types_by_name['MsgRepayAssetResponse']
_MSGLIQUIDATERESPONSE = DESCRIPTOR.message_types_by_name['MsgLiquidateResponse']
MsgLendAsset = _reflection.GeneratedProtocolMessageType('MsgLendAsset', (_message.Message,), {'DESCRIPTOR': _MSGLENDASSET, '__module__': 'umee.leverage.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgLendAsset)
MsgWithdrawAsset = _reflection.GeneratedProtocolMessageType('MsgWithdrawAsset', (_message.Message,), {'DESCRIPTOR': _MSGWITHDRAWASSET, '__module__': 'umee.leverage.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgWithdrawAsset)
MsgSetCollateral = _reflection.GeneratedProtocolMessageType('MsgSetCollateral', (_message.Message,), {'DESCRIPTOR': _MSGSETCOLLATERAL, '__module__': 'umee.leverage.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgSetCollateral)
MsgBorrowAsset = _reflection.GeneratedProtocolMessageType('MsgBorrowAsset', (_message.Message,), {'DESCRIPTOR': _MSGBORROWASSET, '__module__': 'umee.leverage.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgBorrowAsset)
MsgRepayAsset = _reflection.GeneratedProtocolMessageType('MsgRepayAsset', (_message.Message,), {'DESCRIPTOR': _MSGREPAYASSET, '__module__': 'umee.leverage.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgRepayAsset)
MsgLiquidate = _reflection.GeneratedProtocolMessageType('MsgLiquidate', (_message.Message,), {'DESCRIPTOR': _MSGLIQUIDATE, '__module__': 'umee.leverage.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgLiquidate)
MsgLendAssetResponse = _reflection.GeneratedProtocolMessageType('MsgLendAssetResponse', (_message.Message,), {'DESCRIPTOR': _MSGLENDASSETRESPONSE, '__module__': 'umee.leverage.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgLendAssetResponse)
MsgWithdrawAssetResponse = _reflection.GeneratedProtocolMessageType('MsgWithdrawAssetResponse', (_message.Message,), {'DESCRIPTOR': _MSGWITHDRAWASSETRESPONSE, '__module__': 'umee.leverage.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgWithdrawAssetResponse)
MsgSetCollateralResponse = _reflection.GeneratedProtocolMessageType('MsgSetCollateralResponse', (_message.Message,), {'DESCRIPTOR': _MSGSETCOLLATERALRESPONSE, '__module__': 'umee.leverage.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgSetCollateralResponse)
MsgBorrowAssetResponse = _reflection.GeneratedProtocolMessageType('MsgBorrowAssetResponse', (_message.Message,), {'DESCRIPTOR': _MSGBORROWASSETRESPONSE, '__module__': 'umee.leverage.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgBorrowAssetResponse)
MsgRepayAssetResponse = _reflection.GeneratedProtocolMessageType('MsgRepayAssetResponse', (_message.Message,), {'DESCRIPTOR': _MSGREPAYASSETRESPONSE, '__module__': 'umee.leverage.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgRepayAssetResponse)
MsgLiquidateResponse = _reflection.GeneratedProtocolMessageType('MsgLiquidateResponse', (_message.Message,), {'DESCRIPTOR': _MSGLIQUIDATERESPONSE, '__module__': 'umee.leverage.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgLiquidateResponse)
_MSG = DESCRIPTOR.services_by_name['Msg']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z0github.com/umee-network/umee/v2/x/leverage/types'
    _MSGLENDASSET.fields_by_name['amount']._options = None
    _MSGLENDASSET.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGWITHDRAWASSET.fields_by_name['amount']._options = None
    _MSGWITHDRAWASSET.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGBORROWASSET.fields_by_name['amount']._options = None
    _MSGBORROWASSET.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGREPAYASSET.fields_by_name['amount']._options = None
    _MSGREPAYASSET.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGLIQUIDATE.fields_by_name['repayment']._options = None
    _MSGLIQUIDATE.fields_by_name['repayment']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGLIQUIDATE.fields_by_name['reward']._options = None
    _MSGLIQUIDATE.fields_by_name['reward']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGREPAYASSETRESPONSE.fields_by_name['repaid']._options = None
    _MSGREPAYASSETRESPONSE.fields_by_name['repaid']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGLIQUIDATERESPONSE.fields_by_name['repaid']._options = None
    _MSGLIQUIDATERESPONSE.fields_by_name['repaid']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGLIQUIDATERESPONSE.fields_by_name['reward']._options = None
    _MSGLIQUIDATERESPONSE.fields_by_name['reward']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGLENDASSET._serialized_start = 123
    _MSGLENDASSET._serialized_end = 202
    _MSGWITHDRAWASSET._serialized_start = 204
    _MSGWITHDRAWASSET._serialized_end = 287
    _MSGSETCOLLATERAL._serialized_start = 289
    _MSGSETCOLLATERAL._serialized_end = 356
    _MSGBORROWASSET._serialized_start = 358
    _MSGBORROWASSET._serialized_end = 441
    _MSGREPAYASSET._serialized_start = 443
    _MSGREPAYASSET._serialized_end = 525
    _MSGLIQUIDATE._serialized_start = 528
    _MSGLIQUIDATE._serialized_end = 681
    _MSGLENDASSETRESPONSE._serialized_start = 683
    _MSGLENDASSETRESPONSE._serialized_end = 705
    _MSGWITHDRAWASSETRESPONSE._serialized_start = 707
    _MSGWITHDRAWASSETRESPONSE._serialized_end = 733
    _MSGSETCOLLATERALRESPONSE._serialized_start = 735
    _MSGSETCOLLATERALRESPONSE._serialized_end = 761
    _MSGBORROWASSETRESPONSE._serialized_start = 763
    _MSGBORROWASSETRESPONSE._serialized_end = 787
    _MSGREPAYASSETRESPONSE._serialized_start = 789
    _MSGREPAYASSETRESPONSE._serialized_end = 861
    _MSGLIQUIDATERESPONSE._serialized_start = 863
    _MSGLIQUIDATERESPONSE._serialized_end = 983
    _MSG._serialized_start = 986
    _MSG._serialized_end = 1740
