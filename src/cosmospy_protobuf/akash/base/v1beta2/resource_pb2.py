
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.base.v1beta2 import attribute_pb2 as akash_dot_base_dot_v1beta2_dot_attribute__pb2
from ....akash.base.v1beta2 import resourcevalue_pb2 as akash_dot_base_dot_v1beta2_dot_resourcevalue__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!akash/base/v1beta2/resource.proto\x12\x12akash.base.v1beta2\x1a\x14gogoproto/gogo.proto\x1a"akash/base/v1beta2/attribute.proto\x1a&akash/base/v1beta2/resourcevalue.proto"\xc1\x01\n\x03CPU\x126\n\x05units\x18\x01 \x01(\x0b2!.akash.base.v1beta2.ResourceValueB\x04\xc8\xde\x1f\x00\x12|\n\nattributes\x18\x02 \x03(\x0b2\x1d.akash.base.v1beta2.AttributeBI\xc8\xde\x1f\x00\xaa\xdf\x1f\nAttributes\xea\xde\x1f\x14attributes,omitempty\xf2\xde\x1f\x1byaml:"attributes,omitempty":\x04\xe8\xa0\x1f\x01"\xde\x01\n\x06Memory\x12P\n\x08quantity\x18\x01 \x01(\x0b2!.akash.base.v1beta2.ResourceValueB\x1b\xc8\xde\x1f\x00\xea\xde\x1f\x04size\xf2\xde\x1f\x0byaml:"size"\x12|\n\nattributes\x18\x02 \x03(\x0b2\x1d.akash.base.v1beta2.AttributeBI\xc8\xde\x1f\x00\xaa\xdf\x1f\nAttributes\xea\xde\x1f\x14attributes,omitempty\xf2\xde\x1f\x1byaml:"attributes,omitempty":\x04\xe8\xa0\x1f\x01"\x86\x02\n\x07Storage\x12%\n\x04name\x18\x01 \x01(\tB\x17\xea\xde\x1f\x04name\xf2\xde\x1f\x0byaml:"name"\x12P\n\x08quantity\x18\x02 \x01(\x0b2!.akash.base.v1beta2.ResourceValueB\x1b\xc8\xde\x1f\x00\xea\xde\x1f\x04size\xf2\xde\x1f\x0byaml:"size"\x12|\n\nattributes\x18\x03 \x03(\x0b2\x1d.akash.base.v1beta2.AttributeBI\xc8\xde\x1f\x00\xaa\xdf\x1f\nAttributes\xea\xde\x1f\x14attributes,omitempty\xf2\xde\x1f\x1byaml:"attributes,omitempty":\x04\xe8\xa0\x1f\x01B\'Z%github.com/ovrclk/akash/types/v1beta2b\x06proto3')
_CPU = DESCRIPTOR.message_types_by_name['CPU']
_MEMORY = DESCRIPTOR.message_types_by_name['Memory']
_STORAGE = DESCRIPTOR.message_types_by_name['Storage']
CPU = _reflection.GeneratedProtocolMessageType('CPU', (_message.Message,), {'DESCRIPTOR': _CPU, '__module__': 'akash.base.v1beta2.resource_pb2'})
_sym_db.RegisterMessage(CPU)
Memory = _reflection.GeneratedProtocolMessageType('Memory', (_message.Message,), {'DESCRIPTOR': _MEMORY, '__module__': 'akash.base.v1beta2.resource_pb2'})
_sym_db.RegisterMessage(Memory)
Storage = _reflection.GeneratedProtocolMessageType('Storage', (_message.Message,), {'DESCRIPTOR': _STORAGE, '__module__': 'akash.base.v1beta2.resource_pb2'})
_sym_db.RegisterMessage(Storage)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z%github.com/ovrclk/akash/types/v1beta2'
    _CPU.fields_by_name['units']._options = None
    _CPU.fields_by_name['units']._serialized_options = b'\xc8\xde\x1f\x00'
    _CPU.fields_by_name['attributes']._options = None
    _CPU.fields_by_name['attributes']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f\nAttributes\xea\xde\x1f\x14attributes,omitempty\xf2\xde\x1f\x1byaml:"attributes,omitempty"'
    _CPU._options = None
    _CPU._serialized_options = b'\xe8\xa0\x1f\x01'
    _MEMORY.fields_by_name['quantity']._options = None
    _MEMORY.fields_by_name['quantity']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x04size\xf2\xde\x1f\x0byaml:"size"'
    _MEMORY.fields_by_name['attributes']._options = None
    _MEMORY.fields_by_name['attributes']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f\nAttributes\xea\xde\x1f\x14attributes,omitempty\xf2\xde\x1f\x1byaml:"attributes,omitempty"'
    _MEMORY._options = None
    _MEMORY._serialized_options = b'\xe8\xa0\x1f\x01'
    _STORAGE.fields_by_name['name']._options = None
    _STORAGE.fields_by_name['name']._serialized_options = b'\xea\xde\x1f\x04name\xf2\xde\x1f\x0byaml:"name"'
    _STORAGE.fields_by_name['quantity']._options = None
    _STORAGE.fields_by_name['quantity']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x04size\xf2\xde\x1f\x0byaml:"size"'
    _STORAGE.fields_by_name['attributes']._options = None
    _STORAGE.fields_by_name['attributes']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f\nAttributes\xea\xde\x1f\x14attributes,omitempty\xf2\xde\x1f\x1byaml:"attributes,omitempty"'
    _STORAGE._options = None
    _STORAGE._serialized_options = b'\xe8\xa0\x1f\x01'
    _CPU._serialized_start = 156
    _CPU._serialized_end = 349
    _MEMORY._serialized_start = 352
    _MEMORY._serialized_end = 574
    _STORAGE._serialized_start = 577
    _STORAGE._serialized_end = 839
