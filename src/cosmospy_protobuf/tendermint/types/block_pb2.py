
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ...tendermint.types import types_pb2 as tendermint_dot_types_dot_types__pb2
from ...tendermint.types import evidence_pb2 as tendermint_dot_types_dot_evidence__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ctendermint/types/block.proto\x12\x10tendermint.types\x1a\x14gogoproto/gogo.proto\x1a\x1ctendermint/types/types.proto\x1a\x1ftendermint/types/evidence.proto"\xca\x01\n\x05Block\x12.\n\x06header\x18\x01 \x01(\x0b2\x18.tendermint.types.HeaderB\x04\xc8\xde\x1f\x00\x12*\n\x04data\x18\x02 \x01(\x0b2\x16.tendermint.types.DataB\x04\xc8\xde\x1f\x00\x126\n\x08evidence\x18\x03 \x01(\x0b2\x1e.tendermint.types.EvidenceListB\x04\xc8\xde\x1f\x00\x12-\n\x0blast_commit\x18\x04 \x01(\x0b2\x18.tendermint.types.CommitB9Z7github.com/tendermint/tendermint/proto/tendermint/typesb\x06proto3')
_BLOCK = DESCRIPTOR.message_types_by_name['Block']
Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), {'DESCRIPTOR': _BLOCK, '__module__': 'tendermint.types.block_pb2'})
_sym_db.RegisterMessage(Block)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z7github.com/tendermint/tendermint/proto/tendermint/types'
    _BLOCK.fields_by_name['header']._options = None
    _BLOCK.fields_by_name['header']._serialized_options = b'\xc8\xde\x1f\x00'
    _BLOCK.fields_by_name['data']._options = None
    _BLOCK.fields_by_name['data']._serialized_options = b'\xc8\xde\x1f\x00'
    _BLOCK.fields_by_name['evidence']._options = None
    _BLOCK.fields_by_name['evidence']._serialized_options = b'\xc8\xde\x1f\x00'
    _BLOCK._serialized_start = 136
    _BLOCK._serialized_end = 338
