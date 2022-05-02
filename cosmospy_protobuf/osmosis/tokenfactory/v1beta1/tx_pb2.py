
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%osmosis/tokenfactory/v1beta1/tx.proto\x12\x1cosmosis.tokenfactory.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"T\n\x0eMsgCreateDenom\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12\x1f\n\x05nonce\x18\x02 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"nonce""M\n\x16MsgCreateDenomResponse\x123\n\x0fnew_token_denom\x18\x01 \x01(\tB\x1a\xf2\xde\x1f\x16yaml:"new_token_denom""\xa1\x01\n\x07MsgMint\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12@\n\x06amount\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x15\xf2\xde\x1f\ryaml:"amount"\xc8\xde\x1f\x00\x121\n\rmintToAddress\x18\x03 \x01(\tB\x1a\xf2\xde\x1f\x16yaml:"mint_to_address""\x11\n\x0fMsgMintResponse"\xa5\x01\n\x07MsgBurn\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12@\n\x06amount\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x15\xf2\xde\x1f\ryaml:"amount"\xc8\xde\x1f\x00\x125\n\x0fburnFromAddress\x18\x03 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"burn_from_address""\x11\n\x0fMsgBurnResponse"|\n\x0eMsgChangeAdmin\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12\x1f\n\x05denom\x18\x02 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"denom"\x12&\n\x08newAdmin\x18\x03 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"new_admin""\x18\n\x16MsgChangeAdminResponse2\xa7\x03\n\x03Msg\x12q\n\x0bCreateDenom\x12,.osmosis.tokenfactory.v1beta1.MsgCreateDenom\x1a4.osmosis.tokenfactory.v1beta1.MsgCreateDenomResponse\x12\\\n\x04Mint\x12%.osmosis.tokenfactory.v1beta1.MsgMint\x1a-.osmosis.tokenfactory.v1beta1.MsgMintResponse\x12\\\n\x04Burn\x12%.osmosis.tokenfactory.v1beta1.MsgBurn\x1a-.osmosis.tokenfactory.v1beta1.MsgBurnResponse\x12q\n\x0bChangeAdmin\x12,.osmosis.tokenfactory.v1beta1.MsgChangeAdmin\x1a4.osmosis.tokenfactory.v1beta1.MsgChangeAdminResponseB9Z7github.com/osmosis-labs/osmosis/v7/x/tokenfactory/typesb\x06proto3')
_MSGCREATEDENOM = DESCRIPTOR.message_types_by_name['MsgCreateDenom']
_MSGCREATEDENOMRESPONSE = DESCRIPTOR.message_types_by_name['MsgCreateDenomResponse']
_MSGMINT = DESCRIPTOR.message_types_by_name['MsgMint']
_MSGMINTRESPONSE = DESCRIPTOR.message_types_by_name['MsgMintResponse']
_MSGBURN = DESCRIPTOR.message_types_by_name['MsgBurn']
_MSGBURNRESPONSE = DESCRIPTOR.message_types_by_name['MsgBurnResponse']
_MSGCHANGEADMIN = DESCRIPTOR.message_types_by_name['MsgChangeAdmin']
_MSGCHANGEADMINRESPONSE = DESCRIPTOR.message_types_by_name['MsgChangeAdminResponse']
MsgCreateDenom = _reflection.GeneratedProtocolMessageType('MsgCreateDenom', (_message.Message,), {'DESCRIPTOR': _MSGCREATEDENOM, '__module__': 'osmosis.tokenfactory.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgCreateDenom)
MsgCreateDenomResponse = _reflection.GeneratedProtocolMessageType('MsgCreateDenomResponse', (_message.Message,), {'DESCRIPTOR': _MSGCREATEDENOMRESPONSE, '__module__': 'osmosis.tokenfactory.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgCreateDenomResponse)
MsgMint = _reflection.GeneratedProtocolMessageType('MsgMint', (_message.Message,), {'DESCRIPTOR': _MSGMINT, '__module__': 'osmosis.tokenfactory.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgMint)
MsgMintResponse = _reflection.GeneratedProtocolMessageType('MsgMintResponse', (_message.Message,), {'DESCRIPTOR': _MSGMINTRESPONSE, '__module__': 'osmosis.tokenfactory.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgMintResponse)
MsgBurn = _reflection.GeneratedProtocolMessageType('MsgBurn', (_message.Message,), {'DESCRIPTOR': _MSGBURN, '__module__': 'osmosis.tokenfactory.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgBurn)
MsgBurnResponse = _reflection.GeneratedProtocolMessageType('MsgBurnResponse', (_message.Message,), {'DESCRIPTOR': _MSGBURNRESPONSE, '__module__': 'osmosis.tokenfactory.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgBurnResponse)
MsgChangeAdmin = _reflection.GeneratedProtocolMessageType('MsgChangeAdmin', (_message.Message,), {'DESCRIPTOR': _MSGCHANGEADMIN, '__module__': 'osmosis.tokenfactory.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgChangeAdmin)
MsgChangeAdminResponse = _reflection.GeneratedProtocolMessageType('MsgChangeAdminResponse', (_message.Message,), {'DESCRIPTOR': _MSGCHANGEADMINRESPONSE, '__module__': 'osmosis.tokenfactory.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgChangeAdminResponse)
_MSG = DESCRIPTOR.services_by_name['Msg']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z7github.com/osmosis-labs/osmosis/v7/x/tokenfactory/types'
    _MSGCREATEDENOM.fields_by_name['sender']._options = None
    _MSGCREATEDENOM.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGCREATEDENOM.fields_by_name['nonce']._options = None
    _MSGCREATEDENOM.fields_by_name['nonce']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"nonce"'
    _MSGCREATEDENOMRESPONSE.fields_by_name['new_token_denom']._options = None
    _MSGCREATEDENOMRESPONSE.fields_by_name['new_token_denom']._serialized_options = b'\xf2\xde\x1f\x16yaml:"new_token_denom"'
    _MSGMINT.fields_by_name['sender']._options = None
    _MSGMINT.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGMINT.fields_by_name['amount']._options = None
    _MSGMINT.fields_by_name['amount']._serialized_options = b'\xf2\xde\x1f\ryaml:"amount"\xc8\xde\x1f\x00'
    _MSGMINT.fields_by_name['mintToAddress']._options = None
    _MSGMINT.fields_by_name['mintToAddress']._serialized_options = b'\xf2\xde\x1f\x16yaml:"mint_to_address"'
    _MSGBURN.fields_by_name['sender']._options = None
    _MSGBURN.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGBURN.fields_by_name['amount']._options = None
    _MSGBURN.fields_by_name['amount']._serialized_options = b'\xf2\xde\x1f\ryaml:"amount"\xc8\xde\x1f\x00'
    _MSGBURN.fields_by_name['burnFromAddress']._options = None
    _MSGBURN.fields_by_name['burnFromAddress']._serialized_options = b'\xf2\xde\x1f\x18yaml:"burn_from_address"'
    _MSGCHANGEADMIN.fields_by_name['sender']._options = None
    _MSGCHANGEADMIN.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGCHANGEADMIN.fields_by_name['denom']._options = None
    _MSGCHANGEADMIN.fields_by_name['denom']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"denom"'
    _MSGCHANGEADMIN.fields_by_name['newAdmin']._options = None
    _MSGCHANGEADMIN.fields_by_name['newAdmin']._serialized_options = b'\xf2\xde\x1f\x10yaml:"new_admin"'
    _MSGCREATEDENOM._serialized_start = 125
    _MSGCREATEDENOM._serialized_end = 209
    _MSGCREATEDENOMRESPONSE._serialized_start = 211
    _MSGCREATEDENOMRESPONSE._serialized_end = 288
    _MSGMINT._serialized_start = 291
    _MSGMINT._serialized_end = 452
    _MSGMINTRESPONSE._serialized_start = 454
    _MSGMINTRESPONSE._serialized_end = 471
    _MSGBURN._serialized_start = 474
    _MSGBURN._serialized_end = 639
    _MSGBURNRESPONSE._serialized_start = 641
    _MSGBURNRESPONSE._serialized_end = 658
    _MSGCHANGEADMIN._serialized_start = 660
    _MSGCHANGEADMIN._serialized_end = 784
    _MSGCHANGEADMINRESPONSE._serialized_start = 786
    _MSGCHANGEADMINRESPONSE._serialized_end = 810
    _MSG._serialized_start = 813
    _MSG._serialized_end = 1236
