
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from .....ibc.applications.fee.v1 import fee_pb2 as ibc_dot_applications_dot_fee_dot_v1_dot_fee__pb2
from .....ibc.core.channel.v1 import channel_pb2 as ibc_dot_core_dot_channel_dot_v1_dot_channel__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n ibc/applications/fee/v1/tx.proto\x12\x17ibc.applications.fee.v1\x1a\x14gogoproto/gogo.proto\x1a!ibc/applications/fee/v1/fee.proto\x1a!ibc/core/channel/v1/channel.proto"\xa5\x01\n\x1eMsgRegisterCounterpartyAddress\x12\x0f\n\x07address\x18\x01 \x01(\t\x12=\n\x14counterparty_address\x18\x02 \x01(\tB\x1f\xf2\xde\x1f\x1byaml:"counterparty_address"\x12)\n\nchannel_id\x18\x03 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"channel_id":\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"(\n&MsgRegisterCounterpartyAddressResponse"\xda\x01\n\x0fMsgPayPacketFee\x12/\n\x03fee\x18\x01 \x01(\x0b2\x1c.ibc.applications.fee.v1.FeeB\x04\xc8\xde\x1f\x00\x121\n\x0esource_port_id\x18\x02 \x01(\tB\x19\xf2\xde\x1f\x15yaml:"source_port_id"\x127\n\x11source_channel_id\x18\x03 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"source_channel_id"\x12\x0e\n\x06signer\x18\x04 \x01(\t\x12\x10\n\x08relayers\x18\x05 \x03(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\x19\n\x17MsgPayPacketFeeResponse"\xbf\x01\n\x14MsgPayPacketFeeAsync\x12J\n\tpacket_id\x18\x01 \x01(\x0b2\x1d.ibc.core.channel.v1.PacketIdB\x18\xf2\xde\x1f\x10yaml:"packet_id"\xc8\xde\x1f\x00\x12Q\n\npacket_fee\x18\x02 \x01(\x0b2".ibc.applications.fee.v1.PacketFeeB\x19\xf2\xde\x1f\x11yaml:"packet_fee"\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\x1e\n\x1cMsgPayPacketFeeAsyncResponse2\x86\x03\n\x03Msg\x12\x97\x01\n\x1bRegisterCounterpartyAddress\x127.ibc.applications.fee.v1.MsgRegisterCounterpartyAddress\x1a?.ibc.applications.fee.v1.MsgRegisterCounterpartyAddressResponse\x12j\n\x0cPayPacketFee\x12(.ibc.applications.fee.v1.MsgPayPacketFee\x1a0.ibc.applications.fee.v1.MsgPayPacketFeeResponse\x12y\n\x11PayPacketFeeAsync\x12-.ibc.applications.fee.v1.MsgPayPacketFeeAsync\x1a5.ibc.applications.fee.v1.MsgPayPacketFeeAsyncResponseB7Z5github.com/cosmos/ibc-go/v3/modules/apps/29-fee/typesb\x06proto3')
_MSGREGISTERCOUNTERPARTYADDRESS = DESCRIPTOR.message_types_by_name['MsgRegisterCounterpartyAddress']
_MSGREGISTERCOUNTERPARTYADDRESSRESPONSE = DESCRIPTOR.message_types_by_name['MsgRegisterCounterpartyAddressResponse']
_MSGPAYPACKETFEE = DESCRIPTOR.message_types_by_name['MsgPayPacketFee']
_MSGPAYPACKETFEERESPONSE = DESCRIPTOR.message_types_by_name['MsgPayPacketFeeResponse']
_MSGPAYPACKETFEEASYNC = DESCRIPTOR.message_types_by_name['MsgPayPacketFeeAsync']
_MSGPAYPACKETFEEASYNCRESPONSE = DESCRIPTOR.message_types_by_name['MsgPayPacketFeeAsyncResponse']
MsgRegisterCounterpartyAddress = _reflection.GeneratedProtocolMessageType('MsgRegisterCounterpartyAddress', (_message.Message,), {'DESCRIPTOR': _MSGREGISTERCOUNTERPARTYADDRESS, '__module__': 'ibc.applications.fee.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgRegisterCounterpartyAddress)
MsgRegisterCounterpartyAddressResponse = _reflection.GeneratedProtocolMessageType('MsgRegisterCounterpartyAddressResponse', (_message.Message,), {'DESCRIPTOR': _MSGREGISTERCOUNTERPARTYADDRESSRESPONSE, '__module__': 'ibc.applications.fee.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgRegisterCounterpartyAddressResponse)
MsgPayPacketFee = _reflection.GeneratedProtocolMessageType('MsgPayPacketFee', (_message.Message,), {'DESCRIPTOR': _MSGPAYPACKETFEE, '__module__': 'ibc.applications.fee.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgPayPacketFee)
MsgPayPacketFeeResponse = _reflection.GeneratedProtocolMessageType('MsgPayPacketFeeResponse', (_message.Message,), {'DESCRIPTOR': _MSGPAYPACKETFEERESPONSE, '__module__': 'ibc.applications.fee.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgPayPacketFeeResponse)
MsgPayPacketFeeAsync = _reflection.GeneratedProtocolMessageType('MsgPayPacketFeeAsync', (_message.Message,), {'DESCRIPTOR': _MSGPAYPACKETFEEASYNC, '__module__': 'ibc.applications.fee.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgPayPacketFeeAsync)
MsgPayPacketFeeAsyncResponse = _reflection.GeneratedProtocolMessageType('MsgPayPacketFeeAsyncResponse', (_message.Message,), {'DESCRIPTOR': _MSGPAYPACKETFEEASYNCRESPONSE, '__module__': 'ibc.applications.fee.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgPayPacketFeeAsyncResponse)
_MSG = DESCRIPTOR.services_by_name['Msg']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z5github.com/cosmos/ibc-go/v3/modules/apps/29-fee/types'
    _MSGREGISTERCOUNTERPARTYADDRESS.fields_by_name['counterparty_address']._options = None
    _MSGREGISTERCOUNTERPARTYADDRESS.fields_by_name['counterparty_address']._serialized_options = b'\xf2\xde\x1f\x1byaml:"counterparty_address"'
    _MSGREGISTERCOUNTERPARTYADDRESS.fields_by_name['channel_id']._options = None
    _MSGREGISTERCOUNTERPARTYADDRESS.fields_by_name['channel_id']._serialized_options = b'\xf2\xde\x1f\x11yaml:"channel_id"'
    _MSGREGISTERCOUNTERPARTYADDRESS._options = None
    _MSGREGISTERCOUNTERPARTYADDRESS._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _MSGPAYPACKETFEE.fields_by_name['fee']._options = None
    _MSGPAYPACKETFEE.fields_by_name['fee']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGPAYPACKETFEE.fields_by_name['source_port_id']._options = None
    _MSGPAYPACKETFEE.fields_by_name['source_port_id']._serialized_options = b'\xf2\xde\x1f\x15yaml:"source_port_id"'
    _MSGPAYPACKETFEE.fields_by_name['source_channel_id']._options = None
    _MSGPAYPACKETFEE.fields_by_name['source_channel_id']._serialized_options = b'\xf2\xde\x1f\x18yaml:"source_channel_id"'
    _MSGPAYPACKETFEE._options = None
    _MSGPAYPACKETFEE._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _MSGPAYPACKETFEEASYNC.fields_by_name['packet_id']._options = None
    _MSGPAYPACKETFEEASYNC.fields_by_name['packet_id']._serialized_options = b'\xf2\xde\x1f\x10yaml:"packet_id"\xc8\xde\x1f\x00'
    _MSGPAYPACKETFEEASYNC.fields_by_name['packet_fee']._options = None
    _MSGPAYPACKETFEEASYNC.fields_by_name['packet_fee']._serialized_options = b'\xf2\xde\x1f\x11yaml:"packet_fee"\xc8\xde\x1f\x00'
    _MSGPAYPACKETFEEASYNC._options = None
    _MSGPAYPACKETFEEASYNC._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _MSGREGISTERCOUNTERPARTYADDRESS._serialized_start = 154
    _MSGREGISTERCOUNTERPARTYADDRESS._serialized_end = 319
    _MSGREGISTERCOUNTERPARTYADDRESSRESPONSE._serialized_start = 321
    _MSGREGISTERCOUNTERPARTYADDRESSRESPONSE._serialized_end = 361
    _MSGPAYPACKETFEE._serialized_start = 364
    _MSGPAYPACKETFEE._serialized_end = 582
    _MSGPAYPACKETFEERESPONSE._serialized_start = 584
    _MSGPAYPACKETFEERESPONSE._serialized_end = 609
    _MSGPAYPACKETFEEASYNC._serialized_start = 612
    _MSGPAYPACKETFEEASYNC._serialized_end = 803
    _MSGPAYPACKETFEEASYNCRESPONSE._serialized_start = 805
    _MSGPAYPACKETFEEASYNCRESPONSE._serialized_end = 835
    _MSG._serialized_start = 838
    _MSG._serialized_end = 1228
