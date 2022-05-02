
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.slashing.v1beta1 import slashing_pb2 as cosmos_dot_slashing_dot_v1beta1_dot_slashing__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%cosmos/slashing/v1beta1/genesis.proto\x12\x17cosmos.slashing.v1beta1\x1a\x14gogoproto/gogo.proto\x1a&cosmos/slashing/v1beta1/slashing.proto\x1a\x19cosmos_proto/cosmos.proto"\xd5\x01\n\x0cGenesisState\x125\n\x06params\x18\x01 \x01(\x0b2\x1f.cosmos.slashing.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12A\n\rsigning_infos\x18\x02 \x03(\x0b2$.cosmos.slashing.v1beta1.SigningInfoB\x04\xc8\xde\x1f\x00\x12K\n\rmissed_blocks\x18\x03 \x03(\x0b2..cosmos.slashing.v1beta1.ValidatorMissedBlocksB\x04\xc8\xde\x1f\x00"\x8d\x01\n\x0bSigningInfo\x12)\n\x07address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12S\n\x16validator_signing_info\x18\x02 \x01(\x0b2-.cosmos.slashing.v1beta1.ValidatorSigningInfoB\x04\xc8\xde\x1f\x00"\x85\x01\n\x15ValidatorMissedBlocks\x12)\n\x07address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12A\n\rmissed_blocks\x18\x02 \x03(\x0b2$.cosmos.slashing.v1beta1.MissedBlockB\x04\xc8\xde\x1f\x00",\n\x0bMissedBlock\x12\r\n\x05index\x18\x01 \x01(\x03\x12\x0e\n\x06missed\x18\x02 \x01(\x08B/Z-github.com/cosmos/cosmos-sdk/x/slashing/typesb\x06proto3')
_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
_SIGNINGINFO = DESCRIPTOR.message_types_by_name['SigningInfo']
_VALIDATORMISSEDBLOCKS = DESCRIPTOR.message_types_by_name['ValidatorMissedBlocks']
_MISSEDBLOCK = DESCRIPTOR.message_types_by_name['MissedBlock']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {'DESCRIPTOR': _GENESISSTATE, '__module__': 'cosmos.slashing.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(GenesisState)
SigningInfo = _reflection.GeneratedProtocolMessageType('SigningInfo', (_message.Message,), {'DESCRIPTOR': _SIGNINGINFO, '__module__': 'cosmos.slashing.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(SigningInfo)
ValidatorMissedBlocks = _reflection.GeneratedProtocolMessageType('ValidatorMissedBlocks', (_message.Message,), {'DESCRIPTOR': _VALIDATORMISSEDBLOCKS, '__module__': 'cosmos.slashing.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(ValidatorMissedBlocks)
MissedBlock = _reflection.GeneratedProtocolMessageType('MissedBlock', (_message.Message,), {'DESCRIPTOR': _MISSEDBLOCK, '__module__': 'cosmos.slashing.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(MissedBlock)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z-github.com/cosmos/cosmos-sdk/x/slashing/types'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['signing_infos']._options = None
    _GENESISSTATE.fields_by_name['signing_infos']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['missed_blocks']._options = None
    _GENESISSTATE.fields_by_name['missed_blocks']._serialized_options = b'\xc8\xde\x1f\x00'
    _SIGNINGINFO.fields_by_name['address']._options = None
    _SIGNINGINFO.fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _SIGNINGINFO.fields_by_name['validator_signing_info']._options = None
    _SIGNINGINFO.fields_by_name['validator_signing_info']._serialized_options = b'\xc8\xde\x1f\x00'
    _VALIDATORMISSEDBLOCKS.fields_by_name['address']._options = None
    _VALIDATORMISSEDBLOCKS.fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _VALIDATORMISSEDBLOCKS.fields_by_name['missed_blocks']._options = None
    _VALIDATORMISSEDBLOCKS.fields_by_name['missed_blocks']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE._serialized_start = 156
    _GENESISSTATE._serialized_end = 369
    _SIGNINGINFO._serialized_start = 372
    _SIGNINGINFO._serialized_end = 513
    _VALIDATORMISSEDBLOCKS._serialized_start = 516
    _VALIDATORMISSEDBLOCKS._serialized_end = 649
    _MISSEDBLOCK._serialized_start = 651
    _MISSEDBLOCK._serialized_end = 695
