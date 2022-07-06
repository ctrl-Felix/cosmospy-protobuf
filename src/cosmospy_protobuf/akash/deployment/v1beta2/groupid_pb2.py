
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&akash/deployment/v1beta2/groupid.proto\x12\x18akash.deployment.v1beta2\x1a\x14gogoproto/gogo.proto"\x9b\x01\n\x07GroupID\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12-\n\x04dseq\x18\x02 \x01(\x04B\x1f\xe2\xde\x1f\x04DSeq\xea\xde\x1f\x04dseq\xf2\xde\x1f\x0byaml:"dseq"\x12-\n\x04gseq\x18\x03 \x01(\rB\x1f\xe2\xde\x1f\x04GSeq\xea\xde\x1f\x04gseq\xf2\xde\x1f\x0byaml:"gseq":\x08\xe8\xa0\x1f\x00\x98\xa0\x1f\x00B4Z2github.com/ovrclk/akash/x/deployment/types/v1beta2b\x06proto3')
_GROUPID = DESCRIPTOR.message_types_by_name['GroupID']
GroupID = _reflection.GeneratedProtocolMessageType('GroupID', (_message.Message,), {'DESCRIPTOR': _GROUPID, '__module__': 'akash.deployment.v1beta2.groupid_pb2'})
_sym_db.RegisterMessage(GroupID)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2github.com/ovrclk/akash/x/deployment/types/v1beta2'
    _GROUPID.fields_by_name['owner']._options = None
    _GROUPID.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _GROUPID.fields_by_name['dseq']._options = None
    _GROUPID.fields_by_name['dseq']._serialized_options = b'\xe2\xde\x1f\x04DSeq\xea\xde\x1f\x04dseq\xf2\xde\x1f\x0byaml:"dseq"'
    _GROUPID.fields_by_name['gseq']._options = None
    _GROUPID.fields_by_name['gseq']._serialized_options = b'\xe2\xde\x1f\x04GSeq\xea\xde\x1f\x04gseq\xf2\xde\x1f\x0byaml:"gseq"'
    _GROUPID._options = None
    _GROUPID._serialized_options = b'\xe8\xa0\x1f\x00\x98\xa0\x1f\x00'
    _GROUPID._serialized_start = 91
    _GROUPID._serialized_end = 246
