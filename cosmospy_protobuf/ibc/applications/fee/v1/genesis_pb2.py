
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
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%ibc/applications/fee/v1/genesis.proto\x12\x17ibc.applications.fee.v1\x1a\x14gogoproto/gogo.proto\x1a!ibc/applications/fee/v1/fee.proto\x1a!ibc/core/channel/v1/channel.proto"\xc4\x03\n\x0cGenesisState\x12f\n\x0fidentified_fees\x18\x01 \x03(\x0b2-.ibc.applications.fee.v1.IdentifiedPacketFeesB\x1e\xf2\xde\x1f\x16yaml:"identified_fees"\xc8\xde\x1f\x00\x12m\n\x14fee_enabled_channels\x18\x02 \x03(\x0b2*.ibc.applications.fee.v1.FeeEnabledChannelB#\xf2\xde\x1f\x1byaml:"fee_enabled_channels"\xc8\xde\x1f\x00\x12r\n\x13registered_relayers\x18\x03 \x03(\x0b21.ibc.applications.fee.v1.RegisteredRelayerAddressB"\xf2\xde\x1f\x1ayaml:"registered_relayers"\xc8\xde\x1f\x00\x12i\n\x10forward_relayers\x18\x04 \x03(\x0b2..ibc.applications.fee.v1.ForwardRelayerAddressB\x1f\xf2\xde\x1f\x17yaml:"forward_relayers"\xc8\xde\x1f\x00"c\n\x11FeeEnabledChannel\x12#\n\x07port_id\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"port_id"\x12)\n\nchannel_id\x18\x02 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"channel_id""\x95\x01\n\x18RegisteredRelayerAddress\x12\x0f\n\x07address\x18\x01 \x01(\t\x12=\n\x14counterparty_address\x18\x02 \x01(\tB\x1f\xf2\xde\x1f\x1byaml:"counterparty_address"\x12)\n\nchannel_id\x18\x03 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"channel_id""t\n\x15ForwardRelayerAddress\x12\x0f\n\x07address\x18\x01 \x01(\t\x12J\n\tpacket_id\x18\x02 \x01(\x0b2\x1d.ibc.core.channel.v1.PacketIdB\x18\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"packet_id"B7Z5github.com/cosmos/ibc-go/v3/modules/apps/29-fee/typesb\x06proto3')
_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
_FEEENABLEDCHANNEL = DESCRIPTOR.message_types_by_name['FeeEnabledChannel']
_REGISTEREDRELAYERADDRESS = DESCRIPTOR.message_types_by_name['RegisteredRelayerAddress']
_FORWARDRELAYERADDRESS = DESCRIPTOR.message_types_by_name['ForwardRelayerAddress']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {'DESCRIPTOR': _GENESISSTATE, '__module__': 'ibc.applications.fee.v1.genesis_pb2'})
_sym_db.RegisterMessage(GenesisState)
FeeEnabledChannel = _reflection.GeneratedProtocolMessageType('FeeEnabledChannel', (_message.Message,), {'DESCRIPTOR': _FEEENABLEDCHANNEL, '__module__': 'ibc.applications.fee.v1.genesis_pb2'})
_sym_db.RegisterMessage(FeeEnabledChannel)
RegisteredRelayerAddress = _reflection.GeneratedProtocolMessageType('RegisteredRelayerAddress', (_message.Message,), {'DESCRIPTOR': _REGISTEREDRELAYERADDRESS, '__module__': 'ibc.applications.fee.v1.genesis_pb2'})
_sym_db.RegisterMessage(RegisteredRelayerAddress)
ForwardRelayerAddress = _reflection.GeneratedProtocolMessageType('ForwardRelayerAddress', (_message.Message,), {'DESCRIPTOR': _FORWARDRELAYERADDRESS, '__module__': 'ibc.applications.fee.v1.genesis_pb2'})
_sym_db.RegisterMessage(ForwardRelayerAddress)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z5github.com/cosmos/ibc-go/v3/modules/apps/29-fee/types'
    _GENESISSTATE.fields_by_name['identified_fees']._options = None
    _GENESISSTATE.fields_by_name['identified_fees']._serialized_options = b'\xf2\xde\x1f\x16yaml:"identified_fees"\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['fee_enabled_channels']._options = None
    _GENESISSTATE.fields_by_name['fee_enabled_channels']._serialized_options = b'\xf2\xde\x1f\x1byaml:"fee_enabled_channels"\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['registered_relayers']._options = None
    _GENESISSTATE.fields_by_name['registered_relayers']._serialized_options = b'\xf2\xde\x1f\x1ayaml:"registered_relayers"\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['forward_relayers']._options = None
    _GENESISSTATE.fields_by_name['forward_relayers']._serialized_options = b'\xf2\xde\x1f\x17yaml:"forward_relayers"\xc8\xde\x1f\x00'
    _FEEENABLEDCHANNEL.fields_by_name['port_id']._options = None
    _FEEENABLEDCHANNEL.fields_by_name['port_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"port_id"'
    _FEEENABLEDCHANNEL.fields_by_name['channel_id']._options = None
    _FEEENABLEDCHANNEL.fields_by_name['channel_id']._serialized_options = b'\xf2\xde\x1f\x11yaml:"channel_id"'
    _REGISTEREDRELAYERADDRESS.fields_by_name['counterparty_address']._options = None
    _REGISTEREDRELAYERADDRESS.fields_by_name['counterparty_address']._serialized_options = b'\xf2\xde\x1f\x1byaml:"counterparty_address"'
    _REGISTEREDRELAYERADDRESS.fields_by_name['channel_id']._options = None
    _REGISTEREDRELAYERADDRESS.fields_by_name['channel_id']._serialized_options = b'\xf2\xde\x1f\x11yaml:"channel_id"'
    _FORWARDRELAYERADDRESS.fields_by_name['packet_id']._options = None
    _FORWARDRELAYERADDRESS.fields_by_name['packet_id']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"packet_id"'
    _GENESISSTATE._serialized_start = 159
    _GENESISSTATE._serialized_end = 611
    _FEEENABLEDCHANNEL._serialized_start = 613
    _FEEENABLEDCHANNEL._serialized_end = 712
    _REGISTEREDRELAYERADDRESS._serialized_start = 715
    _REGISTEREDRELAYERADDRESS._serialized_end = 864
    _FORWARDRELAYERADDRESS._serialized_start = 866
    _FORWARDRELAYERADDRESS._serialized_end = 982
