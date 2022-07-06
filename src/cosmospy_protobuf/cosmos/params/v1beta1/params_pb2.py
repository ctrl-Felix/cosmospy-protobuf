
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"cosmos/params/v1beta1/params.proto\x12\x15cosmos.params.v1beta1\x1a\x14gogoproto/gogo.proto"\x82\x01\n\x17ParameterChangeProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x129\n\x07changes\x18\x03 \x03(\x0b2".cosmos.params.v1beta1.ParamChangeB\x04\xc8\xde\x1f\x00:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00"A\n\x0bParamChange\x12\x10\n\x08subspace\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t:\x04\x98\xa0\x1f\x00B:Z4github.com/cosmos/cosmos-sdk/x/params/types/proposal\xa8\xe2\x1e\x01b\x06proto3')
_PARAMETERCHANGEPROPOSAL = DESCRIPTOR.message_types_by_name['ParameterChangeProposal']
_PARAMCHANGE = DESCRIPTOR.message_types_by_name['ParamChange']
ParameterChangeProposal = _reflection.GeneratedProtocolMessageType('ParameterChangeProposal', (_message.Message,), {'DESCRIPTOR': _PARAMETERCHANGEPROPOSAL, '__module__': 'cosmos.params.v1beta1.params_pb2'})
_sym_db.RegisterMessage(ParameterChangeProposal)
ParamChange = _reflection.GeneratedProtocolMessageType('ParamChange', (_message.Message,), {'DESCRIPTOR': _PARAMCHANGE, '__module__': 'cosmos.params.v1beta1.params_pb2'})
_sym_db.RegisterMessage(ParamChange)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z4github.com/cosmos/cosmos-sdk/x/params/types/proposal\xa8\xe2\x1e\x01'
    _PARAMETERCHANGEPROPOSAL.fields_by_name['changes']._options = None
    _PARAMETERCHANGEPROPOSAL.fields_by_name['changes']._serialized_options = b'\xc8\xde\x1f\x00'
    _PARAMETERCHANGEPROPOSAL._options = None
    _PARAMETERCHANGEPROPOSAL._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00'
    _PARAMCHANGE._options = None
    _PARAMCHANGE._serialized_options = b'\x98\xa0\x1f\x00'
    _PARAMETERCHANGEPROPOSAL._serialized_start = 84
    _PARAMETERCHANGEPROPOSAL._serialized_end = 214
    _PARAMCHANGE._serialized_start = 216
    _PARAMCHANGE._serialized_end = 281
