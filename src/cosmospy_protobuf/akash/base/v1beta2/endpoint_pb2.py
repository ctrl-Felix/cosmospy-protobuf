
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!akash/base/v1beta2/endpoint.proto\x12\x12akash.base.v1beta2\x1a\x14gogoproto/gogo.proto"\xd4\x01\n\x08Endpoint\x12/\n\x04kind\x18\x01 \x01(\x0e2!.akash.base.v1beta2.Endpoint.Kind\x12X\n\x0fsequence_number\x18\x02 \x01(\rB?\xe2\xde\x1f\x0eSequenceNumber\xea\xde\x1f\x0fsequence_number\xf2\xde\x1f\x16yaml:"sequence_number""7\n\x04Kind\x12\x0f\n\x0bSHARED_HTTP\x10\x00\x12\x0f\n\x0bRANDOM_PORT\x10\x01\x12\r\n\tLEASED_IP\x10\x02:\x04\xe8\xa0\x1f\x01B\'Z%github.com/ovrclk/akash/types/v1beta2b\x06proto3')
_ENDPOINT = DESCRIPTOR.message_types_by_name['Endpoint']
_ENDPOINT_KIND = _ENDPOINT.enum_types_by_name['Kind']
Endpoint = _reflection.GeneratedProtocolMessageType('Endpoint', (_message.Message,), {'DESCRIPTOR': _ENDPOINT, '__module__': 'akash.base.v1beta2.endpoint_pb2'})
_sym_db.RegisterMessage(Endpoint)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z%github.com/ovrclk/akash/types/v1beta2'
    _ENDPOINT.fields_by_name['sequence_number']._options = None
    _ENDPOINT.fields_by_name['sequence_number']._serialized_options = b'\xe2\xde\x1f\x0eSequenceNumber\xea\xde\x1f\x0fsequence_number\xf2\xde\x1f\x16yaml:"sequence_number"'
    _ENDPOINT._options = None
    _ENDPOINT._serialized_options = b'\xe8\xa0\x1f\x01'
    _ENDPOINT._serialized_start = 80
    _ENDPOINT._serialized_end = 292
    _ENDPOINT_KIND._serialized_start = 231
    _ENDPOINT_KIND._serialized_end = 286
