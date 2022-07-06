
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&akash/base/v1beta1/resourcevalue.proto\x12\x12akash.base.v1beta1\x1a\x14gogoproto/gogo.proto"R\n\rResourceValue\x12;\n\x03val\x18\x01 \x01(\x0cB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int:\x04\xe8\xa0\x1f\x01B\'Z%github.com/ovrclk/akash/types/v1beta1b\x06proto3')
_RESOURCEVALUE = DESCRIPTOR.message_types_by_name['ResourceValue']
ResourceValue = _reflection.GeneratedProtocolMessageType('ResourceValue', (_message.Message,), {'DESCRIPTOR': _RESOURCEVALUE, '__module__': 'akash.base.v1beta1.resourcevalue_pb2'})
_sym_db.RegisterMessage(ResourceValue)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z%github.com/ovrclk/akash/types/v1beta1'
    _RESOURCEVALUE.fields_by_name['val']._options = None
    _RESOURCEVALUE.fields_by_name['val']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _RESOURCEVALUE._options = None
    _RESOURCEVALUE._serialized_options = b'\xe8\xa0\x1f\x01'
    _RESOURCEVALUE._serialized_start = 84
    _RESOURCEVALUE._serialized_end = 166
