
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17umee/oracle/v1/tx.proto\x12\x1aumeenetwork.umee.oracle.v1\x1a\x14gogoproto/gogo.proto"\x96\x01\n\x1fMsgAggregateExchangeRatePrevote\x12\x1d\n\x04hash\x18\x01 \x01(\tB\x0f\xf2\xde\x1f\x0byaml:"hash"\x12!\n\x06feeder\x18\x02 \x01(\tB\x11\xf2\xde\x1f\ryaml:"feeder"\x12\'\n\tvalidator\x18\x03 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"validator":\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00")\n\'MsgAggregateExchangeRatePrevoteResponse"\xc6\x01\n\x1cMsgAggregateExchangeRateVote\x12\x1d\n\x04salt\x18\x01 \x01(\tB\x0f\xf2\xde\x1f\x0byaml:"salt"\x121\n\x0eexchange_rates\x18\x02 \x01(\tB\x19\xf2\xde\x1f\x15yaml:"exchange_rates"\x12!\n\x06feeder\x18\x03 \x01(\tB\x11\xf2\xde\x1f\ryaml:"feeder"\x12\'\n\tvalidator\x18\x04 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"validator":\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"&\n$MsgAggregateExchangeRateVoteResponse"p\n\x16MsgDelegateFeedConsent\x12%\n\x08operator\x18\x01 \x01(\tB\x13\xf2\xde\x1f\x0fyaml:"operator"\x12%\n\x08delegate\x18\x02 \x01(\tB\x13\xf2\xde\x1f\x0fyaml:"delegate":\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00" \n\x1eMsgDelegateFeedConsentResponse2\xca\x03\n\x03Msg\x12\xa0\x01\n\x1cAggregateExchangeRatePrevote\x12;.umeenetwork.umee.oracle.v1.MsgAggregateExchangeRatePrevote\x1aC.umeenetwork.umee.oracle.v1.MsgAggregateExchangeRatePrevoteResponse\x12\x97\x01\n\x19AggregateExchangeRateVote\x128.umeenetwork.umee.oracle.v1.MsgAggregateExchangeRateVote\x1a@.umeenetwork.umee.oracle.v1.MsgAggregateExchangeRateVoteResponse\x12\x85\x01\n\x13DelegateFeedConsent\x122.umeenetwork.umee.oracle.v1.MsgDelegateFeedConsent\x1a:.umeenetwork.umee.oracle.v1.MsgDelegateFeedConsentResponseB0Z.github.com/umee-network/umee/v2/x/oracle/typesb\x06proto3')
_MSGAGGREGATEEXCHANGERATEPREVOTE = DESCRIPTOR.message_types_by_name['MsgAggregateExchangeRatePrevote']
_MSGAGGREGATEEXCHANGERATEPREVOTERESPONSE = DESCRIPTOR.message_types_by_name['MsgAggregateExchangeRatePrevoteResponse']
_MSGAGGREGATEEXCHANGERATEVOTE = DESCRIPTOR.message_types_by_name['MsgAggregateExchangeRateVote']
_MSGAGGREGATEEXCHANGERATEVOTERESPONSE = DESCRIPTOR.message_types_by_name['MsgAggregateExchangeRateVoteResponse']
_MSGDELEGATEFEEDCONSENT = DESCRIPTOR.message_types_by_name['MsgDelegateFeedConsent']
_MSGDELEGATEFEEDCONSENTRESPONSE = DESCRIPTOR.message_types_by_name['MsgDelegateFeedConsentResponse']
MsgAggregateExchangeRatePrevote = _reflection.GeneratedProtocolMessageType('MsgAggregateExchangeRatePrevote', (_message.Message,), {'DESCRIPTOR': _MSGAGGREGATEEXCHANGERATEPREVOTE, '__module__': 'umee.oracle.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgAggregateExchangeRatePrevote)
MsgAggregateExchangeRatePrevoteResponse = _reflection.GeneratedProtocolMessageType('MsgAggregateExchangeRatePrevoteResponse', (_message.Message,), {'DESCRIPTOR': _MSGAGGREGATEEXCHANGERATEPREVOTERESPONSE, '__module__': 'umee.oracle.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgAggregateExchangeRatePrevoteResponse)
MsgAggregateExchangeRateVote = _reflection.GeneratedProtocolMessageType('MsgAggregateExchangeRateVote', (_message.Message,), {'DESCRIPTOR': _MSGAGGREGATEEXCHANGERATEVOTE, '__module__': 'umee.oracle.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgAggregateExchangeRateVote)
MsgAggregateExchangeRateVoteResponse = _reflection.GeneratedProtocolMessageType('MsgAggregateExchangeRateVoteResponse', (_message.Message,), {'DESCRIPTOR': _MSGAGGREGATEEXCHANGERATEVOTERESPONSE, '__module__': 'umee.oracle.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgAggregateExchangeRateVoteResponse)
MsgDelegateFeedConsent = _reflection.GeneratedProtocolMessageType('MsgDelegateFeedConsent', (_message.Message,), {'DESCRIPTOR': _MSGDELEGATEFEEDCONSENT, '__module__': 'umee.oracle.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgDelegateFeedConsent)
MsgDelegateFeedConsentResponse = _reflection.GeneratedProtocolMessageType('MsgDelegateFeedConsentResponse', (_message.Message,), {'DESCRIPTOR': _MSGDELEGATEFEEDCONSENTRESPONSE, '__module__': 'umee.oracle.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgDelegateFeedConsentResponse)
_MSG = DESCRIPTOR.services_by_name['Msg']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z.github.com/umee-network/umee/v2/x/oracle/types'
    _MSGAGGREGATEEXCHANGERATEPREVOTE.fields_by_name['hash']._options = None
    _MSGAGGREGATEEXCHANGERATEPREVOTE.fields_by_name['hash']._serialized_options = b'\xf2\xde\x1f\x0byaml:"hash"'
    _MSGAGGREGATEEXCHANGERATEPREVOTE.fields_by_name['feeder']._options = None
    _MSGAGGREGATEEXCHANGERATEPREVOTE.fields_by_name['feeder']._serialized_options = b'\xf2\xde\x1f\ryaml:"feeder"'
    _MSGAGGREGATEEXCHANGERATEPREVOTE.fields_by_name['validator']._options = None
    _MSGAGGREGATEEXCHANGERATEPREVOTE.fields_by_name['validator']._serialized_options = b'\xf2\xde\x1f\x10yaml:"validator"'
    _MSGAGGREGATEEXCHANGERATEPREVOTE._options = None
    _MSGAGGREGATEEXCHANGERATEPREVOTE._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _MSGAGGREGATEEXCHANGERATEVOTE.fields_by_name['salt']._options = None
    _MSGAGGREGATEEXCHANGERATEVOTE.fields_by_name['salt']._serialized_options = b'\xf2\xde\x1f\x0byaml:"salt"'
    _MSGAGGREGATEEXCHANGERATEVOTE.fields_by_name['exchange_rates']._options = None
    _MSGAGGREGATEEXCHANGERATEVOTE.fields_by_name['exchange_rates']._serialized_options = b'\xf2\xde\x1f\x15yaml:"exchange_rates"'
    _MSGAGGREGATEEXCHANGERATEVOTE.fields_by_name['feeder']._options = None
    _MSGAGGREGATEEXCHANGERATEVOTE.fields_by_name['feeder']._serialized_options = b'\xf2\xde\x1f\ryaml:"feeder"'
    _MSGAGGREGATEEXCHANGERATEVOTE.fields_by_name['validator']._options = None
    _MSGAGGREGATEEXCHANGERATEVOTE.fields_by_name['validator']._serialized_options = b'\xf2\xde\x1f\x10yaml:"validator"'
    _MSGAGGREGATEEXCHANGERATEVOTE._options = None
    _MSGAGGREGATEEXCHANGERATEVOTE._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _MSGDELEGATEFEEDCONSENT.fields_by_name['operator']._options = None
    _MSGDELEGATEFEEDCONSENT.fields_by_name['operator']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"operator"'
    _MSGDELEGATEFEEDCONSENT.fields_by_name['delegate']._options = None
    _MSGDELEGATEFEEDCONSENT.fields_by_name['delegate']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"delegate"'
    _MSGDELEGATEFEEDCONSENT._options = None
    _MSGDELEGATEFEEDCONSENT._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _MSGAGGREGATEEXCHANGERATEPREVOTE._serialized_start = 78
    _MSGAGGREGATEEXCHANGERATEPREVOTE._serialized_end = 228
    _MSGAGGREGATEEXCHANGERATEPREVOTERESPONSE._serialized_start = 230
    _MSGAGGREGATEEXCHANGERATEPREVOTERESPONSE._serialized_end = 271
    _MSGAGGREGATEEXCHANGERATEVOTE._serialized_start = 274
    _MSGAGGREGATEEXCHANGERATEVOTE._serialized_end = 472
    _MSGAGGREGATEEXCHANGERATEVOTERESPONSE._serialized_start = 474
    _MSGAGGREGATEEXCHANGERATEVOTERESPONSE._serialized_end = 512
    _MSGDELEGATEFEEDCONSENT._serialized_start = 514
    _MSGDELEGATEFEEDCONSENT._serialized_end = 626
    _MSGDELEGATEFEEDCONSENTRESPONSE._serialized_start = 628
    _MSGDELEGATEFEEDCONSENTRESPONSE._serialized_end = 660
    _MSG._serialized_start = 663
    _MSG._serialized_end = 1121
