
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!bitsong/fantoken/v1beta1/tx.proto\x12\x10bitsong.fantoken\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto"\xba\x01\n\x08MsgIssue\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12W\n\nmax_supply\x18\x03 \x01(\tBC\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x11yaml:"max_supply"\xc8\xde\x1f\x00\x12\x11\n\tauthority\x18\x04 \x01(\t\x12\x0e\n\x06minter\x18\x05 \x01(\t\x12\x14\n\x03uri\x18\x06 \x01(\tB\x07\xe2\xde\x1f\x03URI"\x12\n\x10MsgIssueResponse"/\n\x0eMsgDisableMint\x12\r\n\x05denom\x18\x01 \x01(\t\x12\x0e\n\x06minter\x18\x02 \x01(\t"\x18\n\x16MsgDisableMintResponse"j\n\x07MsgMint\x12\x11\n\trecipient\x18\x01 \x01(\t\x12<\n\x04coin\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x13\xf2\xde\x1f\x0byaml:"coin"\xc8\xde\x1f\x00\x12\x0e\n\x06minter\x18\x03 \x01(\t"\x11\n\x0fMsgMintResponse"W\n\x07MsgBurn\x12<\n\x04coin\x18\x01 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x13\xf2\xde\x1f\x0byaml:"coin"\xc8\xde\x1f\x00\x12\x0e\n\x06sender\x18\x02 \x01(\t"\x11\n\x0fMsgBurnResponse"s\n\x0cMsgSetMinter\x12\r\n\x05denom\x18\x01 \x01(\t\x12)\n\nold_minter\x18\x02 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"old_minter"\x12)\n\nnew_minter\x18\x03 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"new_minter""\x16\n\x14MsgSetMinterResponse"\x82\x01\n\x0fMsgSetAuthority\x12\r\n\x05denom\x18\x01 \x01(\t\x12/\n\rold_authority\x18\x02 \x01(\tB\x18\xf2\xde\x1f\x14yaml:"old_authority"\x12/\n\rnew_authority\x18\x03 \x01(\tB\x18\xf2\xde\x1f\x14yaml:"new_authority""\x19\n\x17MsgSetAuthorityResponse"C\n\tMsgSetUri\x12\x11\n\tauthority\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t\x12\x14\n\x03uri\x18\x03 \x01(\tB\x07\xe2\xde\x1f\x03URI"\x13\n\x11MsgSetUriResponse2\xb4\x04\n\x03Msg\x12G\n\x05Issue\x12\x1a.bitsong.fantoken.MsgIssue\x1a".bitsong.fantoken.MsgIssueResponse\x12D\n\x04Mint\x12\x19.bitsong.fantoken.MsgMint\x1a!.bitsong.fantoken.MsgMintResponse\x12D\n\x04Burn\x12\x19.bitsong.fantoken.MsgBurn\x1a!.bitsong.fantoken.MsgBurnResponse\x12Y\n\x0bDisableMint\x12 .bitsong.fantoken.MsgDisableMint\x1a(.bitsong.fantoken.MsgDisableMintResponse\x12S\n\tSetMinter\x12\x1e.bitsong.fantoken.MsgSetMinter\x1a&.bitsong.fantoken.MsgSetMinterResponse\x12\\\n\x0cSetAuthority\x12!.bitsong.fantoken.MsgSetAuthority\x1a).bitsong.fantoken.MsgSetAuthorityResponse\x12J\n\x06SetUri\x12\x1b.bitsong.fantoken.MsgSetUri\x1a#.bitsong.fantoken.MsgSetUriResponseB<Z6github.com/bitsongofficial/go-bitsong/x/fantoken/types\xc8\xe1\x1e\x00b\x06proto3')
_MSGISSUE = DESCRIPTOR.message_types_by_name['MsgIssue']
_MSGISSUERESPONSE = DESCRIPTOR.message_types_by_name['MsgIssueResponse']
_MSGDISABLEMINT = DESCRIPTOR.message_types_by_name['MsgDisableMint']
_MSGDISABLEMINTRESPONSE = DESCRIPTOR.message_types_by_name['MsgDisableMintResponse']
_MSGMINT = DESCRIPTOR.message_types_by_name['MsgMint']
_MSGMINTRESPONSE = DESCRIPTOR.message_types_by_name['MsgMintResponse']
_MSGBURN = DESCRIPTOR.message_types_by_name['MsgBurn']
_MSGBURNRESPONSE = DESCRIPTOR.message_types_by_name['MsgBurnResponse']
_MSGSETMINTER = DESCRIPTOR.message_types_by_name['MsgSetMinter']
_MSGSETMINTERRESPONSE = DESCRIPTOR.message_types_by_name['MsgSetMinterResponse']
_MSGSETAUTHORITY = DESCRIPTOR.message_types_by_name['MsgSetAuthority']
_MSGSETAUTHORITYRESPONSE = DESCRIPTOR.message_types_by_name['MsgSetAuthorityResponse']
_MSGSETURI = DESCRIPTOR.message_types_by_name['MsgSetUri']
_MSGSETURIRESPONSE = DESCRIPTOR.message_types_by_name['MsgSetUriResponse']
MsgIssue = _reflection.GeneratedProtocolMessageType('MsgIssue', (_message.Message,), {'DESCRIPTOR': _MSGISSUE, '__module__': 'bitsong.fantoken.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgIssue)
MsgIssueResponse = _reflection.GeneratedProtocolMessageType('MsgIssueResponse', (_message.Message,), {'DESCRIPTOR': _MSGISSUERESPONSE, '__module__': 'bitsong.fantoken.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgIssueResponse)
MsgDisableMint = _reflection.GeneratedProtocolMessageType('MsgDisableMint', (_message.Message,), {'DESCRIPTOR': _MSGDISABLEMINT, '__module__': 'bitsong.fantoken.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgDisableMint)
MsgDisableMintResponse = _reflection.GeneratedProtocolMessageType('MsgDisableMintResponse', (_message.Message,), {'DESCRIPTOR': _MSGDISABLEMINTRESPONSE, '__module__': 'bitsong.fantoken.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgDisableMintResponse)
MsgMint = _reflection.GeneratedProtocolMessageType('MsgMint', (_message.Message,), {'DESCRIPTOR': _MSGMINT, '__module__': 'bitsong.fantoken.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgMint)
MsgMintResponse = _reflection.GeneratedProtocolMessageType('MsgMintResponse', (_message.Message,), {'DESCRIPTOR': _MSGMINTRESPONSE, '__module__': 'bitsong.fantoken.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgMintResponse)
MsgBurn = _reflection.GeneratedProtocolMessageType('MsgBurn', (_message.Message,), {'DESCRIPTOR': _MSGBURN, '__module__': 'bitsong.fantoken.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgBurn)
MsgBurnResponse = _reflection.GeneratedProtocolMessageType('MsgBurnResponse', (_message.Message,), {'DESCRIPTOR': _MSGBURNRESPONSE, '__module__': 'bitsong.fantoken.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgBurnResponse)
MsgSetMinter = _reflection.GeneratedProtocolMessageType('MsgSetMinter', (_message.Message,), {'DESCRIPTOR': _MSGSETMINTER, '__module__': 'bitsong.fantoken.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgSetMinter)
MsgSetMinterResponse = _reflection.GeneratedProtocolMessageType('MsgSetMinterResponse', (_message.Message,), {'DESCRIPTOR': _MSGSETMINTERRESPONSE, '__module__': 'bitsong.fantoken.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgSetMinterResponse)
MsgSetAuthority = _reflection.GeneratedProtocolMessageType('MsgSetAuthority', (_message.Message,), {'DESCRIPTOR': _MSGSETAUTHORITY, '__module__': 'bitsong.fantoken.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgSetAuthority)
MsgSetAuthorityResponse = _reflection.GeneratedProtocolMessageType('MsgSetAuthorityResponse', (_message.Message,), {'DESCRIPTOR': _MSGSETAUTHORITYRESPONSE, '__module__': 'bitsong.fantoken.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgSetAuthorityResponse)
MsgSetUri = _reflection.GeneratedProtocolMessageType('MsgSetUri', (_message.Message,), {'DESCRIPTOR': _MSGSETURI, '__module__': 'bitsong.fantoken.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgSetUri)
MsgSetUriResponse = _reflection.GeneratedProtocolMessageType('MsgSetUriResponse', (_message.Message,), {'DESCRIPTOR': _MSGSETURIRESPONSE, '__module__': 'bitsong.fantoken.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgSetUriResponse)
_MSG = DESCRIPTOR.services_by_name['Msg']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/bitsongofficial/go-bitsong/x/fantoken/types\xc8\xe1\x1e\x00'
    _MSGISSUE.fields_by_name['max_supply']._options = None
    _MSGISSUE.fields_by_name['max_supply']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x11yaml:"max_supply"\xc8\xde\x1f\x00'
    _MSGISSUE.fields_by_name['uri']._options = None
    _MSGISSUE.fields_by_name['uri']._serialized_options = b'\xe2\xde\x1f\x03URI'
    _MSGMINT.fields_by_name['coin']._options = None
    _MSGMINT.fields_by_name['coin']._serialized_options = b'\xf2\xde\x1f\x0byaml:"coin"\xc8\xde\x1f\x00'
    _MSGBURN.fields_by_name['coin']._options = None
    _MSGBURN.fields_by_name['coin']._serialized_options = b'\xf2\xde\x1f\x0byaml:"coin"\xc8\xde\x1f\x00'
    _MSGSETMINTER.fields_by_name['old_minter']._options = None
    _MSGSETMINTER.fields_by_name['old_minter']._serialized_options = b'\xf2\xde\x1f\x11yaml:"old_minter"'
    _MSGSETMINTER.fields_by_name['new_minter']._options = None
    _MSGSETMINTER.fields_by_name['new_minter']._serialized_options = b'\xf2\xde\x1f\x11yaml:"new_minter"'
    _MSGSETAUTHORITY.fields_by_name['old_authority']._options = None
    _MSGSETAUTHORITY.fields_by_name['old_authority']._serialized_options = b'\xf2\xde\x1f\x14yaml:"old_authority"'
    _MSGSETAUTHORITY.fields_by_name['new_authority']._options = None
    _MSGSETAUTHORITY.fields_by_name['new_authority']._serialized_options = b'\xf2\xde\x1f\x14yaml:"new_authority"'
    _MSGSETURI.fields_by_name['uri']._options = None
    _MSGSETURI.fields_by_name['uri']._serialized_options = b'\xe2\xde\x1f\x03URI'
    _MSGISSUE._serialized_start = 110
    _MSGISSUE._serialized_end = 296
    _MSGISSUERESPONSE._serialized_start = 298
    _MSGISSUERESPONSE._serialized_end = 316
    _MSGDISABLEMINT._serialized_start = 318
    _MSGDISABLEMINT._serialized_end = 365
    _MSGDISABLEMINTRESPONSE._serialized_start = 367
    _MSGDISABLEMINTRESPONSE._serialized_end = 391
    _MSGMINT._serialized_start = 393
    _MSGMINT._serialized_end = 499
    _MSGMINTRESPONSE._serialized_start = 501
    _MSGMINTRESPONSE._serialized_end = 518
    _MSGBURN._serialized_start = 520
    _MSGBURN._serialized_end = 607
    _MSGBURNRESPONSE._serialized_start = 609
    _MSGBURNRESPONSE._serialized_end = 626
    _MSGSETMINTER._serialized_start = 628
    _MSGSETMINTER._serialized_end = 743
    _MSGSETMINTERRESPONSE._serialized_start = 745
    _MSGSETMINTERRESPONSE._serialized_end = 767
    _MSGSETAUTHORITY._serialized_start = 770
    _MSGSETAUTHORITY._serialized_end = 900
    _MSGSETAUTHORITYRESPONSE._serialized_start = 902
    _MSGSETAUTHORITYRESPONSE._serialized_end = 927
    _MSGSETURI._serialized_start = 929
    _MSGSETURI._serialized_end = 996
    _MSGSETURIRESPONSE._serialized_start = 998
    _MSGSETURIRESPONSE._serialized_end = 1017
    _MSG._serialized_start = 1020
    _MSG._serialized_end = 1584
