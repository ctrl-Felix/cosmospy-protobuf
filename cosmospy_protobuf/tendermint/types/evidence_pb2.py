
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ...tendermint.types import types_pb2 as tendermint_dot_types_dot_types__pb2
from ...tendermint.types import validator_pb2 as tendermint_dot_types_dot_validator__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ftendermint/types/evidence.proto\x12\x10tendermint.types\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1ctendermint/types/types.proto\x1a tendermint/types/validator.proto"\xb2\x01\n\x08Evidence\x12J\n\x17duplicate_vote_evidence\x18\x01 \x01(\x0b2\'.tendermint.types.DuplicateVoteEvidenceH\x00\x12S\n\x1clight_client_attack_evidence\x18\x02 \x01(\x0b2+.tendermint.types.LightClientAttackEvidenceH\x00B\x05\n\x03sum"\xd5\x01\n\x15DuplicateVoteEvidence\x12&\n\x06vote_a\x18\x01 \x01(\x0b2\x16.tendermint.types.Vote\x12&\n\x06vote_b\x18\x02 \x01(\x0b2\x16.tendermint.types.Vote\x12\x1a\n\x12total_voting_power\x18\x03 \x01(\x03\x12\x17\n\x0fvalidator_power\x18\x04 \x01(\x03\x127\n\ttimestamp\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01"\xfb\x01\n\x19LightClientAttackEvidence\x127\n\x11conflicting_block\x18\x01 \x01(\x0b2\x1c.tendermint.types.LightBlock\x12\x15\n\rcommon_height\x18\x02 \x01(\x03\x129\n\x14byzantine_validators\x18\x03 \x03(\x0b2\x1b.tendermint.types.Validator\x12\x1a\n\x12total_voting_power\x18\x04 \x01(\x03\x127\n\ttimestamp\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01"B\n\x0cEvidenceList\x122\n\x08evidence\x18\x01 \x03(\x0b2\x1a.tendermint.types.EvidenceB\x04\xc8\xde\x1f\x00B9Z7github.com/tendermint/tendermint/proto/tendermint/typesb\x06proto3')
_EVIDENCE = DESCRIPTOR.message_types_by_name['Evidence']
_DUPLICATEVOTEEVIDENCE = DESCRIPTOR.message_types_by_name['DuplicateVoteEvidence']
_LIGHTCLIENTATTACKEVIDENCE = DESCRIPTOR.message_types_by_name['LightClientAttackEvidence']
_EVIDENCELIST = DESCRIPTOR.message_types_by_name['EvidenceList']
Evidence = _reflection.GeneratedProtocolMessageType('Evidence', (_message.Message,), {'DESCRIPTOR': _EVIDENCE, '__module__': 'tendermint.types.evidence_pb2'})
_sym_db.RegisterMessage(Evidence)
DuplicateVoteEvidence = _reflection.GeneratedProtocolMessageType('DuplicateVoteEvidence', (_message.Message,), {'DESCRIPTOR': _DUPLICATEVOTEEVIDENCE, '__module__': 'tendermint.types.evidence_pb2'})
_sym_db.RegisterMessage(DuplicateVoteEvidence)
LightClientAttackEvidence = _reflection.GeneratedProtocolMessageType('LightClientAttackEvidence', (_message.Message,), {'DESCRIPTOR': _LIGHTCLIENTATTACKEVIDENCE, '__module__': 'tendermint.types.evidence_pb2'})
_sym_db.RegisterMessage(LightClientAttackEvidence)
EvidenceList = _reflection.GeneratedProtocolMessageType('EvidenceList', (_message.Message,), {'DESCRIPTOR': _EVIDENCELIST, '__module__': 'tendermint.types.evidence_pb2'})
_sym_db.RegisterMessage(EvidenceList)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z7github.com/tendermint/tendermint/proto/tendermint/types'
    _DUPLICATEVOTEEVIDENCE.fields_by_name['timestamp']._options = None
    _DUPLICATEVOTEEVIDENCE.fields_by_name['timestamp']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _LIGHTCLIENTATTACKEVIDENCE.fields_by_name['timestamp']._options = None
    _LIGHTCLIENTATTACKEVIDENCE.fields_by_name['timestamp']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _EVIDENCELIST.fields_by_name['evidence']._options = None
    _EVIDENCELIST.fields_by_name['evidence']._serialized_options = b'\xc8\xde\x1f\x00'
    _EVIDENCE._serialized_start = 173
    _EVIDENCE._serialized_end = 351
    _DUPLICATEVOTEEVIDENCE._serialized_start = 354
    _DUPLICATEVOTEEVIDENCE._serialized_end = 567
    _LIGHTCLIENTATTACKEVIDENCE._serialized_start = 570
    _LIGHTCLIENTATTACKEVIDENCE._serialized_end = 821
    _EVIDENCELIST._serialized_start = 823
    _EVIDENCELIST._serialized_end = 889
