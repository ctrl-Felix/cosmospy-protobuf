
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4osmosis/tokenfactory/v1beta1/authorityMetadata.proto\x12\x1cosmosis.tokenfactory.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"?\n\x16DenomAuthorityMetadata\x12\x1f\n\x05Admin\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"admin":\x04\xe8\xa0\x1f\x01B9Z7github.com/osmosis-labs/osmosis/v7/x/tokenfactory/typesb\x06proto3')
_DENOMAUTHORITYMETADATA = DESCRIPTOR.message_types_by_name['DenomAuthorityMetadata']
DenomAuthorityMetadata = _reflection.GeneratedProtocolMessageType('DenomAuthorityMetadata', (_message.Message,), {'DESCRIPTOR': _DENOMAUTHORITYMETADATA, '__module__': 'osmosis.tokenfactory.v1beta1.authorityMetadata_pb2'})
_sym_db.RegisterMessage(DenomAuthorityMetadata)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z7github.com/osmosis-labs/osmosis/v7/x/tokenfactory/types'
    _DENOMAUTHORITYMETADATA.fields_by_name['Admin']._options = None
    _DENOMAUTHORITYMETADATA.fields_by_name['Admin']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"admin"'
    _DENOMAUTHORITYMETADATA._options = None
    _DENOMAUTHORITYMETADATA._serialized_options = b'\xe8\xa0\x1f\x01'
    _DENOMAUTHORITYMETADATA._serialized_start = 140
    _DENOMAUTHORITYMETADATA._serialized_end = 203
