
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ...osmosis.superfluid import superfluid_pb2 as osmosis_dot_superfluid_dot_superfluid__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cosmosis/superfluid/gov.proto\x12\x1aosmosis.superfluid.v1beta1\x1a\x14gogoproto/gogo.proto\x1a#osmosis/superfluid/superfluid.proto"\x8a\x01\n\x1bSetSuperfluidAssetsProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x129\n\x06assets\x18\x03 \x03(\x0b2#.osmosis.superfluid.SuperfluidAssetB\x04\xc8\xde\x1f\x00:\x0c\xe8\xa0\x1f\x01\x88\xa0\x1f\x00\x98\xa0\x1f\x00"s\n\x1eRemoveSuperfluidAssetsProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x1f\n\x17superfluid_asset_denoms\x18\x03 \x03(\t:\x0c\xe8\xa0\x1f\x01\x88\xa0\x1f\x00\x98\xa0\x1f\x00B7Z5github.com/osmosis-labs/osmosis/v7/x/superfluid/typesb\x06proto3')
_SETSUPERFLUIDASSETSPROPOSAL = DESCRIPTOR.message_types_by_name['SetSuperfluidAssetsProposal']
_REMOVESUPERFLUIDASSETSPROPOSAL = DESCRIPTOR.message_types_by_name['RemoveSuperfluidAssetsProposal']
SetSuperfluidAssetsProposal = _reflection.GeneratedProtocolMessageType('SetSuperfluidAssetsProposal', (_message.Message,), {'DESCRIPTOR': _SETSUPERFLUIDASSETSPROPOSAL, '__module__': 'osmosis.superfluid.gov_pb2'})
_sym_db.RegisterMessage(SetSuperfluidAssetsProposal)
RemoveSuperfluidAssetsProposal = _reflection.GeneratedProtocolMessageType('RemoveSuperfluidAssetsProposal', (_message.Message,), {'DESCRIPTOR': _REMOVESUPERFLUIDASSETSPROPOSAL, '__module__': 'osmosis.superfluid.gov_pb2'})
_sym_db.RegisterMessage(RemoveSuperfluidAssetsProposal)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z5github.com/osmosis-labs/osmosis/v7/x/superfluid/types'
    _SETSUPERFLUIDASSETSPROPOSAL.fields_by_name['assets']._options = None
    _SETSUPERFLUIDASSETSPROPOSAL.fields_by_name['assets']._serialized_options = b'\xc8\xde\x1f\x00'
    _SETSUPERFLUIDASSETSPROPOSAL._options = None
    _SETSUPERFLUIDASSETSPROPOSAL._serialized_options = b'\xe8\xa0\x1f\x01\x88\xa0\x1f\x00\x98\xa0\x1f\x00'
    _REMOVESUPERFLUIDASSETSPROPOSAL._options = None
    _REMOVESUPERFLUIDASSETSPROPOSAL._serialized_options = b'\xe8\xa0\x1f\x01\x88\xa0\x1f\x00\x98\xa0\x1f\x00'
    _SETSUPERFLUIDASSETSPROPOSAL._serialized_start = 120
    _SETSUPERFLUIDASSETSPROPOSAL._serialized_end = 258
    _REMOVESUPERFLUIDASSETSPROPOSAL._serialized_start = 260
    _REMOVESUPERFLUIDASSETSPROPOSAL._serialized_end = 375
