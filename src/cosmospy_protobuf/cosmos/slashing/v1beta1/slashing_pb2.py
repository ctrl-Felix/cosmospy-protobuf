
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&cosmos/slashing/v1beta1/slashing.proto\x12\x17cosmos.slashing.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19cosmos_proto/cosmos.proto"\xe6\x01\n\x14ValidatorSigningInfo\x12)\n\x07address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12\x14\n\x0cstart_height\x18\x02 \x01(\x03\x12\x14\n\x0cindex_offset\x18\x03 \x01(\x03\x12:\n\x0cjailed_until\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\x90\xdf\x1f\x01\xc8\xde\x1f\x00\x12\x12\n\ntombstoned\x18\x05 \x01(\x08\x12\x1d\n\x15missed_blocks_counter\x18\x06 \x01(\x03:\x08\xe8\xa0\x1f\x01\x98\xa0\x1f\x00"\xdf\x02\n\x06Params\x12\x1c\n\x14signed_blocks_window\x18\x01 \x01(\x03\x12M\n\x15min_signed_per_window\x18\x02 \x01(\x0cB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12C\n\x16downtime_jail_duration\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12R\n\x1aslash_fraction_double_sign\x18\x04 \x01(\x0cB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12O\n\x17slash_fraction_downtime\x18\x05 \x01(\x0cB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00B3Z-github.com/cosmos/cosmos-sdk/x/slashing/types\xa8\xe2\x1e\x01b\x06proto3')
_VALIDATORSIGNINGINFO = DESCRIPTOR.message_types_by_name['ValidatorSigningInfo']
_PARAMS = DESCRIPTOR.message_types_by_name['Params']
ValidatorSigningInfo = _reflection.GeneratedProtocolMessageType('ValidatorSigningInfo', (_message.Message,), {'DESCRIPTOR': _VALIDATORSIGNINGINFO, '__module__': 'cosmos.slashing.v1beta1.slashing_pb2'})
_sym_db.RegisterMessage(ValidatorSigningInfo)
Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {'DESCRIPTOR': _PARAMS, '__module__': 'cosmos.slashing.v1beta1.slashing_pb2'})
_sym_db.RegisterMessage(Params)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z-github.com/cosmos/cosmos-sdk/x/slashing/types\xa8\xe2\x1e\x01'
    _VALIDATORSIGNINGINFO.fields_by_name['address']._options = None
    _VALIDATORSIGNINGINFO.fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _VALIDATORSIGNINGINFO.fields_by_name['jailed_until']._options = None
    _VALIDATORSIGNINGINFO.fields_by_name['jailed_until']._serialized_options = b'\x90\xdf\x1f\x01\xc8\xde\x1f\x00'
    _VALIDATORSIGNINGINFO._options = None
    _VALIDATORSIGNINGINFO._serialized_options = b'\xe8\xa0\x1f\x01\x98\xa0\x1f\x00'
    _PARAMS.fields_by_name['min_signed_per_window']._options = None
    _PARAMS.fields_by_name['min_signed_per_window']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['downtime_jail_duration']._options = None
    _PARAMS.fields_by_name['downtime_jail_duration']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _PARAMS.fields_by_name['slash_fraction_double_sign']._options = None
    _PARAMS.fields_by_name['slash_fraction_double_sign']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['slash_fraction_downtime']._options = None
    _PARAMS.fields_by_name['slash_fraction_downtime']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _VALIDATORSIGNINGINFO._serialized_start = 182
    _VALIDATORSIGNINGINFO._serialized_end = 412
    _PARAMS._serialized_start = 415
    _PARAMS._serialized_end = 766
