
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.staking.v1beta1 import staking_pb2 as cosmos_dot_staking_dot_v1beta1_dot_staking__pb2
from ....cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fcosmos/staking/v1beta1/tx.proto\x12\x16cosmos.staking.v1beta1\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x14gogoproto/gogo.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a$cosmos/staking/v1beta1/staking.proto\x1a\x17cosmos/msg/v1/msg.proto"\x82\x04\n\x12MsgCreateValidator\x12>\n\x0bdescription\x18\x01 \x01(\x0b2#.cosmos.staking.v1beta1.DescriptionB\x04\xc8\xde\x1f\x00\x12A\n\ncommission\x18\x02 \x01(\x0b2\'.cosmos.staking.v1beta1.CommissionRatesB\x04\xc8\xde\x1f\x00\x12Y\n\x13min_self_delegation\x18\x03 \x01(\tB<\xd2\xb4-\ncosmos.Int\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x123\n\x11delegator_address\x18\x04 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x123\n\x11validator_address\x18\x05 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12>\n\x06pubkey\x18\x06 \x01(\x0b2\x14.google.protobuf.AnyB\x18\xca\xb4-\x14cosmos.crypto.PubKey\x12.\n\x05value\x18\x07 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00:4\x82\xe7\xb0*\x11delegator_address\x82\xe7\xb0*\x11validator_address\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\x1c\n\x1aMsgCreateValidatorResponse"\xd1\x02\n\x10MsgEditValidator\x12>\n\x0bdescription\x18\x01 \x01(\x0b2#.cosmos.staking.v1beta1.DescriptionB\x04\xc8\xde\x1f\x00\x123\n\x11validator_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12Q\n\x0fcommission_rate\x18\x03 \x01(\tB8\xd2\xb4-\ncosmos.Dec\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12U\n\x13min_self_delegation\x18\x04 \x01(\tB8\xd2\xb4-\ncosmos.Int\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int:\x1e\x82\xe7\xb0*\x11validator_address\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\x1a\n\x18MsgEditValidatorResponse"\xc8\x01\n\x0bMsgDelegate\x123\n\x11delegator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x123\n\x11validator_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12/\n\x06amount\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00:\x1e\x82\xe7\xb0*\x11delegator_address\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\x15\n\x13MsgDelegateResponse"\x8c\x02\n\x12MsgBeginRedelegate\x123\n\x11delegator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x127\n\x15validator_src_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x127\n\x15validator_dst_address\x18\x03 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12/\n\x06amount\x18\x04 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00:\x1e\x82\xe7\xb0*\x11delegator_address\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"[\n\x1aMsgBeginRedelegateResponse\x12=\n\x0fcompletion_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01"\xca\x01\n\rMsgUndelegate\x123\n\x11delegator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x123\n\x11validator_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12/\n\x06amount\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00:\x1e\x82\xe7\xb0*\x11delegator_address\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"V\n\x15MsgUndelegateResponse\x12=\n\x0fcompletion_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01"\xf2\x01\n\x1cMsgCancelUnbondingDelegation\x123\n\x11delegator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x123\n\x11validator_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12/\n\x06amount\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x17\n\x0fcreation_height\x18\x04 \x01(\x03:\x1e\x82\xe7\xb0*\x11delegator_address\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"&\n$MsgCancelUnbondingDelegationResponse2\xac\x05\n\x03Msg\x12q\n\x0fCreateValidator\x12*.cosmos.staking.v1beta1.MsgCreateValidator\x1a2.cosmos.staking.v1beta1.MsgCreateValidatorResponse\x12k\n\rEditValidator\x12(.cosmos.staking.v1beta1.MsgEditValidator\x1a0.cosmos.staking.v1beta1.MsgEditValidatorResponse\x12\\\n\x08Delegate\x12#.cosmos.staking.v1beta1.MsgDelegate\x1a+.cosmos.staking.v1beta1.MsgDelegateResponse\x12q\n\x0fBeginRedelegate\x12*.cosmos.staking.v1beta1.MsgBeginRedelegate\x1a2.cosmos.staking.v1beta1.MsgBeginRedelegateResponse\x12b\n\nUndelegate\x12%.cosmos.staking.v1beta1.MsgUndelegate\x1a-.cosmos.staking.v1beta1.MsgUndelegateResponse\x12\x8f\x01\n\x19CancelUnbondingDelegation\x124.cosmos.staking.v1beta1.MsgCancelUnbondingDelegation\x1a<.cosmos.staking.v1beta1.MsgCancelUnbondingDelegationResponseB.Z,github.com/cosmos/cosmos-sdk/x/staking/typesb\x06proto3')
_MSGCREATEVALIDATOR = DESCRIPTOR.message_types_by_name['MsgCreateValidator']
_MSGCREATEVALIDATORRESPONSE = DESCRIPTOR.message_types_by_name['MsgCreateValidatorResponse']
_MSGEDITVALIDATOR = DESCRIPTOR.message_types_by_name['MsgEditValidator']
_MSGEDITVALIDATORRESPONSE = DESCRIPTOR.message_types_by_name['MsgEditValidatorResponse']
_MSGDELEGATE = DESCRIPTOR.message_types_by_name['MsgDelegate']
_MSGDELEGATERESPONSE = DESCRIPTOR.message_types_by_name['MsgDelegateResponse']
_MSGBEGINREDELEGATE = DESCRIPTOR.message_types_by_name['MsgBeginRedelegate']
_MSGBEGINREDELEGATERESPONSE = DESCRIPTOR.message_types_by_name['MsgBeginRedelegateResponse']
_MSGUNDELEGATE = DESCRIPTOR.message_types_by_name['MsgUndelegate']
_MSGUNDELEGATERESPONSE = DESCRIPTOR.message_types_by_name['MsgUndelegateResponse']
_MSGCANCELUNBONDINGDELEGATION = DESCRIPTOR.message_types_by_name['MsgCancelUnbondingDelegation']
_MSGCANCELUNBONDINGDELEGATIONRESPONSE = DESCRIPTOR.message_types_by_name['MsgCancelUnbondingDelegationResponse']
MsgCreateValidator = _reflection.GeneratedProtocolMessageType('MsgCreateValidator', (_message.Message,), {'DESCRIPTOR': _MSGCREATEVALIDATOR, '__module__': 'cosmos.staking.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgCreateValidator)
MsgCreateValidatorResponse = _reflection.GeneratedProtocolMessageType('MsgCreateValidatorResponse', (_message.Message,), {'DESCRIPTOR': _MSGCREATEVALIDATORRESPONSE, '__module__': 'cosmos.staking.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgCreateValidatorResponse)
MsgEditValidator = _reflection.GeneratedProtocolMessageType('MsgEditValidator', (_message.Message,), {'DESCRIPTOR': _MSGEDITVALIDATOR, '__module__': 'cosmos.staking.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgEditValidator)
MsgEditValidatorResponse = _reflection.GeneratedProtocolMessageType('MsgEditValidatorResponse', (_message.Message,), {'DESCRIPTOR': _MSGEDITVALIDATORRESPONSE, '__module__': 'cosmos.staking.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgEditValidatorResponse)
MsgDelegate = _reflection.GeneratedProtocolMessageType('MsgDelegate', (_message.Message,), {'DESCRIPTOR': _MSGDELEGATE, '__module__': 'cosmos.staking.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgDelegate)
MsgDelegateResponse = _reflection.GeneratedProtocolMessageType('MsgDelegateResponse', (_message.Message,), {'DESCRIPTOR': _MSGDELEGATERESPONSE, '__module__': 'cosmos.staking.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgDelegateResponse)
MsgBeginRedelegate = _reflection.GeneratedProtocolMessageType('MsgBeginRedelegate', (_message.Message,), {'DESCRIPTOR': _MSGBEGINREDELEGATE, '__module__': 'cosmos.staking.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgBeginRedelegate)
MsgBeginRedelegateResponse = _reflection.GeneratedProtocolMessageType('MsgBeginRedelegateResponse', (_message.Message,), {'DESCRIPTOR': _MSGBEGINREDELEGATERESPONSE, '__module__': 'cosmos.staking.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgBeginRedelegateResponse)
MsgUndelegate = _reflection.GeneratedProtocolMessageType('MsgUndelegate', (_message.Message,), {'DESCRIPTOR': _MSGUNDELEGATE, '__module__': 'cosmos.staking.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgUndelegate)
MsgUndelegateResponse = _reflection.GeneratedProtocolMessageType('MsgUndelegateResponse', (_message.Message,), {'DESCRIPTOR': _MSGUNDELEGATERESPONSE, '__module__': 'cosmos.staking.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgUndelegateResponse)
MsgCancelUnbondingDelegation = _reflection.GeneratedProtocolMessageType('MsgCancelUnbondingDelegation', (_message.Message,), {'DESCRIPTOR': _MSGCANCELUNBONDINGDELEGATION, '__module__': 'cosmos.staking.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgCancelUnbondingDelegation)
MsgCancelUnbondingDelegationResponse = _reflection.GeneratedProtocolMessageType('MsgCancelUnbondingDelegationResponse', (_message.Message,), {'DESCRIPTOR': _MSGCANCELUNBONDINGDELEGATIONRESPONSE, '__module__': 'cosmos.staking.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgCancelUnbondingDelegationResponse)
_MSG = DESCRIPTOR.services_by_name['Msg']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z,github.com/cosmos/cosmos-sdk/x/staking/types'
    _MSGCREATEVALIDATOR.fields_by_name['description']._options = None
    _MSGCREATEVALIDATOR.fields_by_name['description']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGCREATEVALIDATOR.fields_by_name['commission']._options = None
    _MSGCREATEVALIDATOR.fields_by_name['commission']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGCREATEVALIDATOR.fields_by_name['min_self_delegation']._options = None
    _MSGCREATEVALIDATOR.fields_by_name['min_self_delegation']._serialized_options = b'\xd2\xb4-\ncosmos.Int\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _MSGCREATEVALIDATOR.fields_by_name['delegator_address']._options = None
    _MSGCREATEVALIDATOR.fields_by_name['delegator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGCREATEVALIDATOR.fields_by_name['validator_address']._options = None
    _MSGCREATEVALIDATOR.fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGCREATEVALIDATOR.fields_by_name['pubkey']._options = None
    _MSGCREATEVALIDATOR.fields_by_name['pubkey']._serialized_options = b'\xca\xb4-\x14cosmos.crypto.PubKey'
    _MSGCREATEVALIDATOR.fields_by_name['value']._options = None
    _MSGCREATEVALIDATOR.fields_by_name['value']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGCREATEVALIDATOR._options = None
    _MSGCREATEVALIDATOR._serialized_options = b'\x82\xe7\xb0*\x11delegator_address\x82\xe7\xb0*\x11validator_address\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _MSGEDITVALIDATOR.fields_by_name['description']._options = None
    _MSGEDITVALIDATOR.fields_by_name['description']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGEDITVALIDATOR.fields_by_name['validator_address']._options = None
    _MSGEDITVALIDATOR.fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGEDITVALIDATOR.fields_by_name['commission_rate']._options = None
    _MSGEDITVALIDATOR.fields_by_name['commission_rate']._serialized_options = b'\xd2\xb4-\ncosmos.Dec\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec'
    _MSGEDITVALIDATOR.fields_by_name['min_self_delegation']._options = None
    _MSGEDITVALIDATOR.fields_by_name['min_self_delegation']._serialized_options = b'\xd2\xb4-\ncosmos.Int\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _MSGEDITVALIDATOR._options = None
    _MSGEDITVALIDATOR._serialized_options = b'\x82\xe7\xb0*\x11validator_address\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _MSGDELEGATE.fields_by_name['delegator_address']._options = None
    _MSGDELEGATE.fields_by_name['delegator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGDELEGATE.fields_by_name['validator_address']._options = None
    _MSGDELEGATE.fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGDELEGATE.fields_by_name['amount']._options = None
    _MSGDELEGATE.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGDELEGATE._options = None
    _MSGDELEGATE._serialized_options = b'\x82\xe7\xb0*\x11delegator_address\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _MSGBEGINREDELEGATE.fields_by_name['delegator_address']._options = None
    _MSGBEGINREDELEGATE.fields_by_name['delegator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGBEGINREDELEGATE.fields_by_name['validator_src_address']._options = None
    _MSGBEGINREDELEGATE.fields_by_name['validator_src_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGBEGINREDELEGATE.fields_by_name['validator_dst_address']._options = None
    _MSGBEGINREDELEGATE.fields_by_name['validator_dst_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGBEGINREDELEGATE.fields_by_name['amount']._options = None
    _MSGBEGINREDELEGATE.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGBEGINREDELEGATE._options = None
    _MSGBEGINREDELEGATE._serialized_options = b'\x82\xe7\xb0*\x11delegator_address\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _MSGBEGINREDELEGATERESPONSE.fields_by_name['completion_time']._options = None
    _MSGBEGINREDELEGATERESPONSE.fields_by_name['completion_time']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _MSGUNDELEGATE.fields_by_name['delegator_address']._options = None
    _MSGUNDELEGATE.fields_by_name['delegator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGUNDELEGATE.fields_by_name['validator_address']._options = None
    _MSGUNDELEGATE.fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGUNDELEGATE.fields_by_name['amount']._options = None
    _MSGUNDELEGATE.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGUNDELEGATE._options = None
    _MSGUNDELEGATE._serialized_options = b'\x82\xe7\xb0*\x11delegator_address\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _MSGUNDELEGATERESPONSE.fields_by_name['completion_time']._options = None
    _MSGUNDELEGATERESPONSE.fields_by_name['completion_time']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _MSGCANCELUNBONDINGDELEGATION.fields_by_name['delegator_address']._options = None
    _MSGCANCELUNBONDINGDELEGATION.fields_by_name['delegator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGCANCELUNBONDINGDELEGATION.fields_by_name['validator_address']._options = None
    _MSGCANCELUNBONDINGDELEGATION.fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGCANCELUNBONDINGDELEGATION.fields_by_name['amount']._options = None
    _MSGCANCELUNBONDINGDELEGATION.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGCANCELUNBONDINGDELEGATION._options = None
    _MSGCANCELUNBONDINGDELEGATION._serialized_options = b'\x82\xe7\xb0*\x11delegator_address\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _MSGCREATEVALIDATOR._serialized_start = 264
    _MSGCREATEVALIDATOR._serialized_end = 778
    _MSGCREATEVALIDATORRESPONSE._serialized_start = 780
    _MSGCREATEVALIDATORRESPONSE._serialized_end = 808
    _MSGEDITVALIDATOR._serialized_start = 811
    _MSGEDITVALIDATOR._serialized_end = 1148
    _MSGEDITVALIDATORRESPONSE._serialized_start = 1150
    _MSGEDITVALIDATORRESPONSE._serialized_end = 1176
    _MSGDELEGATE._serialized_start = 1179
    _MSGDELEGATE._serialized_end = 1379
    _MSGDELEGATERESPONSE._serialized_start = 1381
    _MSGDELEGATERESPONSE._serialized_end = 1402
    _MSGBEGINREDELEGATE._serialized_start = 1405
    _MSGBEGINREDELEGATE._serialized_end = 1673
    _MSGBEGINREDELEGATERESPONSE._serialized_start = 1675
    _MSGBEGINREDELEGATERESPONSE._serialized_end = 1766
    _MSGUNDELEGATE._serialized_start = 1769
    _MSGUNDELEGATE._serialized_end = 1971
    _MSGUNDELEGATERESPONSE._serialized_start = 1973
    _MSGUNDELEGATERESPONSE._serialized_end = 2059
    _MSGCANCELUNBONDINGDELEGATION._serialized_start = 2062
    _MSGCANCELUNBONDINGDELEGATION._serialized_end = 2304
    _MSGCANCELUNBONDINGDELEGATIONRESPONSE._serialized_start = 2306
    _MSGCANCELUNBONDINGDELEGATIONRESPONSE._serialized_end = 2344
    _MSG._serialized_start = 2347
    _MSG._serialized_end = 3031
