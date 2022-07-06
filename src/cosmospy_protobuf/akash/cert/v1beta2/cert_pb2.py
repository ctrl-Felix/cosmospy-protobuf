
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dakash/cert/v1beta2/cert.proto\x12\x12akash.cert.v1beta2\x1a\x14gogoproto/gogo.proto"p\n\rCertificateID\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12+\n\x06serial\x18\x02 \x01(\tB\x1b\xea\xde\x1f\x06serial\xf2\xde\x1f\ryaml:"serial":\x08\xe8\xa0\x1f\x00\x98\xa0\x1f\x00"\xb1\x02\n\x0bCertificate\x12O\n\x05state\x18\x02 \x01(\x0e2%.akash.cert.v1beta2.Certificate.StateB\x19\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state"\x12%\n\x04cert\x18\x03 \x01(\x0cB\x17\xea\xde\x1f\x04cert\xf2\xde\x1f\x0byaml:"cert"\x12+\n\x06pubkey\x18\x04 \x01(\x0cB\x1b\xea\xde\x1f\x06pubkey\xf2\xde\x1f\ryaml:"pubkey""}\n\x05State\x12(\n\x07invalid\x10\x00\x1a\x1b\x8a\x9d \x17CertificateStateInvalid\x12\x1f\n\x05valid\x10\x01\x1a\x14\x8a\x9d \x10CertificateValid\x12#\n\x07revoked\x10\x02\x1a\x16\x8a\x9d \x12CertificateRevoked\x1a\x04\x88\xa3\x1e\x00"\x9a\x01\n\x11CertificateFilter\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12+\n\x06serial\x18\x02 \x01(\tB\x1b\xea\xde\x1f\x06serial\xf2\xde\x1f\ryaml:"serial"\x12(\n\x05state\x18\x03 \x01(\tB\x19\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state":\x04\xe8\xa0\x1f\x00"\x9a\x01\n\x14MsgCreateCertificate\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12%\n\x04cert\x18\x02 \x01(\x0cB\x17\xea\xde\x1f\x04cert\xf2\xde\x1f\x0byaml:"cert"\x12+\n\x06pubkey\x18\x03 \x01(\x0cB\x1b\xea\xde\x1f\x06pubkey\xf2\xde\x1f\ryaml:"pubkey":\x04\xe8\xa0\x1f\x00"\x1e\n\x1cMsgCreateCertificateResponse"j\n\x14MsgRevokeCertificate\x12L\n\x02id\x18\x01 \x01(\x0b2!.akash.cert.v1beta2.CertificateIDB\x1d\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id":\x04\xe8\xa0\x1f\x00"\x1e\n\x1cMsgRevokeCertificateResponse2\xe7\x01\n\x03Msg\x12o\n\x11CreateCertificate\x12(.akash.cert.v1beta2.MsgCreateCertificate\x1a0.akash.cert.v1beta2.MsgCreateCertificateResponse\x12o\n\x11RevokeCertificate\x12(.akash.cert.v1beta2.MsgRevokeCertificate\x1a0.akash.cert.v1beta2.MsgRevokeCertificateResponseB.Z,github.com/ovrclk/akash/x/cert/types/v1beta2b\x06proto3')
_CERTIFICATEID = DESCRIPTOR.message_types_by_name['CertificateID']
_CERTIFICATE = DESCRIPTOR.message_types_by_name['Certificate']
_CERTIFICATEFILTER = DESCRIPTOR.message_types_by_name['CertificateFilter']
_MSGCREATECERTIFICATE = DESCRIPTOR.message_types_by_name['MsgCreateCertificate']
_MSGCREATECERTIFICATERESPONSE = DESCRIPTOR.message_types_by_name['MsgCreateCertificateResponse']
_MSGREVOKECERTIFICATE = DESCRIPTOR.message_types_by_name['MsgRevokeCertificate']
_MSGREVOKECERTIFICATERESPONSE = DESCRIPTOR.message_types_by_name['MsgRevokeCertificateResponse']
_CERTIFICATE_STATE = _CERTIFICATE.enum_types_by_name['State']
CertificateID = _reflection.GeneratedProtocolMessageType('CertificateID', (_message.Message,), {'DESCRIPTOR': _CERTIFICATEID, '__module__': 'akash.cert.v1beta2.cert_pb2'})
_sym_db.RegisterMessage(CertificateID)
Certificate = _reflection.GeneratedProtocolMessageType('Certificate', (_message.Message,), {'DESCRIPTOR': _CERTIFICATE, '__module__': 'akash.cert.v1beta2.cert_pb2'})
_sym_db.RegisterMessage(Certificate)
CertificateFilter = _reflection.GeneratedProtocolMessageType('CertificateFilter', (_message.Message,), {'DESCRIPTOR': _CERTIFICATEFILTER, '__module__': 'akash.cert.v1beta2.cert_pb2'})
_sym_db.RegisterMessage(CertificateFilter)
MsgCreateCertificate = _reflection.GeneratedProtocolMessageType('MsgCreateCertificate', (_message.Message,), {'DESCRIPTOR': _MSGCREATECERTIFICATE, '__module__': 'akash.cert.v1beta2.cert_pb2'})
_sym_db.RegisterMessage(MsgCreateCertificate)
MsgCreateCertificateResponse = _reflection.GeneratedProtocolMessageType('MsgCreateCertificateResponse', (_message.Message,), {'DESCRIPTOR': _MSGCREATECERTIFICATERESPONSE, '__module__': 'akash.cert.v1beta2.cert_pb2'})
_sym_db.RegisterMessage(MsgCreateCertificateResponse)
MsgRevokeCertificate = _reflection.GeneratedProtocolMessageType('MsgRevokeCertificate', (_message.Message,), {'DESCRIPTOR': _MSGREVOKECERTIFICATE, '__module__': 'akash.cert.v1beta2.cert_pb2'})
_sym_db.RegisterMessage(MsgRevokeCertificate)
MsgRevokeCertificateResponse = _reflection.GeneratedProtocolMessageType('MsgRevokeCertificateResponse', (_message.Message,), {'DESCRIPTOR': _MSGREVOKECERTIFICATERESPONSE, '__module__': 'akash.cert.v1beta2.cert_pb2'})
_sym_db.RegisterMessage(MsgRevokeCertificateResponse)
_MSG = DESCRIPTOR.services_by_name['Msg']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z,github.com/ovrclk/akash/x/cert/types/v1beta2'
    _CERTIFICATEID.fields_by_name['owner']._options = None
    _CERTIFICATEID.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _CERTIFICATEID.fields_by_name['serial']._options = None
    _CERTIFICATEID.fields_by_name['serial']._serialized_options = b'\xea\xde\x1f\x06serial\xf2\xde\x1f\ryaml:"serial"'
    _CERTIFICATEID._options = None
    _CERTIFICATEID._serialized_options = b'\xe8\xa0\x1f\x00\x98\xa0\x1f\x00'
    _CERTIFICATE_STATE._options = None
    _CERTIFICATE_STATE._serialized_options = b'\x88\xa3\x1e\x00'
    _CERTIFICATE_STATE.values_by_name['invalid']._options = None
    _CERTIFICATE_STATE.values_by_name['invalid']._serialized_options = b'\x8a\x9d \x17CertificateStateInvalid'
    _CERTIFICATE_STATE.values_by_name['valid']._options = None
    _CERTIFICATE_STATE.values_by_name['valid']._serialized_options = b'\x8a\x9d \x10CertificateValid'
    _CERTIFICATE_STATE.values_by_name['revoked']._options = None
    _CERTIFICATE_STATE.values_by_name['revoked']._serialized_options = b'\x8a\x9d \x12CertificateRevoked'
    _CERTIFICATE.fields_by_name['state']._options = None
    _CERTIFICATE.fields_by_name['state']._serialized_options = b'\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state"'
    _CERTIFICATE.fields_by_name['cert']._options = None
    _CERTIFICATE.fields_by_name['cert']._serialized_options = b'\xea\xde\x1f\x04cert\xf2\xde\x1f\x0byaml:"cert"'
    _CERTIFICATE.fields_by_name['pubkey']._options = None
    _CERTIFICATE.fields_by_name['pubkey']._serialized_options = b'\xea\xde\x1f\x06pubkey\xf2\xde\x1f\ryaml:"pubkey"'
    _CERTIFICATEFILTER.fields_by_name['owner']._options = None
    _CERTIFICATEFILTER.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _CERTIFICATEFILTER.fields_by_name['serial']._options = None
    _CERTIFICATEFILTER.fields_by_name['serial']._serialized_options = b'\xea\xde\x1f\x06serial\xf2\xde\x1f\ryaml:"serial"'
    _CERTIFICATEFILTER.fields_by_name['state']._options = None
    _CERTIFICATEFILTER.fields_by_name['state']._serialized_options = b'\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state"'
    _CERTIFICATEFILTER._options = None
    _CERTIFICATEFILTER._serialized_options = b'\xe8\xa0\x1f\x00'
    _MSGCREATECERTIFICATE.fields_by_name['owner']._options = None
    _MSGCREATECERTIFICATE.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _MSGCREATECERTIFICATE.fields_by_name['cert']._options = None
    _MSGCREATECERTIFICATE.fields_by_name['cert']._serialized_options = b'\xea\xde\x1f\x04cert\xf2\xde\x1f\x0byaml:"cert"'
    _MSGCREATECERTIFICATE.fields_by_name['pubkey']._options = None
    _MSGCREATECERTIFICATE.fields_by_name['pubkey']._serialized_options = b'\xea\xde\x1f\x06pubkey\xf2\xde\x1f\ryaml:"pubkey"'
    _MSGCREATECERTIFICATE._options = None
    _MSGCREATECERTIFICATE._serialized_options = b'\xe8\xa0\x1f\x00'
    _MSGREVOKECERTIFICATE.fields_by_name['id']._options = None
    _MSGREVOKECERTIFICATE.fields_by_name['id']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"'
    _MSGREVOKECERTIFICATE._options = None
    _MSGREVOKECERTIFICATE._serialized_options = b'\xe8\xa0\x1f\x00'
    _CERTIFICATEID._serialized_start = 75
    _CERTIFICATEID._serialized_end = 187
    _CERTIFICATE._serialized_start = 190
    _CERTIFICATE._serialized_end = 495
    _CERTIFICATE_STATE._serialized_start = 370
    _CERTIFICATE_STATE._serialized_end = 495
    _CERTIFICATEFILTER._serialized_start = 498
    _CERTIFICATEFILTER._serialized_end = 652
    _MSGCREATECERTIFICATE._serialized_start = 655
    _MSGCREATECERTIFICATE._serialized_end = 809
    _MSGCREATECERTIFICATERESPONSE._serialized_start = 811
    _MSGCREATECERTIFICATERESPONSE._serialized_end = 841
    _MSGREVOKECERTIFICATE._serialized_start = 843
    _MSGREVOKECERTIFICATE._serialized_end = 949
    _MSGREVOKECERTIFICATERESPONSE._serialized_start = 951
    _MSGREVOKECERTIFICATERESPONSE._serialized_end = 981
    _MSG._serialized_start = 984
    _MSG._serialized_end = 1215
