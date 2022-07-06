
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.crypto.multisig.v1beta1 import multisig_pb2 as cosmos_dot_crypto_dot_multisig_dot_v1beta1_dot_multisig__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.tx.signing.v1beta1 import signing_pb2 as cosmos_dot_tx_dot_signing_dot_v1beta1_dot_signing__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1acosmos/tx/v1beta1/tx.proto\x12\x11cosmos.tx.v1beta1\x1a\x14gogoproto/gogo.proto\x1a-cosmos/crypto/multisig/v1beta1/multisig.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\'cosmos/tx/signing/v1beta1/signing.proto\x1a\x19google/protobuf/any.proto\x1a\x19cosmos_proto/cosmos.proto"q\n\x02Tx\x12\'\n\x04body\x18\x01 \x01(\x0b2\x19.cosmos.tx.v1beta1.TxBody\x12.\n\tauth_info\x18\x02 \x01(\x0b2\x1b.cosmos.tx.v1beta1.AuthInfo\x12\x12\n\nsignatures\x18\x03 \x03(\x0c"H\n\x05TxRaw\x12\x12\n\nbody_bytes\x18\x01 \x01(\x0c\x12\x17\n\x0fauth_info_bytes\x18\x02 \x01(\x0c\x12\x12\n\nsignatures\x18\x03 \x03(\x0c"`\n\x07SignDoc\x12\x12\n\nbody_bytes\x18\x01 \x01(\x0c\x12\x17\n\x0fauth_info_bytes\x18\x02 \x01(\x0c\x12\x10\n\x08chain_id\x18\x03 \x01(\t\x12\x16\n\x0eaccount_number\x18\x04 \x01(\x04"\xb1\x01\n\x10SignDocDirectAux\x12\x12\n\nbody_bytes\x18\x01 \x01(\x0c\x12(\n\npublic_key\x18\x02 \x01(\x0b2\x14.google.protobuf.Any\x12\x10\n\x08chain_id\x18\x03 \x01(\t\x12\x16\n\x0eaccount_number\x18\x04 \x01(\x04\x12\x10\n\x08sequence\x18\x05 \x01(\x04\x12#\n\x03tip\x18\x06 \x01(\x0b2\x16.cosmos.tx.v1beta1.Tip"\xc7\x01\n\x06TxBody\x12&\n\x08messages\x18\x01 \x03(\x0b2\x14.google.protobuf.Any\x12\x0c\n\x04memo\x18\x02 \x01(\t\x12\x16\n\x0etimeout_height\x18\x03 \x01(\x04\x120\n\x11extension_options\x18\xff\x07 \x03(\x0b2\x14.google.protobuf.Any\x12=\n\x1enon_critical_extension_options\x18\xff\x0f \x03(\x0b2\x14.google.protobuf.Any"\x89\x01\n\x08AuthInfo\x123\n\x0csigner_infos\x18\x01 \x03(\x0b2\x1d.cosmos.tx.v1beta1.SignerInfo\x12#\n\x03fee\x18\x02 \x01(\x0b2\x16.cosmos.tx.v1beta1.Fee\x12#\n\x03tip\x18\x03 \x01(\x0b2\x16.cosmos.tx.v1beta1.Tip"x\n\nSignerInfo\x12(\n\npublic_key\x18\x01 \x01(\x0b2\x14.google.protobuf.Any\x12.\n\tmode_info\x18\x02 \x01(\x0b2\x1b.cosmos.tx.v1beta1.ModeInfo\x12\x10\n\x08sequence\x18\x03 \x01(\x04"\xb5\x02\n\x08ModeInfo\x124\n\x06single\x18\x01 \x01(\x0b2".cosmos.tx.v1beta1.ModeInfo.SingleH\x00\x122\n\x05multi\x18\x02 \x01(\x0b2!.cosmos.tx.v1beta1.ModeInfo.MultiH\x00\x1a;\n\x06Single\x121\n\x04mode\x18\x01 \x01(\x0e2#.cosmos.tx.signing.v1beta1.SignMode\x1a{\n\x05Multi\x12A\n\x08bitarray\x18\x01 \x01(\x0b2/.cosmos.crypto.multisig.v1beta1.CompactBitArray\x12/\n\nmode_infos\x18\x02 \x03(\x0b2\x1b.cosmos.tx.v1beta1.ModeInfoB\x05\n\x03sum"\xc9\x01\n\x03Fee\x12[\n\x06amount\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12\x11\n\tgas_limit\x18\x02 \x01(\x04\x12\'\n\x05payer\x18\x03 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12)\n\x07granter\x18\x04 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString"\x8c\x01\n\x03Tip\x12[\n\x06amount\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12(\n\x06tipper\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString"\xb1\x01\n\rAuxSignerData\x12)\n\x07address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x125\n\x08sign_doc\x18\x02 \x01(\x0b2#.cosmos.tx.v1beta1.SignDocDirectAux\x121\n\x04mode\x18\x03 \x01(\x0e2#.cosmos.tx.signing.v1beta1.SignMode\x12\x0b\n\x03sig\x18\x04 \x01(\x0cB\'Z%github.com/cosmos/cosmos-sdk/types/txb\x06proto3')
_TX = DESCRIPTOR.message_types_by_name['Tx']
_TXRAW = DESCRIPTOR.message_types_by_name['TxRaw']
_SIGNDOC = DESCRIPTOR.message_types_by_name['SignDoc']
_SIGNDOCDIRECTAUX = DESCRIPTOR.message_types_by_name['SignDocDirectAux']
_TXBODY = DESCRIPTOR.message_types_by_name['TxBody']
_AUTHINFO = DESCRIPTOR.message_types_by_name['AuthInfo']
_SIGNERINFO = DESCRIPTOR.message_types_by_name['SignerInfo']
_MODEINFO = DESCRIPTOR.message_types_by_name['ModeInfo']
_MODEINFO_SINGLE = _MODEINFO.nested_types_by_name['Single']
_MODEINFO_MULTI = _MODEINFO.nested_types_by_name['Multi']
_FEE = DESCRIPTOR.message_types_by_name['Fee']
_TIP = DESCRIPTOR.message_types_by_name['Tip']
_AUXSIGNERDATA = DESCRIPTOR.message_types_by_name['AuxSignerData']
Tx = _reflection.GeneratedProtocolMessageType('Tx', (_message.Message,), {'DESCRIPTOR': _TX, '__module__': 'cosmos.tx.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(Tx)
TxRaw = _reflection.GeneratedProtocolMessageType('TxRaw', (_message.Message,), {'DESCRIPTOR': _TXRAW, '__module__': 'cosmos.tx.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(TxRaw)
SignDoc = _reflection.GeneratedProtocolMessageType('SignDoc', (_message.Message,), {'DESCRIPTOR': _SIGNDOC, '__module__': 'cosmos.tx.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(SignDoc)
SignDocDirectAux = _reflection.GeneratedProtocolMessageType('SignDocDirectAux', (_message.Message,), {'DESCRIPTOR': _SIGNDOCDIRECTAUX, '__module__': 'cosmos.tx.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(SignDocDirectAux)
TxBody = _reflection.GeneratedProtocolMessageType('TxBody', (_message.Message,), {'DESCRIPTOR': _TXBODY, '__module__': 'cosmos.tx.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(TxBody)
AuthInfo = _reflection.GeneratedProtocolMessageType('AuthInfo', (_message.Message,), {'DESCRIPTOR': _AUTHINFO, '__module__': 'cosmos.tx.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(AuthInfo)
SignerInfo = _reflection.GeneratedProtocolMessageType('SignerInfo', (_message.Message,), {'DESCRIPTOR': _SIGNERINFO, '__module__': 'cosmos.tx.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(SignerInfo)
ModeInfo = _reflection.GeneratedProtocolMessageType('ModeInfo', (_message.Message,), {'Single': _reflection.GeneratedProtocolMessageType('Single', (_message.Message,), {'DESCRIPTOR': _MODEINFO_SINGLE, '__module__': 'cosmos.tx.v1beta1.tx_pb2'}), 'Multi': _reflection.GeneratedProtocolMessageType('Multi', (_message.Message,), {'DESCRIPTOR': _MODEINFO_MULTI, '__module__': 'cosmos.tx.v1beta1.tx_pb2'}), 'DESCRIPTOR': _MODEINFO, '__module__': 'cosmos.tx.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(ModeInfo)
_sym_db.RegisterMessage(ModeInfo.Single)
_sym_db.RegisterMessage(ModeInfo.Multi)
Fee = _reflection.GeneratedProtocolMessageType('Fee', (_message.Message,), {'DESCRIPTOR': _FEE, '__module__': 'cosmos.tx.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(Fee)
Tip = _reflection.GeneratedProtocolMessageType('Tip', (_message.Message,), {'DESCRIPTOR': _TIP, '__module__': 'cosmos.tx.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(Tip)
AuxSignerData = _reflection.GeneratedProtocolMessageType('AuxSignerData', (_message.Message,), {'DESCRIPTOR': _AUXSIGNERDATA, '__module__': 'cosmos.tx.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(AuxSignerData)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z%github.com/cosmos/cosmos-sdk/types/tx'
    _FEE.fields_by_name['amount']._options = None
    _FEE.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _FEE.fields_by_name['payer']._options = None
    _FEE.fields_by_name['payer']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _FEE.fields_by_name['granter']._options = None
    _FEE.fields_by_name['granter']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _TIP.fields_by_name['amount']._options = None
    _TIP.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _TIP.fields_by_name['tipper']._options = None
    _TIP.fields_by_name['tipper']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _AUXSIGNERDATA.fields_by_name['address']._options = None
    _AUXSIGNERDATA.fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _TX._serialized_start = 245
    _TX._serialized_end = 358
    _TXRAW._serialized_start = 360
    _TXRAW._serialized_end = 432
    _SIGNDOC._serialized_start = 434
    _SIGNDOC._serialized_end = 530
    _SIGNDOCDIRECTAUX._serialized_start = 533
    _SIGNDOCDIRECTAUX._serialized_end = 710
    _TXBODY._serialized_start = 713
    _TXBODY._serialized_end = 912
    _AUTHINFO._serialized_start = 915
    _AUTHINFO._serialized_end = 1052
    _SIGNERINFO._serialized_start = 1054
    _SIGNERINFO._serialized_end = 1174
    _MODEINFO._serialized_start = 1177
    _MODEINFO._serialized_end = 1486
    _MODEINFO_SINGLE._serialized_start = 1295
    _MODEINFO_SINGLE._serialized_end = 1354
    _MODEINFO_MULTI._serialized_start = 1356
    _MODEINFO_MULTI._serialized_end = 1479
    _FEE._serialized_start = 1489
    _FEE._serialized_end = 1690
    _TIP._serialized_start = 1693
    _TIP._serialized_end = 1833
    _AUXSIGNERDATA._serialized_start = 1836
    _AUXSIGNERDATA._serialized_end = 2013
