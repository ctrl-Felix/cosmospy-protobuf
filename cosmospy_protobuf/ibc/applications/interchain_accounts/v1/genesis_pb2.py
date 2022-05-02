
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from .....ibc.applications.interchain_accounts.controller.v1 import controller_pb2 as ibc_dot_applications_dot_interchain__accounts_dot_controller_dot_v1_dot_controller__pb2
from .....ibc.applications.interchain_accounts.host.v1 import host_pb2 as ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_host__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5ibc/applications/interchain_accounts/v1/genesis.proto\x12\'ibc.applications.interchain_accounts.v1\x1a\x14gogoproto/gogo.proto\x1aCibc/applications/interchain_accounts/controller/v1/controller.proto\x1a7ibc/applications/interchain_accounts/host/v1/host.proto"\x95\x02\n\x0cGenesisState\x12\x8a\x01\n\x18controller_genesis_state\x18\x01 \x01(\x0b2?.ibc.applications.interchain_accounts.v1.ControllerGenesisStateB\'\xc8\xde\x1f\x00\xf2\xde\x1f\x1fyaml:"controller_genesis_state"\x12x\n\x12host_genesis_state\x18\x02 \x01(\x0b29.ibc.applications.interchain_accounts.v1.HostGenesisStateB!\xc8\xde\x1f\x00\xf2\xde\x1f\x19yaml:"host_genesis_state""\xf2\x02\n\x16ControllerGenesisState\x12o\n\x0factive_channels\x18\x01 \x03(\x0b26.ibc.applications.interchain_accounts.v1.ActiveChannelB\x1e\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:"active_channels"\x12\x85\x01\n\x13interchain_accounts\x18\x02 \x03(\x0b2D.ibc.applications.interchain_accounts.v1.RegisteredInterchainAccountB"\xc8\xde\x1f\x00\xf2\xde\x1f\x1ayaml:"interchain_accounts"\x12\r\n\x05ports\x18\x03 \x03(\t\x12P\n\x06params\x18\x04 \x01(\x0b2:.ibc.applications.interchain_accounts.controller.v1.ParamsB\x04\xc8\xde\x1f\x00"\xe5\x02\n\x10HostGenesisState\x12o\n\x0factive_channels\x18\x01 \x03(\x0b26.ibc.applications.interchain_accounts.v1.ActiveChannelB\x1e\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:"active_channels"\x12\x85\x01\n\x13interchain_accounts\x18\x02 \x03(\x0b2D.ibc.applications.interchain_accounts.v1.RegisteredInterchainAccountB"\xc8\xde\x1f\x00\xf2\xde\x1f\x1ayaml:"interchain_accounts"\x12\x0c\n\x04port\x18\x03 \x01(\t\x12J\n\x06params\x18\x04 \x01(\x0b24.ibc.applications.interchain_accounts.host.v1.ParamsB\x04\xc8\xde\x1f\x00"\x90\x01\n\rActiveChannel\x12/\n\rconnection_id\x18\x01 \x01(\tB\x18\xf2\xde\x1f\x14yaml:"connection_id"\x12#\n\x07port_id\x18\x02 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"port_id"\x12)\n\nchannel_id\x18\x03 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"channel_id""\xa8\x01\n\x1bRegisteredInterchainAccount\x12/\n\rconnection_id\x18\x01 \x01(\tB\x18\xf2\xde\x1f\x14yaml:"connection_id"\x12#\n\x07port_id\x18\x02 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"port_id"\x123\n\x0faccount_address\x18\x03 \x01(\tB\x1a\xf2\xde\x1f\x16yaml:"account_address"BGZEgithub.com/cosmos/ibc-go/v3/modules/apps/27-interchain-accounts/typesb\x06proto3')
_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
_CONTROLLERGENESISSTATE = DESCRIPTOR.message_types_by_name['ControllerGenesisState']
_HOSTGENESISSTATE = DESCRIPTOR.message_types_by_name['HostGenesisState']
_ACTIVECHANNEL = DESCRIPTOR.message_types_by_name['ActiveChannel']
_REGISTEREDINTERCHAINACCOUNT = DESCRIPTOR.message_types_by_name['RegisteredInterchainAccount']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {'DESCRIPTOR': _GENESISSTATE, '__module__': 'ibc.applications.interchain_accounts.v1.genesis_pb2'})
_sym_db.RegisterMessage(GenesisState)
ControllerGenesisState = _reflection.GeneratedProtocolMessageType('ControllerGenesisState', (_message.Message,), {'DESCRIPTOR': _CONTROLLERGENESISSTATE, '__module__': 'ibc.applications.interchain_accounts.v1.genesis_pb2'})
_sym_db.RegisterMessage(ControllerGenesisState)
HostGenesisState = _reflection.GeneratedProtocolMessageType('HostGenesisState', (_message.Message,), {'DESCRIPTOR': _HOSTGENESISSTATE, '__module__': 'ibc.applications.interchain_accounts.v1.genesis_pb2'})
_sym_db.RegisterMessage(HostGenesisState)
ActiveChannel = _reflection.GeneratedProtocolMessageType('ActiveChannel', (_message.Message,), {'DESCRIPTOR': _ACTIVECHANNEL, '__module__': 'ibc.applications.interchain_accounts.v1.genesis_pb2'})
_sym_db.RegisterMessage(ActiveChannel)
RegisteredInterchainAccount = _reflection.GeneratedProtocolMessageType('RegisteredInterchainAccount', (_message.Message,), {'DESCRIPTOR': _REGISTEREDINTERCHAINACCOUNT, '__module__': 'ibc.applications.interchain_accounts.v1.genesis_pb2'})
_sym_db.RegisterMessage(RegisteredInterchainAccount)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZEgithub.com/cosmos/ibc-go/v3/modules/apps/27-interchain-accounts/types'
    _GENESISSTATE.fields_by_name['controller_genesis_state']._options = None
    _GENESISSTATE.fields_by_name['controller_genesis_state']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x1fyaml:"controller_genesis_state"'
    _GENESISSTATE.fields_by_name['host_genesis_state']._options = None
    _GENESISSTATE.fields_by_name['host_genesis_state']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x19yaml:"host_genesis_state"'
    _CONTROLLERGENESISSTATE.fields_by_name['active_channels']._options = None
    _CONTROLLERGENESISSTATE.fields_by_name['active_channels']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:"active_channels"'
    _CONTROLLERGENESISSTATE.fields_by_name['interchain_accounts']._options = None
    _CONTROLLERGENESISSTATE.fields_by_name['interchain_accounts']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x1ayaml:"interchain_accounts"'
    _CONTROLLERGENESISSTATE.fields_by_name['params']._options = None
    _CONTROLLERGENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _HOSTGENESISSTATE.fields_by_name['active_channels']._options = None
    _HOSTGENESISSTATE.fields_by_name['active_channels']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:"active_channels"'
    _HOSTGENESISSTATE.fields_by_name['interchain_accounts']._options = None
    _HOSTGENESISSTATE.fields_by_name['interchain_accounts']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x1ayaml:"interchain_accounts"'
    _HOSTGENESISSTATE.fields_by_name['params']._options = None
    _HOSTGENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _ACTIVECHANNEL.fields_by_name['connection_id']._options = None
    _ACTIVECHANNEL.fields_by_name['connection_id']._serialized_options = b'\xf2\xde\x1f\x14yaml:"connection_id"'
    _ACTIVECHANNEL.fields_by_name['port_id']._options = None
    _ACTIVECHANNEL.fields_by_name['port_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"port_id"'
    _ACTIVECHANNEL.fields_by_name['channel_id']._options = None
    _ACTIVECHANNEL.fields_by_name['channel_id']._serialized_options = b'\xf2\xde\x1f\x11yaml:"channel_id"'
    _REGISTEREDINTERCHAINACCOUNT.fields_by_name['connection_id']._options = None
    _REGISTEREDINTERCHAINACCOUNT.fields_by_name['connection_id']._serialized_options = b'\xf2\xde\x1f\x14yaml:"connection_id"'
    _REGISTEREDINTERCHAINACCOUNT.fields_by_name['port_id']._options = None
    _REGISTEREDINTERCHAINACCOUNT.fields_by_name['port_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"port_id"'
    _REGISTEREDINTERCHAINACCOUNT.fields_by_name['account_address']._options = None
    _REGISTEREDINTERCHAINACCOUNT.fields_by_name['account_address']._serialized_options = b'\xf2\xde\x1f\x16yaml:"account_address"'
    _GENESISSTATE._serialized_start = 247
    _GENESISSTATE._serialized_end = 524
    _CONTROLLERGENESISSTATE._serialized_start = 527
    _CONTROLLERGENESISSTATE._serialized_end = 897
    _HOSTGENESISSTATE._serialized_start = 900
    _HOSTGENESISSTATE._serialized_end = 1257
    _ACTIVECHANNEL._serialized_start = 1260
    _ACTIVECHANNEL._serialized_end = 1404
    _REGISTEREDINTERCHAINACCOUNT._serialized_start = 1407
    _REGISTEREDINTERCHAINACCOUNT._serialized_end = 1575
