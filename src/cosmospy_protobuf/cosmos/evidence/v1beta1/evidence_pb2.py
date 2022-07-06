
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&cosmos/evidence/v1beta1/evidence.proto\x12\x17cosmos.evidence.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19cosmos_proto/cosmos.proto"\xa4\x01\n\x0cEquivocation\x12\x0e\n\x06height\x18\x01 \x01(\x03\x122\n\x04time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\r\n\x05power\x18\x03 \x01(\x03\x123\n\x11consensus_address\x18\x04 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\x0c\x98\xa0\x1f\x00\x88\xa0\x1f\x00\xe8\xa0\x1f\x00B3Z-github.com/cosmos/cosmos-sdk/x/evidence/types\xa8\xe2\x1e\x01b\x06proto3')
_EQUIVOCATION = DESCRIPTOR.message_types_by_name['Equivocation']
Equivocation = _reflection.GeneratedProtocolMessageType('Equivocation', (_message.Message,), {'DESCRIPTOR': _EQUIVOCATION, '__module__': 'cosmos.evidence.v1beta1.evidence_pb2'})
_sym_db.RegisterMessage(Equivocation)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z-github.com/cosmos/cosmos-sdk/x/evidence/types\xa8\xe2\x1e\x01'
    _EQUIVOCATION.fields_by_name['time']._options = None
    _EQUIVOCATION.fields_by_name['time']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _EQUIVOCATION.fields_by_name['consensus_address']._options = None
    _EQUIVOCATION.fields_by_name['consensus_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _EQUIVOCATION._options = None
    _EQUIVOCATION._serialized_options = b'\x98\xa0\x1f\x00\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _EQUIVOCATION._serialized_start = 150
    _EQUIVOCATION._serialized_end = 314
