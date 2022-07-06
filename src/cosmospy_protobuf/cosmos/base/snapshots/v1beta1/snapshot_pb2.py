
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,cosmos/base/snapshots/v1beta1/snapshot.proto\x12\x1dcosmos.base.snapshots.v1beta1\x1a\x14gogoproto/gogo.proto"\x89\x01\n\x08Snapshot\x12\x0e\n\x06height\x18\x01 \x01(\x04\x12\x0e\n\x06format\x18\x02 \x01(\r\x12\x0e\n\x06chunks\x18\x03 \x01(\r\x12\x0c\n\x04hash\x18\x04 \x01(\x0c\x12?\n\x08metadata\x18\x05 \x01(\x0b2\'.cosmos.base.snapshots.v1beta1.MetadataB\x04\xc8\xde\x1f\x00" \n\x08Metadata\x12\x14\n\x0cchunk_hashes\x18\x01 \x03(\x0c"\xcb\x03\n\x0cSnapshotItem\x12A\n\x05store\x18\x01 \x01(\x0b20.cosmos.base.snapshots.v1beta1.SnapshotStoreItemH\x00\x12I\n\x04iavl\x18\x02 \x01(\x0b2/.cosmos.base.snapshots.v1beta1.SnapshotIAVLItemB\x08\xe2\xde\x1f\x04IAVLH\x00\x12I\n\textension\x18\x03 \x01(\x0b24.cosmos.base.snapshots.v1beta1.SnapshotExtensionMetaH\x00\x12T\n\x11extension_payload\x18\x04 \x01(\x0b27.cosmos.base.snapshots.v1beta1.SnapshotExtensionPayloadH\x00\x12C\n\x02kv\x18\x05 \x01(\x0b2-.cosmos.base.snapshots.v1beta1.SnapshotKVItemB\x06\xe2\xde\x1f\x02KVH\x00\x12?\n\x06schema\x18\x06 \x01(\x0b2-.cosmos.base.snapshots.v1beta1.SnapshotSchemaH\x00B\x06\n\x04item"!\n\x11SnapshotStoreItem\x12\x0c\n\x04name\x18\x01 \x01(\t"O\n\x10SnapshotIAVLItem\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x0f\n\x07version\x18\x03 \x01(\x03\x12\x0e\n\x06height\x18\x04 \x01(\x05"5\n\x15SnapshotExtensionMeta\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06format\x18\x02 \x01(\r"+\n\x18SnapshotExtensionPayload\x12\x0f\n\x07payload\x18\x01 \x01(\x0c",\n\x0eSnapshotKVItem\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c"\x1e\n\x0eSnapshotSchema\x12\x0c\n\x04keys\x18\x01 \x03(\x0cB.Z,github.com/cosmos/cosmos-sdk/snapshots/typesb\x06proto3')
_SNAPSHOT = DESCRIPTOR.message_types_by_name['Snapshot']
_METADATA = DESCRIPTOR.message_types_by_name['Metadata']
_SNAPSHOTITEM = DESCRIPTOR.message_types_by_name['SnapshotItem']
_SNAPSHOTSTOREITEM = DESCRIPTOR.message_types_by_name['SnapshotStoreItem']
_SNAPSHOTIAVLITEM = DESCRIPTOR.message_types_by_name['SnapshotIAVLItem']
_SNAPSHOTEXTENSIONMETA = DESCRIPTOR.message_types_by_name['SnapshotExtensionMeta']
_SNAPSHOTEXTENSIONPAYLOAD = DESCRIPTOR.message_types_by_name['SnapshotExtensionPayload']
_SNAPSHOTKVITEM = DESCRIPTOR.message_types_by_name['SnapshotKVItem']
_SNAPSHOTSCHEMA = DESCRIPTOR.message_types_by_name['SnapshotSchema']
Snapshot = _reflection.GeneratedProtocolMessageType('Snapshot', (_message.Message,), {'DESCRIPTOR': _SNAPSHOT, '__module__': 'cosmos.base.snapshots.v1beta1.snapshot_pb2'})
_sym_db.RegisterMessage(Snapshot)
Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), {'DESCRIPTOR': _METADATA, '__module__': 'cosmos.base.snapshots.v1beta1.snapshot_pb2'})
_sym_db.RegisterMessage(Metadata)
SnapshotItem = _reflection.GeneratedProtocolMessageType('SnapshotItem', (_message.Message,), {'DESCRIPTOR': _SNAPSHOTITEM, '__module__': 'cosmos.base.snapshots.v1beta1.snapshot_pb2'})
_sym_db.RegisterMessage(SnapshotItem)
SnapshotStoreItem = _reflection.GeneratedProtocolMessageType('SnapshotStoreItem', (_message.Message,), {'DESCRIPTOR': _SNAPSHOTSTOREITEM, '__module__': 'cosmos.base.snapshots.v1beta1.snapshot_pb2'})
_sym_db.RegisterMessage(SnapshotStoreItem)
SnapshotIAVLItem = _reflection.GeneratedProtocolMessageType('SnapshotIAVLItem', (_message.Message,), {'DESCRIPTOR': _SNAPSHOTIAVLITEM, '__module__': 'cosmos.base.snapshots.v1beta1.snapshot_pb2'})
_sym_db.RegisterMessage(SnapshotIAVLItem)
SnapshotExtensionMeta = _reflection.GeneratedProtocolMessageType('SnapshotExtensionMeta', (_message.Message,), {'DESCRIPTOR': _SNAPSHOTEXTENSIONMETA, '__module__': 'cosmos.base.snapshots.v1beta1.snapshot_pb2'})
_sym_db.RegisterMessage(SnapshotExtensionMeta)
SnapshotExtensionPayload = _reflection.GeneratedProtocolMessageType('SnapshotExtensionPayload', (_message.Message,), {'DESCRIPTOR': _SNAPSHOTEXTENSIONPAYLOAD, '__module__': 'cosmos.base.snapshots.v1beta1.snapshot_pb2'})
_sym_db.RegisterMessage(SnapshotExtensionPayload)
SnapshotKVItem = _reflection.GeneratedProtocolMessageType('SnapshotKVItem', (_message.Message,), {'DESCRIPTOR': _SNAPSHOTKVITEM, '__module__': 'cosmos.base.snapshots.v1beta1.snapshot_pb2'})
_sym_db.RegisterMessage(SnapshotKVItem)
SnapshotSchema = _reflection.GeneratedProtocolMessageType('SnapshotSchema', (_message.Message,), {'DESCRIPTOR': _SNAPSHOTSCHEMA, '__module__': 'cosmos.base.snapshots.v1beta1.snapshot_pb2'})
_sym_db.RegisterMessage(SnapshotSchema)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z,github.com/cosmos/cosmos-sdk/snapshots/types'
    _SNAPSHOT.fields_by_name['metadata']._options = None
    _SNAPSHOT.fields_by_name['metadata']._serialized_options = b'\xc8\xde\x1f\x00'
    _SNAPSHOTITEM.fields_by_name['iavl']._options = None
    _SNAPSHOTITEM.fields_by_name['iavl']._serialized_options = b'\xe2\xde\x1f\x04IAVL'
    _SNAPSHOTITEM.fields_by_name['kv']._options = None
    _SNAPSHOTITEM.fields_by_name['kv']._serialized_options = b'\xe2\xde\x1f\x02KV'
    _SNAPSHOT._serialized_start = 102
    _SNAPSHOT._serialized_end = 239
    _METADATA._serialized_start = 241
    _METADATA._serialized_end = 273
    _SNAPSHOTITEM._serialized_start = 276
    _SNAPSHOTITEM._serialized_end = 735
    _SNAPSHOTSTOREITEM._serialized_start = 737
    _SNAPSHOTSTOREITEM._serialized_end = 770
    _SNAPSHOTIAVLITEM._serialized_start = 772
    _SNAPSHOTIAVLITEM._serialized_end = 851
    _SNAPSHOTEXTENSIONMETA._serialized_start = 853
    _SNAPSHOTEXTENSIONMETA._serialized_end = 906
    _SNAPSHOTEXTENSIONPAYLOAD._serialized_start = 908
    _SNAPSHOTEXTENSIONPAYLOAD._serialized_end = 951
    _SNAPSHOTKVITEM._serialized_start = 953
    _SNAPSHOTKVITEM._serialized_end = 997
    _SNAPSHOTSCHEMA._serialized_start = 999
    _SNAPSHOTSCHEMA._serialized_end = 1029
