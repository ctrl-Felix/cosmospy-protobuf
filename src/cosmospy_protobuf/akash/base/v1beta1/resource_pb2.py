
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.base.v1beta1 import attribute_pb2 as akash_dot_base_dot_v1beta1_dot_attribute__pb2
from ....akash.base.v1beta1 import resourcevalue_pb2 as akash_dot_base_dot_v1beta1_dot_resourcevalue__pb2
from ....akash.base.v1beta1 import endpoint_pb2 as akash_dot_base_dot_v1beta1_dot_endpoint__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!akash/base/v1beta1/resource.proto\x12\x12akash.base.v1beta1\x1a\x14gogoproto/gogo.proto\x1a"akash/base/v1beta1/attribute.proto\x1a&akash/base/v1beta1/resourcevalue.proto\x1a!akash/base/v1beta1/endpoint.proto"\xac\x01\n\x03CPU\x126\n\x05units\x18\x01 \x01(\x0b2!.akash.base.v1beta1.ResourceValueB\x04\xc8\xde\x1f\x00\x12g\n\nattributes\x18\x02 \x03(\x0b2\x1d.akash.base.v1beta1.AttributeB4\xc8\xde\x1f\x00\xea\xde\x1f\x14attributes,omitempty\xf2\xde\x1f\x14yaml:"cpu,omitempty":\x04\xe8\xa0\x1f\x01"\xc9\x01\n\x06Memory\x12P\n\x08quantity\x18\x01 \x01(\x0b2!.akash.base.v1beta1.ResourceValueB\x1b\xc8\xde\x1f\x00\xea\xde\x1f\x04size\xf2\xde\x1f\x0byaml:"size"\x12g\n\nattributes\x18\x02 \x03(\x0b2\x1d.akash.base.v1beta1.AttributeB4\xc8\xde\x1f\x00\xea\xde\x1f\x14attributes,omitempty\xf2\xde\x1f\x14yaml:"cpu,omitempty":\x04\xe8\xa0\x1f\x01"\xca\x01\n\x07Storage\x12P\n\x08quantity\x18\x01 \x01(\x0b2!.akash.base.v1beta1.ResourceValueB\x1b\xc8\xde\x1f\x00\xea\xde\x1f\x04size\xf2\xde\x1f\x0byaml:"size"\x12g\n\nattributes\x18\x02 \x03(\x0b2\x1d.akash.base.v1beta1.AttributeB4\xc8\xde\x1f\x00\xea\xde\x1f\x14attributes,omitempty\xf2\xde\x1f\x14yaml:"cpu,omitempty":\x04\xe8\xa0\x1f\x01"\x8f\x03\n\rResourceUnits\x12Z\n\x03cpu\x18\x01 \x01(\x0b2\x17.akash.base.v1beta1.CPUB4\xc8\xde\x1f\x01\xe2\xde\x1f\x03CPU\xea\xde\x1f\rcpu,omitempty\xf2\xde\x1f\x14yaml:"cpu,omitempty"\x12_\n\x06memory\x18\x02 \x01(\x0b2\x1a.akash.base.v1beta1.MemoryB3\xc8\xde\x1f\x01\xea\xde\x1f\x10memory,omitempty\xf2\xde\x1f\x17yaml:"memory,omitempty"\x12c\n\x07storage\x18\x03 \x01(\x0b2\x1b.akash.base.v1beta1.StorageB5\xc8\xde\x1f\x01\xea\xde\x1f\x11storage,omitempty\xf2\xde\x1f\x18yaml:"storage,omitempty"\x12V\n\tendpoints\x18\x04 \x03(\x0b2\x1c.akash.base.v1beta1.EndpointB%\xc8\xde\x1f\x00\xea\xde\x1f\tendpoints\xf2\xde\x1f\x10yaml:"endpoints":\x04\xe8\xa0\x1f\x01B\'Z%github.com/ovrclk/akash/types/v1beta1b\x06proto3')
_CPU = DESCRIPTOR.message_types_by_name['CPU']
_MEMORY = DESCRIPTOR.message_types_by_name['Memory']
_STORAGE = DESCRIPTOR.message_types_by_name['Storage']
_RESOURCEUNITS = DESCRIPTOR.message_types_by_name['ResourceUnits']
CPU = _reflection.GeneratedProtocolMessageType('CPU', (_message.Message,), {'DESCRIPTOR': _CPU, '__module__': 'akash.base.v1beta1.resource_pb2'})
_sym_db.RegisterMessage(CPU)
Memory = _reflection.GeneratedProtocolMessageType('Memory', (_message.Message,), {'DESCRIPTOR': _MEMORY, '__module__': 'akash.base.v1beta1.resource_pb2'})
_sym_db.RegisterMessage(Memory)
Storage = _reflection.GeneratedProtocolMessageType('Storage', (_message.Message,), {'DESCRIPTOR': _STORAGE, '__module__': 'akash.base.v1beta1.resource_pb2'})
_sym_db.RegisterMessage(Storage)
ResourceUnits = _reflection.GeneratedProtocolMessageType('ResourceUnits', (_message.Message,), {'DESCRIPTOR': _RESOURCEUNITS, '__module__': 'akash.base.v1beta1.resource_pb2'})
_sym_db.RegisterMessage(ResourceUnits)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z%github.com/ovrclk/akash/types/v1beta1'
    _CPU.fields_by_name['units']._options = None
    _CPU.fields_by_name['units']._serialized_options = b'\xc8\xde\x1f\x00'
    _CPU.fields_by_name['attributes']._options = None
    _CPU.fields_by_name['attributes']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x14attributes,omitempty\xf2\xde\x1f\x14yaml:"cpu,omitempty"'
    _CPU._options = None
    _CPU._serialized_options = b'\xe8\xa0\x1f\x01'
    _MEMORY.fields_by_name['quantity']._options = None
    _MEMORY.fields_by_name['quantity']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x04size\xf2\xde\x1f\x0byaml:"size"'
    _MEMORY.fields_by_name['attributes']._options = None
    _MEMORY.fields_by_name['attributes']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x14attributes,omitempty\xf2\xde\x1f\x14yaml:"cpu,omitempty"'
    _MEMORY._options = None
    _MEMORY._serialized_options = b'\xe8\xa0\x1f\x01'
    _STORAGE.fields_by_name['quantity']._options = None
    _STORAGE.fields_by_name['quantity']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x04size\xf2\xde\x1f\x0byaml:"size"'
    _STORAGE.fields_by_name['attributes']._options = None
    _STORAGE.fields_by_name['attributes']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x14attributes,omitempty\xf2\xde\x1f\x14yaml:"cpu,omitempty"'
    _STORAGE._options = None
    _STORAGE._serialized_options = b'\xe8\xa0\x1f\x01'
    _RESOURCEUNITS.fields_by_name['cpu']._options = None
    _RESOURCEUNITS.fields_by_name['cpu']._serialized_options = b'\xc8\xde\x1f\x01\xe2\xde\x1f\x03CPU\xea\xde\x1f\rcpu,omitempty\xf2\xde\x1f\x14yaml:"cpu,omitempty"'
    _RESOURCEUNITS.fields_by_name['memory']._options = None
    _RESOURCEUNITS.fields_by_name['memory']._serialized_options = b'\xc8\xde\x1f\x01\xea\xde\x1f\x10memory,omitempty\xf2\xde\x1f\x17yaml:"memory,omitempty"'
    _RESOURCEUNITS.fields_by_name['storage']._options = None
    _RESOURCEUNITS.fields_by_name['storage']._serialized_options = b'\xc8\xde\x1f\x01\xea\xde\x1f\x11storage,omitempty\xf2\xde\x1f\x18yaml:"storage,omitempty"'
    _RESOURCEUNITS.fields_by_name['endpoints']._options = None
    _RESOURCEUNITS.fields_by_name['endpoints']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\tendpoints\xf2\xde\x1f\x10yaml:"endpoints"'
    _RESOURCEUNITS._options = None
    _RESOURCEUNITS._serialized_options = b'\xe8\xa0\x1f\x01'
    _CPU._serialized_start = 191
    _CPU._serialized_end = 363
    _MEMORY._serialized_start = 366
    _MEMORY._serialized_end = 567
    _STORAGE._serialized_start = 570
    _STORAGE._serialized_end = 772
    _RESOURCEUNITS._serialized_start = 775
    _RESOURCEUNITS._serialized_end = 1174
