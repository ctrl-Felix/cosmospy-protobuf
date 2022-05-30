
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....umee.leverage.v1beta1 import leverage_pb2 as umee_dot_leverage_dot_v1beta1_dot_leverage__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fumee/leverage/v1beta1/gov.proto\x12!umeenetwork.umee.leverage.v1beta1\x1a\x14gogoproto/gogo.proto\x1a$umee/leverage/v1beta1/leverage.proto"\x8c\x01\n\x16UpdateRegistryProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12@\n\x08registry\x18\x03 \x03(\x0b2(.umeenetwork.umee.leverage.v1beta1.TokenB\x04\xc8\xde\x1f\x00:\x0c\xe8\xa0\x1f\x01\x88\xa0\x1f\x00\x98\xa0\x1f\x00B2Z0github.com/umee-network/umee/v2/x/leverage/typesb\x06proto3')
_UPDATEREGISTRYPROPOSAL = DESCRIPTOR.message_types_by_name['UpdateRegistryProposal']
UpdateRegistryProposal = _reflection.GeneratedProtocolMessageType('UpdateRegistryProposal', (_message.Message,), {'DESCRIPTOR': _UPDATEREGISTRYPROPOSAL, '__module__': 'umee.leverage.v1beta1.gov_pb2'})
_sym_db.RegisterMessage(UpdateRegistryProposal)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z0github.com/umee-network/umee/v2/x/leverage/types'
    _UPDATEREGISTRYPROPOSAL.fields_by_name['registry']._options = None
    _UPDATEREGISTRYPROPOSAL.fields_by_name['registry']._serialized_options = b'\xc8\xde\x1f\x00'
    _UPDATEREGISTRYPROPOSAL._options = None
    _UPDATEREGISTRYPROPOSAL._serialized_options = b'\xe8\xa0\x1f\x01\x88\xa0\x1f\x00\x98\xa0\x1f\x00'
    _UPDATEREGISTRYPROPOSAL._serialized_start = 131
    _UPDATEREGISTRYPROPOSAL._serialized_end = 271
