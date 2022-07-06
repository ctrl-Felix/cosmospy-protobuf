
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.base.v1beta2 import attribute_pb2 as akash_dot_base_dot_v1beta2_dot_attribute__pb2
from ....akash.deployment.v1beta2 import resource_pb2 as akash_dot_deployment_dot_v1beta2_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(akash/deployment/v1beta2/groupspec.proto\x12\x18akash.deployment.v1beta2\x1a\x14gogoproto/gogo.proto\x1a"akash/base/v1beta2/attribute.proto\x1a\'akash/deployment/v1beta2/resource.proto"\x88\x02\n\tGroupSpec\x12%\n\x04name\x18\x01 \x01(\tB\x17\xea\xde\x1f\x04name\xf2\xde\x1f\x0byaml:"name"\x12l\n\x0crequirements\x18\x02 \x01(\x0b2).akash.base.v1beta2.PlacementRequirementsB+\xc8\xde\x1f\x00\xea\xde\x1f\x0crequirements\xf2\xde\x1f\x13yaml:"requirements"\x12\\\n\tresources\x18\x03 \x03(\x0b2".akash.deployment.v1beta2.ResourceB%\xc8\xde\x1f\x00\xea\xde\x1f\tresources\xf2\xde\x1f\x10yaml:"resources":\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00B4Z2github.com/ovrclk/akash/x/deployment/types/v1beta2b\x06proto3')
_GROUPSPEC = DESCRIPTOR.message_types_by_name['GroupSpec']
GroupSpec = _reflection.GeneratedProtocolMessageType('GroupSpec', (_message.Message,), {'DESCRIPTOR': _GROUPSPEC, '__module__': 'akash.deployment.v1beta2.groupspec_pb2'})
_sym_db.RegisterMessage(GroupSpec)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2github.com/ovrclk/akash/x/deployment/types/v1beta2'
    _GROUPSPEC.fields_by_name['name']._options = None
    _GROUPSPEC.fields_by_name['name']._serialized_options = b'\xea\xde\x1f\x04name\xf2\xde\x1f\x0byaml:"name"'
    _GROUPSPEC.fields_by_name['requirements']._options = None
    _GROUPSPEC.fields_by_name['requirements']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x0crequirements\xf2\xde\x1f\x13yaml:"requirements"'
    _GROUPSPEC.fields_by_name['resources']._options = None
    _GROUPSPEC.fields_by_name['resources']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\tresources\xf2\xde\x1f\x10yaml:"resources"'
    _GROUPSPEC._options = None
    _GROUPSPEC._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _GROUPSPEC._serialized_start = 170
    _GROUPSPEC._serialized_end = 434
