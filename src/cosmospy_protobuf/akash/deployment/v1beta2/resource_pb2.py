
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.base.v1beta2 import resourceunits_pb2 as akash_dot_base_dot_v1beta2_dot_resourceunits__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'akash/deployment/v1beta2/resource.proto\x12\x18akash.deployment.v1beta2\x1a\x14gogoproto/gogo.proto\x1a&akash/base/v1beta2/resourceunits.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\xd9\x01\n\x08Resource\x12Q\n\tresources\x18\x01 \x01(\x0b2!.akash.base.v1beta2.ResourceUnitsB\x1b\xc8\xde\x1f\x00\xea\xde\x1f\x04unit\xf2\xde\x1f\x0byaml:"unit"\x12(\n\x05count\x18\x02 \x01(\rB\x19\xea\xde\x1f\x05count\xf2\xde\x1f\x0cyaml:"count"\x12J\n\x05price\x18\x03 \x01(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB\x1d\xc8\xde\x1f\x00\xea\xde\x1f\x05price\xf2\xde\x1f\x0cyaml:"price":\x04\xe8\xa0\x1f\x00B4Z2github.com/ovrclk/akash/x/deployment/types/v1beta2b\x06proto3')
_RESOURCE = DESCRIPTOR.message_types_by_name['Resource']
Resource = _reflection.GeneratedProtocolMessageType('Resource', (_message.Message,), {'DESCRIPTOR': _RESOURCE, '__module__': 'akash.deployment.v1beta2.resource_pb2'})
_sym_db.RegisterMessage(Resource)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2github.com/ovrclk/akash/x/deployment/types/v1beta2'
    _RESOURCE.fields_by_name['resources']._options = None
    _RESOURCE.fields_by_name['resources']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x04unit\xf2\xde\x1f\x0byaml:"unit"'
    _RESOURCE.fields_by_name['count']._options = None
    _RESOURCE.fields_by_name['count']._serialized_options = b'\xea\xde\x1f\x05count\xf2\xde\x1f\x0cyaml:"count"'
    _RESOURCE.fields_by_name['price']._options = None
    _RESOURCE.fields_by_name['price']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x05price\xf2\xde\x1f\x0cyaml:"price"'
    _RESOURCE._options = None
    _RESOURCE._serialized_options = b'\xe8\xa0\x1f\x00'
    _RESOURCE._serialized_start = 164
    _RESOURCE._serialized_end = 381
