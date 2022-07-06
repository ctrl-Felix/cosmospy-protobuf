
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....osmosis.tokenfactory.v1beta1 import authorityMetadata_pb2 as osmosis_dot_tokenfactory_dot_v1beta1_dot_authorityMetadata__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*osmosis/tokenfactory/v1beta1/genesis.proto\x12\x1cosmosis.tokenfactory.v1beta1\x1a\x14gogoproto/gogo.proto\x1a4osmosis/tokenfactory/v1beta1/authorityMetadata.proto"w\n\x0cGenesisState\x12a\n\x0efactory_denoms\x18\x01 \x03(\x0b2*.osmosis.tokenfactory.v1beta1.GenesisDenomB\x1d\xf2\xde\x1f\x15yaml:"factory_denoms"\xc8\xde\x1f\x00:\x04\xe8\xa0\x1f\x01"\xaa\x01\n\x0cGenesisDenom\x12\x1f\n\x05denom\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"denom"\x12s\n\x12authority_metadata\x18\x02 \x01(\x0b24.osmosis.tokenfactory.v1beta1.DenomAuthorityMetadataB!\xf2\xde\x1f\x19yaml:"authority_metadata"\xc8\xde\x1f\x00:\x04\xe8\xa0\x1f\x01B9Z7github.com/osmosis-labs/osmosis/v7/x/tokenfactory/typesb\x06proto3')
_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
_GENESISDENOM = DESCRIPTOR.message_types_by_name['GenesisDenom']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {'DESCRIPTOR': _GENESISSTATE, '__module__': 'osmosis.tokenfactory.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(GenesisState)
GenesisDenom = _reflection.GeneratedProtocolMessageType('GenesisDenom', (_message.Message,), {'DESCRIPTOR': _GENESISDENOM, '__module__': 'osmosis.tokenfactory.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(GenesisDenom)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z7github.com/osmosis-labs/osmosis/v7/x/tokenfactory/types'
    _GENESISSTATE.fields_by_name['factory_denoms']._options = None
    _GENESISSTATE.fields_by_name['factory_denoms']._serialized_options = b'\xf2\xde\x1f\x15yaml:"factory_denoms"\xc8\xde\x1f\x00'
    _GENESISSTATE._options = None
    _GENESISSTATE._serialized_options = b'\xe8\xa0\x1f\x01'
    _GENESISDENOM.fields_by_name['denom']._options = None
    _GENESISDENOM.fields_by_name['denom']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"denom"'
    _GENESISDENOM.fields_by_name['authority_metadata']._options = None
    _GENESISDENOM.fields_by_name['authority_metadata']._serialized_options = b'\xf2\xde\x1f\x19yaml:"authority_metadata"\xc8\xde\x1f\x00'
    _GENESISDENOM._options = None
    _GENESISDENOM._serialized_options = b'\xe8\xa0\x1f\x01'
    _GENESISSTATE._serialized_start = 152
    _GENESISSTATE._serialized_end = 271
    _GENESISDENOM._serialized_start = 274
    _GENESISDENOM._serialized_end = 444
