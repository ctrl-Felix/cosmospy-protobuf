
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17cosmos/orm/v1/orm.proto\x12\rcosmos.orm.v1\x1a google/protobuf/descriptor.proto"\x8f\x01\n\x0fTableDescriptor\x128\n\x0bprimary_key\x18\x01 \x01(\x0b2#.cosmos.orm.v1.PrimaryKeyDescriptor\x126\n\x05index\x18\x02 \x03(\x0b2\'.cosmos.orm.v1.SecondaryIndexDescriptor\x12\n\n\x02id\x18\x03 \x01(\r">\n\x14PrimaryKeyDescriptor\x12\x0e\n\x06fields\x18\x01 \x01(\t\x12\x16\n\x0eauto_increment\x18\x02 \x01(\x08"F\n\x18SecondaryIndexDescriptor\x12\x0e\n\x06fields\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\r\x12\x0e\n\x06unique\x18\x03 \x01(\x08"!\n\x13SingletonDescriptor\x12\n\n\x02id\x18\x01 \x01(\r:Q\n\x05table\x12\x1f.google.protobuf.MessageOptions\x18\xee\xb3\xea1 \x01(\x0b2\x1e.cosmos.orm.v1.TableDescriptor:Y\n\tsingleton\x12\x1f.google.protobuf.MessageOptions\x18\xef\xb3\xea1 \x01(\x0b2".cosmos.orm.v1.SingletonDescriptorb\x06proto3')
TABLE_FIELD_NUMBER = 104503790
table = DESCRIPTOR.extensions_by_name['table']
SINGLETON_FIELD_NUMBER = 104503791
singleton = DESCRIPTOR.extensions_by_name['singleton']
_TABLEDESCRIPTOR = DESCRIPTOR.message_types_by_name['TableDescriptor']
_PRIMARYKEYDESCRIPTOR = DESCRIPTOR.message_types_by_name['PrimaryKeyDescriptor']
_SECONDARYINDEXDESCRIPTOR = DESCRIPTOR.message_types_by_name['SecondaryIndexDescriptor']
_SINGLETONDESCRIPTOR = DESCRIPTOR.message_types_by_name['SingletonDescriptor']
TableDescriptor = _reflection.GeneratedProtocolMessageType('TableDescriptor', (_message.Message,), {'DESCRIPTOR': _TABLEDESCRIPTOR, '__module__': 'cosmos.orm.v1.orm_pb2'})
_sym_db.RegisterMessage(TableDescriptor)
PrimaryKeyDescriptor = _reflection.GeneratedProtocolMessageType('PrimaryKeyDescriptor', (_message.Message,), {'DESCRIPTOR': _PRIMARYKEYDESCRIPTOR, '__module__': 'cosmos.orm.v1.orm_pb2'})
_sym_db.RegisterMessage(PrimaryKeyDescriptor)
SecondaryIndexDescriptor = _reflection.GeneratedProtocolMessageType('SecondaryIndexDescriptor', (_message.Message,), {'DESCRIPTOR': _SECONDARYINDEXDESCRIPTOR, '__module__': 'cosmos.orm.v1.orm_pb2'})
_sym_db.RegisterMessage(SecondaryIndexDescriptor)
SingletonDescriptor = _reflection.GeneratedProtocolMessageType('SingletonDescriptor', (_message.Message,), {'DESCRIPTOR': _SINGLETONDESCRIPTOR, '__module__': 'cosmos.orm.v1.orm_pb2'})
_sym_db.RegisterMessage(SingletonDescriptor)
if (_descriptor._USE_C_DESCRIPTORS == False):
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(table)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(singleton)
    DESCRIPTOR._options = None
    _TABLEDESCRIPTOR._serialized_start = 77
    _TABLEDESCRIPTOR._serialized_end = 220
    _PRIMARYKEYDESCRIPTOR._serialized_start = 222
    _PRIMARYKEYDESCRIPTOR._serialized_end = 284
    _SECONDARYINDEXDESCRIPTOR._serialized_start = 286
    _SECONDARYINDEXDESCRIPTOR._serialized_end = 356
    _SINGLETONDESCRIPTOR._serialized_start = 358
    _SINGLETONDESCRIPTOR._serialized_end = 391
