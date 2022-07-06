
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/app/v1alpha1/module.proto\x12\x13cosmos.app.v1alpha1\x1a google/protobuf/descriptor.proto"\xa1\x01\n\x10ModuleDescriptor\x12\x11\n\tgo_import\x18\x01 \x01(\t\x12:\n\x0buse_package\x18\x02 \x03(\x0b2%.cosmos.app.v1alpha1.PackageReference\x12>\n\x10can_migrate_from\x18\x03 \x03(\x0b2$.cosmos.app.v1alpha1.MigrateFromInfo"2\n\x10PackageReference\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08revision\x18\x02 \x01(\r"!\n\x0fMigrateFromInfo\x12\x0e\n\x06module\x18\x01 \x01(\t:Y\n\x06module\x12\x1f.google.protobuf.MessageOptions\x18\x87\xe8\xa2\x1b \x01(\x0b2%.cosmos.app.v1alpha1.ModuleDescriptorb\x06proto3')
MODULE_FIELD_NUMBER = 57193479
module = DESCRIPTOR.extensions_by_name['module']
_MODULEDESCRIPTOR = DESCRIPTOR.message_types_by_name['ModuleDescriptor']
_PACKAGEREFERENCE = DESCRIPTOR.message_types_by_name['PackageReference']
_MIGRATEFROMINFO = DESCRIPTOR.message_types_by_name['MigrateFromInfo']
ModuleDescriptor = _reflection.GeneratedProtocolMessageType('ModuleDescriptor', (_message.Message,), {'DESCRIPTOR': _MODULEDESCRIPTOR, '__module__': 'cosmos.app.v1alpha1.module_pb2'})
_sym_db.RegisterMessage(ModuleDescriptor)
PackageReference = _reflection.GeneratedProtocolMessageType('PackageReference', (_message.Message,), {'DESCRIPTOR': _PACKAGEREFERENCE, '__module__': 'cosmos.app.v1alpha1.module_pb2'})
_sym_db.RegisterMessage(PackageReference)
MigrateFromInfo = _reflection.GeneratedProtocolMessageType('MigrateFromInfo', (_message.Message,), {'DESCRIPTOR': _MIGRATEFROMINFO, '__module__': 'cosmos.app.v1alpha1.module_pb2'})
_sym_db.RegisterMessage(MigrateFromInfo)
if (_descriptor._USE_C_DESCRIPTORS == False):
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(module)
    DESCRIPTOR._options = None
    _MODULEDESCRIPTOR._serialized_start = 92
    _MODULEDESCRIPTOR._serialized_end = 253
    _PACKAGEREFERENCE._serialized_start = 255
    _PACKAGEREFERENCE._serialized_end = 305
    _MIGRATEFROMINFO._serialized_start = 307
    _MIGRATEFROMINFO._serialized_end = 340
