
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/app/v1alpha1/config.proto\x12\x13cosmos.app.v1alpha1\x1a\x19google/protobuf/any.proto"<\n\x06Config\x122\n\x07modules\x18\x01 \x03(\x0b2!.cosmos.app.v1alpha1.ModuleConfig"B\n\x0cModuleConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12$\n\x06config\x18\x02 \x01(\x0b2\x14.google.protobuf.Anyb\x06proto3')
_CONFIG = DESCRIPTOR.message_types_by_name['Config']
_MODULECONFIG = DESCRIPTOR.message_types_by_name['ModuleConfig']
Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {'DESCRIPTOR': _CONFIG, '__module__': 'cosmos.app.v1alpha1.config_pb2'})
_sym_db.RegisterMessage(Config)
ModuleConfig = _reflection.GeneratedProtocolMessageType('ModuleConfig', (_message.Message,), {'DESCRIPTOR': _MODULECONFIG, '__module__': 'cosmos.app.v1alpha1.config_pb2'})
_sym_db.RegisterMessage(ModuleConfig)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    _CONFIG._serialized_start = 84
    _CONFIG._serialized_end = 144
    _MODULECONFIG._serialized_start = 146
    _MODULECONFIG._serialized_end = 212
