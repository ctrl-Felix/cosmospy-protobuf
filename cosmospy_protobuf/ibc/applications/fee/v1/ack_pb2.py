
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!ibc/applications/fee/v1/ack.proto\x12\x17ibc.applications.fee.v1\x1a\x14gogoproto/gogo.proto"\xb6\x01\n\x1bIncentivizedAcknowledgement\x12\x0e\n\x06result\x18\x01 \x01(\x0c\x12C\n\x17forward_relayer_address\x18\x02 \x01(\tB"\xf2\xde\x1f\x1eyaml:"forward_relayer_address"\x12B\n\x16underlying_app_success\x18\x03 \x01(\x08B"\xf2\xde\x1f\x1eyaml:"underlying_app_successl"B7Z5github.com/cosmos/ibc-go/v3/modules/apps/29-fee/typesb\x06proto3')
_INCENTIVIZEDACKNOWLEDGEMENT = DESCRIPTOR.message_types_by_name['IncentivizedAcknowledgement']
IncentivizedAcknowledgement = _reflection.GeneratedProtocolMessageType('IncentivizedAcknowledgement', (_message.Message,), {'DESCRIPTOR': _INCENTIVIZEDACKNOWLEDGEMENT, '__module__': 'ibc.applications.fee.v1.ack_pb2'})
_sym_db.RegisterMessage(IncentivizedAcknowledgement)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z5github.com/cosmos/ibc-go/v3/modules/apps/29-fee/types'
    _INCENTIVIZEDACKNOWLEDGEMENT.fields_by_name['forward_relayer_address']._options = None
    _INCENTIVIZEDACKNOWLEDGEMENT.fields_by_name['forward_relayer_address']._serialized_options = b'\xf2\xde\x1f\x1eyaml:"forward_relayer_address"'
    _INCENTIVIZEDACKNOWLEDGEMENT.fields_by_name['underlying_app_success']._options = None
    _INCENTIVIZEDACKNOWLEDGEMENT.fields_by_name['underlying_app_success']._serialized_options = b'\xf2\xde\x1f\x1eyaml:"underlying_app_successl"'
    _INCENTIVIZEDACKNOWLEDGEMENT._serialized_start = 85
    _INCENTIVIZEDACKNOWLEDGEMENT._serialized_end = 267
