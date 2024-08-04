# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: authorizer/v1/authorizer.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x61uthorizer/v1/authorizer.proto\x12\rauthorizer.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"z\n\x13\x41uthorizationCommon\x12\x38\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\x12)\n\x10\x61uthorization_id\x18\x02 \x01(\tR\x0f\x61uthorizationId\"I\n\x0bPingRequest\x12:\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\".authorizer.v1.AuthorizationCommonR\x06\x63ommon\"J\n\x0cPingResponse\x12:\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\".authorizer.v1.AuthorizationCommonR\x06\x63ommon\"\x99\x01\n\x13\x41uthorizationResult\x12#\n\rerror_message\x18\x01 \x01(\tR\x0c\x65rrorMessage\x12!\n\x0c\x65rror_detail\x18\x02 \x01(\tR\x0b\x65rrorDetail\x12:\n\x04\x63ode\x18\x03 \x01(\x0e\x32&.authorizer.v1.AuthorizationResultCodeR\x04\x63ode\"a\n\x16\x45xtraDataSpecification\x12\x1f\n\x0b\x62ucket_tags\x18\x01 \x01(\x08R\nbucketTags\x12&\n\x0fobject_key_tags\x18\x02 \x01(\x08R\robjectKeyTags\"\xac\x02\n\tExtraData\x12I\n\x0b\x62ucket_tags\x18\x01 \x03(\x0b\x32(.authorizer.v1.ExtraData.BucketTagsEntryR\nbucketTags\x12S\n\x0fobject_key_tags\x18\x02 \x03(\x0b\x32+.authorizer.v1.ExtraData.ObjectKeyTagsEntryR\robjectKeyTags\x1a=\n\x0f\x42ucketTagsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x1a@\n\x12ObjectKeyTagsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xa0\x06\n\x12\x41uthorizeV2Request\x12:\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\".authorizer.v1.AuthorizationCommonR\x06\x63ommon\x12*\n\x11\x63\x61nonical_user_id\x18\t \x01(\tR\x0f\x63\x61nonicalUserId\x12\x19\n\x08user_arn\x18\x02 \x01(\tR\x07userArn\x12/\n\x11\x61ssuming_user_arn\x18\x03 \x01(\tH\x00R\x0f\x61ssumingUserArn\x88\x01\x01\x12\x1f\n\x0b\x61\x63\x63ount_arn\x18\x04 \x01(\tR\naccountArn\x12/\n\x06opcode\x18\x05 \x01(\x0e\x32\x17.authorizer.v1.S3OpcodeR\x06opcode\x12\x1f\n\x0b\x62ucket_name\x18\x06 \x01(\tR\nbucketName\x12&\n\x0fobject_key_name\x18\x07 \x01(\tR\robjectKeyName\x12T\n\x0b\x65nvironment\x18\n \x03(\x0b\x32\x32.authorizer.v1.AuthorizeV2Request.EnvironmentEntryR\x0b\x65nvironment\x12Z\n\x13\x65xtra_data_provided\x18\x0b \x01(\x0b\x32%.authorizer.v1.ExtraDataSpecificationH\x01R\x11\x65xtraDataProvided\x88\x01\x01\x12<\n\nextra_data\x18\x08 \x01(\x0b\x32\x18.authorizer.v1.ExtraDataH\x02R\textraData\x88\x01\x01\x1a\x1f\n\x0bIAMMapEntry\x12\x10\n\x03key\x18\x01 \x03(\tR\x03key\x1am\n\x10\x45nvironmentEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x43\n\x05value\x18\x02 \x01(\x0b\x32-.authorizer.v1.AuthorizeV2Request.IAMMapEntryR\x05value:\x02\x38\x01\x42\x14\n\x12_assuming_user_arnB\x16\n\x14_extra_data_providedB\r\n\x0b_extra_data\"\x81\x02\n\x13\x41uthorizeV2Response\x12:\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\".authorizer.v1.AuthorizationCommonR\x06\x63ommon\x12:\n\x06result\x18\x02 \x01(\x0b\x32\".authorizer.v1.AuthorizationResultR\x06result\x12Z\n\x13\x65xtra_data_required\x18\x03 \x01(\x0b\x32%.authorizer.v1.ExtraDataSpecificationH\x00R\x11\x65xtraDataRequired\x88\x01\x01\x42\x16\n\x14_extra_data_required*\xd3\x01\n\x17\x41uthorizationResultCode\x12\x1c\n\x18\x41UTHZ_RESULT_UNSPECIFIED\x10\x00\x12\x16\n\x12\x41UTHZ_RESULT_ALLOW\x10\x01\x12\x15\n\x11\x41UTHZ_RESULT_DENY\x10\x02\x12$\n AUTHZ_RESULT_EXTRA_DATA_REQUIRED\x10\x03\x12\x1f\n\x1b\x41UTHZ_RESULT_INTERNAL_ERROR\x10\x04\x12$\n AUTHZ_RESULT_RATE_LIMIT_EXCEEDED\x10\x05*\xe7\x14\n\x08S3Opcode\x12\x19\n\x15S3_OPCODE_UNSPECIFIED\x10\x00\x12\x18\n\x14S3_OPCODE_GET_OBJECT\x10\x01\x12 \n\x1cS3_OPCODE_GET_OBJECT_VERSION\x10\x02\x12\x18\n\x14S3_OPCODE_PUT_OBJECT\x10\x03\x12\x1c\n\x18S3_OPCODE_GET_OBJECT_ACL\x10\x04\x12$\n S3_OPCODE_GET_OBJECT_VERSION_ACL\x10\x05\x12\x1c\n\x18S3_OPCODE_PUT_OBJECT_ACL\x10\x06\x12$\n S3_OPCODE_PUT_OBJECT_VERSION_ACL\x10\x07\x12\x1b\n\x17S3_OPCODE_DELETE_OBJECT\x10\x08\x12#\n\x1fS3_OPCODE_DELETE_OBJECT_VERSION\x10\t\x12)\n%S3_OPCODE_LIST_MULTIPART_UPLOAD_PARTS\x10\n\x12$\n S3_OPCODE_ABORT_MULTIPART_UPLOAD\x10\x0b\x12 \n\x1cS3_OPCODE_GET_OBJECT_TORRENT\x10\x0c\x12(\n$S3_OPCODE_GET_OBJECT_VERSION_TORRENT\x10\r\x12\x1c\n\x18S3_OPCODE_RESTORE_OBJECT\x10\x0e\x12\x1b\n\x17S3_OPCODE_CREATE_BUCKET\x10\x0f\x12\x1b\n\x17S3_OPCODE_DELETE_BUCKET\x10\x10\x12\x19\n\x15S3_OPCODE_LIST_BUCKET\x10\x11\x12\"\n\x1eS3_OPCODE_LIST_BUCKET_VERSIONS\x10\x12\x12!\n\x1dS3_OPCODE_LIST_ALL_MY_BUCKETS\x10\x13\x12+\n\'S3_OPCODE_LIST_BUCKET_MULTIPART_UPLOADS\x10\x14\x12*\n&S3_OPCODE_GET_ACCELERATE_CONFIGURATION\x10\x15\x12*\n&S3_OPCODE_PUT_ACCELERATE_CONFIGURATION\x10\x16\x12\x1c\n\x18S3_OPCODE_GET_BUCKET_ACL\x10\x17\x12\x1c\n\x18S3_OPCODE_PUT_BUCKET_ACL\x10\x18\x12\x1d\n\x19S3_OPCODE_GET_BUCKET_CORS\x10\x19\x12\x1d\n\x19S3_OPCODE_PUT_BUCKET_CORS\x10\x1a\x12#\n\x1fS3_OPCODE_GET_BUCKET_VERSIONING\x10\x1b\x12#\n\x1fS3_OPCODE_PUT_BUCKET_VERSIONING\x10\x1c\x12(\n$S3_OPCODE_GET_BUCKET_REQUEST_PAYMENT\x10\x1d\x12(\n$S3_OPCODE_PUT_BUCKET_REQUEST_PAYMENT\x10\x1e\x12!\n\x1dS3_OPCODE_GET_BUCKET_LOCATION\x10\x1f\x12\x1f\n\x1bS3_OPCODE_GET_BUCKET_POLICY\x10 \x12\"\n\x1eS3_OPCODE_DELETE_BUCKET_POLICY\x10!\x12\x1f\n\x1bS3_OPCODE_PUT_BUCKET_POLICY\x10\"\x12%\n!S3_OPCODE_GET_BUCKET_NOTIFICATION\x10#\x12%\n!S3_OPCODE_PUT_BUCKET_NOTIFICATION\x10$\x12 \n\x1cS3_OPCODE_GET_BUCKET_LOGGING\x10%\x12 \n\x1cS3_OPCODE_PUT_BUCKET_LOGGING\x10&\x12 \n\x1cS3_OPCODE_GET_BUCKET_TAGGING\x10\'\x12 \n\x1cS3_OPCODE_PUT_BUCKET_TAGGING\x10(\x12 \n\x1cS3_OPCODE_GET_BUCKET_WEBSITE\x10)\x12 \n\x1cS3_OPCODE_PUT_BUCKET_WEBSITE\x10*\x12#\n\x1fS3_OPCODE_DELETE_BUCKET_WEBSITE\x10+\x12)\n%S3_OPCODE_GET_LIFECYCLE_CONFIGURATION\x10,\x12)\n%S3_OPCODE_PUT_LIFECYCLE_CONFIGURATION\x10-\x12+\n\'S3_OPCODE_PUT_REPLICATION_CONFIGURATION\x10.\x12+\n\'S3_OPCODE_GET_REPLICATION_CONFIGURATION\x10/\x12.\n*S3_OPCODE_DELETE_REPLICATION_CONFIGURATION\x10\x30\x12 \n\x1cS3_OPCODE_GET_OBJECT_TAGGING\x10\x31\x12 \n\x1cS3_OPCODE_PUT_OBJECT_TAGGING\x10\x32\x12#\n\x1fS3_OPCODE_DELETE_OBJECT_TAGGING\x10\x33\x12(\n$S3_OPCODE_GET_OBJECT_VERSION_TAGGING\x10\x34\x12(\n$S3_OPCODE_PUT_OBJECT_VERSION_TAGGING\x10\x35\x12+\n\'S3_OPCODE_DELETE_OBJECT_VERSION_TAGGING\x10\x36\x12\x32\n.S3_OPCODE_PUT_BUCKET_OBJECT_LOCK_CONFIGURATION\x10\x37\x12\x32\n.S3_OPCODE_GET_BUCKET_OBJECT_LOCK_CONFIGURATION\x10\x38\x12\"\n\x1eS3_OPCODE_PUT_OBJECT_RETENTION\x10\x39\x12\"\n\x1eS3_OPCODE_GET_OBJECT_RETENTION\x10:\x12#\n\x1fS3_OPCODE_PUT_OBJECT_LEGAL_HOLD\x10;\x12#\n\x1fS3_OPCODE_GET_OBJECT_LEGAL_HOLD\x10<\x12)\n%S3_OPCODE_BYPASS_GOVERNANCE_RETENTION\x10=\x12&\n\"S3_OPCODE_GET_BUCKET_POLICY_STATUS\x10>\x12%\n!S3_OPCODE_PUT_PUBLIC_ACCESS_BLOCK\x10?\x12%\n!S3_OPCODE_GET_PUBLIC_ACCESS_BLOCK\x10@\x12(\n$S3_OPCODE_DELETE_PUBLIC_ACCESS_BLOCK\x10\x41\x12,\n(S3_OPCODE_GET_BUCKET_PUBLIC_ACCESS_BLOCK\x10\x42\x12,\n(S3_OPCODE_PUT_BUCKET_PUBLIC_ACCESS_BLOCK\x10\x43\x12/\n+S3_OPCODE_DELETE_BUCKET_PUBLIC_ACCESS_BLOCK\x10\x44\x12#\n\x1fS3_OPCODE_GET_BUCKET_ENCRYPTION\x10\x45\x12#\n\x1fS3_OPCODE_PUT_BUCKET_ENCRYPTION\x10\x46\x32\xaa\x01\n\x11\x41uthorizerService\x12?\n\x04Ping\x12\x1a.authorizer.v1.PingRequest\x1a\x1b.authorizer.v1.PingResponse\x12T\n\x0b\x41uthorizeV2\x12!.authorizer.v1.AuthorizeV2Request\x1a\".authorizer.v1.AuthorizeV2ResponseB\xb9\x01\n\x11\x63om.authorizer.v1B\x0f\x41uthorizerProtoP\x01Z>bits.linode.com/LinodeApi/obj-endpoint/gen/proto/authorizer/v1\xa2\x02\x03\x41XX\xaa\x02\rAuthorizer.V1\xca\x02\rAuthorizer\\V1\xe2\x02\x19\x41uthorizer\\V1\\GPBMetadata\xea\x02\x0e\x41uthorizer::V1b\x06proto3')

_AUTHORIZATIONRESULTCODE = DESCRIPTOR.enum_types_by_name['AuthorizationResultCode']
AuthorizationResultCode = enum_type_wrapper.EnumTypeWrapper(_AUTHORIZATIONRESULTCODE)
_S3OPCODE = DESCRIPTOR.enum_types_by_name['S3Opcode']
S3Opcode = enum_type_wrapper.EnumTypeWrapper(_S3OPCODE)
AUTHZ_RESULT_UNSPECIFIED = 0
AUTHZ_RESULT_ALLOW = 1
AUTHZ_RESULT_DENY = 2
AUTHZ_RESULT_EXTRA_DATA_REQUIRED = 3
AUTHZ_RESULT_INTERNAL_ERROR = 4
AUTHZ_RESULT_RATE_LIMIT_EXCEEDED = 5
S3_OPCODE_UNSPECIFIED = 0
S3_OPCODE_GET_OBJECT = 1
S3_OPCODE_GET_OBJECT_VERSION = 2
S3_OPCODE_PUT_OBJECT = 3
S3_OPCODE_GET_OBJECT_ACL = 4
S3_OPCODE_GET_OBJECT_VERSION_ACL = 5
S3_OPCODE_PUT_OBJECT_ACL = 6
S3_OPCODE_PUT_OBJECT_VERSION_ACL = 7
S3_OPCODE_DELETE_OBJECT = 8
S3_OPCODE_DELETE_OBJECT_VERSION = 9
S3_OPCODE_LIST_MULTIPART_UPLOAD_PARTS = 10
S3_OPCODE_ABORT_MULTIPART_UPLOAD = 11
S3_OPCODE_GET_OBJECT_TORRENT = 12
S3_OPCODE_GET_OBJECT_VERSION_TORRENT = 13
S3_OPCODE_RESTORE_OBJECT = 14
S3_OPCODE_CREATE_BUCKET = 15
S3_OPCODE_DELETE_BUCKET = 16
S3_OPCODE_LIST_BUCKET = 17
S3_OPCODE_LIST_BUCKET_VERSIONS = 18
S3_OPCODE_LIST_ALL_MY_BUCKETS = 19
S3_OPCODE_LIST_BUCKET_MULTIPART_UPLOADS = 20
S3_OPCODE_GET_ACCELERATE_CONFIGURATION = 21
S3_OPCODE_PUT_ACCELERATE_CONFIGURATION = 22
S3_OPCODE_GET_BUCKET_ACL = 23
S3_OPCODE_PUT_BUCKET_ACL = 24
S3_OPCODE_GET_BUCKET_CORS = 25
S3_OPCODE_PUT_BUCKET_CORS = 26
S3_OPCODE_GET_BUCKET_VERSIONING = 27
S3_OPCODE_PUT_BUCKET_VERSIONING = 28
S3_OPCODE_GET_BUCKET_REQUEST_PAYMENT = 29
S3_OPCODE_PUT_BUCKET_REQUEST_PAYMENT = 30
S3_OPCODE_GET_BUCKET_LOCATION = 31
S3_OPCODE_GET_BUCKET_POLICY = 32
S3_OPCODE_DELETE_BUCKET_POLICY = 33
S3_OPCODE_PUT_BUCKET_POLICY = 34
S3_OPCODE_GET_BUCKET_NOTIFICATION = 35
S3_OPCODE_PUT_BUCKET_NOTIFICATION = 36
S3_OPCODE_GET_BUCKET_LOGGING = 37
S3_OPCODE_PUT_BUCKET_LOGGING = 38
S3_OPCODE_GET_BUCKET_TAGGING = 39
S3_OPCODE_PUT_BUCKET_TAGGING = 40
S3_OPCODE_GET_BUCKET_WEBSITE = 41
S3_OPCODE_PUT_BUCKET_WEBSITE = 42
S3_OPCODE_DELETE_BUCKET_WEBSITE = 43
S3_OPCODE_GET_LIFECYCLE_CONFIGURATION = 44
S3_OPCODE_PUT_LIFECYCLE_CONFIGURATION = 45
S3_OPCODE_PUT_REPLICATION_CONFIGURATION = 46
S3_OPCODE_GET_REPLICATION_CONFIGURATION = 47
S3_OPCODE_DELETE_REPLICATION_CONFIGURATION = 48
S3_OPCODE_GET_OBJECT_TAGGING = 49
S3_OPCODE_PUT_OBJECT_TAGGING = 50
S3_OPCODE_DELETE_OBJECT_TAGGING = 51
S3_OPCODE_GET_OBJECT_VERSION_TAGGING = 52
S3_OPCODE_PUT_OBJECT_VERSION_TAGGING = 53
S3_OPCODE_DELETE_OBJECT_VERSION_TAGGING = 54
S3_OPCODE_PUT_BUCKET_OBJECT_LOCK_CONFIGURATION = 55
S3_OPCODE_GET_BUCKET_OBJECT_LOCK_CONFIGURATION = 56
S3_OPCODE_PUT_OBJECT_RETENTION = 57
S3_OPCODE_GET_OBJECT_RETENTION = 58
S3_OPCODE_PUT_OBJECT_LEGAL_HOLD = 59
S3_OPCODE_GET_OBJECT_LEGAL_HOLD = 60
S3_OPCODE_BYPASS_GOVERNANCE_RETENTION = 61
S3_OPCODE_GET_BUCKET_POLICY_STATUS = 62
S3_OPCODE_PUT_PUBLIC_ACCESS_BLOCK = 63
S3_OPCODE_GET_PUBLIC_ACCESS_BLOCK = 64
S3_OPCODE_DELETE_PUBLIC_ACCESS_BLOCK = 65
S3_OPCODE_GET_BUCKET_PUBLIC_ACCESS_BLOCK = 66
S3_OPCODE_PUT_BUCKET_PUBLIC_ACCESS_BLOCK = 67
S3_OPCODE_DELETE_BUCKET_PUBLIC_ACCESS_BLOCK = 68
S3_OPCODE_GET_BUCKET_ENCRYPTION = 69
S3_OPCODE_PUT_BUCKET_ENCRYPTION = 70


_AUTHORIZATIONCOMMON = DESCRIPTOR.message_types_by_name['AuthorizationCommon']
_PINGREQUEST = DESCRIPTOR.message_types_by_name['PingRequest']
_PINGRESPONSE = DESCRIPTOR.message_types_by_name['PingResponse']
_AUTHORIZATIONRESULT = DESCRIPTOR.message_types_by_name['AuthorizationResult']
_EXTRADATASPECIFICATION = DESCRIPTOR.message_types_by_name['ExtraDataSpecification']
_EXTRADATA = DESCRIPTOR.message_types_by_name['ExtraData']
_EXTRADATA_BUCKETTAGSENTRY = _EXTRADATA.nested_types_by_name['BucketTagsEntry']
_EXTRADATA_OBJECTKEYTAGSENTRY = _EXTRADATA.nested_types_by_name['ObjectKeyTagsEntry']
_AUTHORIZEV2REQUEST = DESCRIPTOR.message_types_by_name['AuthorizeV2Request']
_AUTHORIZEV2REQUEST_IAMMAPENTRY = _AUTHORIZEV2REQUEST.nested_types_by_name['IAMMapEntry']
_AUTHORIZEV2REQUEST_ENVIRONMENTENTRY = _AUTHORIZEV2REQUEST.nested_types_by_name['EnvironmentEntry']
_AUTHORIZEV2RESPONSE = DESCRIPTOR.message_types_by_name['AuthorizeV2Response']
AuthorizationCommon = _reflection.GeneratedProtocolMessageType('AuthorizationCommon', (_message.Message,), {
  'DESCRIPTOR' : _AUTHORIZATIONCOMMON,
  '__module__' : 'authorizer.v1.authorizer_pb2'
  # @@protoc_insertion_point(class_scope:authorizer.v1.AuthorizationCommon)
  })
_sym_db.RegisterMessage(AuthorizationCommon)

PingRequest = _reflection.GeneratedProtocolMessageType('PingRequest', (_message.Message,), {
  'DESCRIPTOR' : _PINGREQUEST,
  '__module__' : 'authorizer.v1.authorizer_pb2'
  # @@protoc_insertion_point(class_scope:authorizer.v1.PingRequest)
  })
_sym_db.RegisterMessage(PingRequest)

PingResponse = _reflection.GeneratedProtocolMessageType('PingResponse', (_message.Message,), {
  'DESCRIPTOR' : _PINGRESPONSE,
  '__module__' : 'authorizer.v1.authorizer_pb2'
  # @@protoc_insertion_point(class_scope:authorizer.v1.PingResponse)
  })
_sym_db.RegisterMessage(PingResponse)

AuthorizationResult = _reflection.GeneratedProtocolMessageType('AuthorizationResult', (_message.Message,), {
  'DESCRIPTOR' : _AUTHORIZATIONRESULT,
  '__module__' : 'authorizer.v1.authorizer_pb2'
  # @@protoc_insertion_point(class_scope:authorizer.v1.AuthorizationResult)
  })
_sym_db.RegisterMessage(AuthorizationResult)

ExtraDataSpecification = _reflection.GeneratedProtocolMessageType('ExtraDataSpecification', (_message.Message,), {
  'DESCRIPTOR' : _EXTRADATASPECIFICATION,
  '__module__' : 'authorizer.v1.authorizer_pb2'
  # @@protoc_insertion_point(class_scope:authorizer.v1.ExtraDataSpecification)
  })
_sym_db.RegisterMessage(ExtraDataSpecification)

ExtraData = _reflection.GeneratedProtocolMessageType('ExtraData', (_message.Message,), {

  'BucketTagsEntry' : _reflection.GeneratedProtocolMessageType('BucketTagsEntry', (_message.Message,), {
    'DESCRIPTOR' : _EXTRADATA_BUCKETTAGSENTRY,
    '__module__' : 'authorizer.v1.authorizer_pb2'
    # @@protoc_insertion_point(class_scope:authorizer.v1.ExtraData.BucketTagsEntry)
    })
  ,

  'ObjectKeyTagsEntry' : _reflection.GeneratedProtocolMessageType('ObjectKeyTagsEntry', (_message.Message,), {
    'DESCRIPTOR' : _EXTRADATA_OBJECTKEYTAGSENTRY,
    '__module__' : 'authorizer.v1.authorizer_pb2'
    # @@protoc_insertion_point(class_scope:authorizer.v1.ExtraData.ObjectKeyTagsEntry)
    })
  ,
  'DESCRIPTOR' : _EXTRADATA,
  '__module__' : 'authorizer.v1.authorizer_pb2'
  # @@protoc_insertion_point(class_scope:authorizer.v1.ExtraData)
  })
_sym_db.RegisterMessage(ExtraData)
_sym_db.RegisterMessage(ExtraData.BucketTagsEntry)
_sym_db.RegisterMessage(ExtraData.ObjectKeyTagsEntry)

AuthorizeV2Request = _reflection.GeneratedProtocolMessageType('AuthorizeV2Request', (_message.Message,), {

  'IAMMapEntry' : _reflection.GeneratedProtocolMessageType('IAMMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _AUTHORIZEV2REQUEST_IAMMAPENTRY,
    '__module__' : 'authorizer.v1.authorizer_pb2'
    # @@protoc_insertion_point(class_scope:authorizer.v1.AuthorizeV2Request.IAMMapEntry)
    })
  ,

  'EnvironmentEntry' : _reflection.GeneratedProtocolMessageType('EnvironmentEntry', (_message.Message,), {
    'DESCRIPTOR' : _AUTHORIZEV2REQUEST_ENVIRONMENTENTRY,
    '__module__' : 'authorizer.v1.authorizer_pb2'
    # @@protoc_insertion_point(class_scope:authorizer.v1.AuthorizeV2Request.EnvironmentEntry)
    })
  ,
  'DESCRIPTOR' : _AUTHORIZEV2REQUEST,
  '__module__' : 'authorizer.v1.authorizer_pb2'
  # @@protoc_insertion_point(class_scope:authorizer.v1.AuthorizeV2Request)
  })
_sym_db.RegisterMessage(AuthorizeV2Request)
_sym_db.RegisterMessage(AuthorizeV2Request.IAMMapEntry)
_sym_db.RegisterMessage(AuthorizeV2Request.EnvironmentEntry)

AuthorizeV2Response = _reflection.GeneratedProtocolMessageType('AuthorizeV2Response', (_message.Message,), {
  'DESCRIPTOR' : _AUTHORIZEV2RESPONSE,
  '__module__' : 'authorizer.v1.authorizer_pb2'
  # @@protoc_insertion_point(class_scope:authorizer.v1.AuthorizeV2Response)
  })
_sym_db.RegisterMessage(AuthorizeV2Response)

_AUTHORIZERSERVICE = DESCRIPTOR.services_by_name['AuthorizerService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021com.authorizer.v1B\017AuthorizerProtoP\001Z>bits.linode.com/LinodeApi/obj-endpoint/gen/proto/authorizer/v1\242\002\003AXX\252\002\rAuthorizer.V1\312\002\rAuthorizer\\V1\342\002\031Authorizer\\V1\\GPBMetadata\352\002\016Authorizer::V1'
  _EXTRADATA_BUCKETTAGSENTRY._options = None
  _EXTRADATA_BUCKETTAGSENTRY._serialized_options = b'8\001'
  _EXTRADATA_OBJECTKEYTAGSENTRY._options = None
  _EXTRADATA_OBJECTKEYTAGSENTRY._serialized_options = b'8\001'
  _AUTHORIZEV2REQUEST_ENVIRONMENTENTRY._options = None
  _AUTHORIZEV2REQUEST_ENVIRONMENTENTRY._serialized_options = b'8\001'
  _AUTHORIZATIONRESULTCODE._serialized_start=1979
  _AUTHORIZATIONRESULTCODE._serialized_end=2190
  _S3OPCODE._serialized_start=2193
  _S3OPCODE._serialized_end=4856
  _AUTHORIZATIONCOMMON._serialized_start=82
  _AUTHORIZATIONCOMMON._serialized_end=204
  _PINGREQUEST._serialized_start=206
  _PINGREQUEST._serialized_end=279
  _PINGRESPONSE._serialized_start=281
  _PINGRESPONSE._serialized_end=355
  _AUTHORIZATIONRESULT._serialized_start=358
  _AUTHORIZATIONRESULT._serialized_end=511
  _EXTRADATASPECIFICATION._serialized_start=513
  _EXTRADATASPECIFICATION._serialized_end=610
  _EXTRADATA._serialized_start=613
  _EXTRADATA._serialized_end=913
  _EXTRADATA_BUCKETTAGSENTRY._serialized_start=786
  _EXTRADATA_BUCKETTAGSENTRY._serialized_end=847
  _EXTRADATA_OBJECTKEYTAGSENTRY._serialized_start=849
  _EXTRADATA_OBJECTKEYTAGSENTRY._serialized_end=913
  _AUTHORIZEV2REQUEST._serialized_start=916
  _AUTHORIZEV2REQUEST._serialized_end=1716
  _AUTHORIZEV2REQUEST_IAMMAPENTRY._serialized_start=1513
  _AUTHORIZEV2REQUEST_IAMMAPENTRY._serialized_end=1544
  _AUTHORIZEV2REQUEST_ENVIRONMENTENTRY._serialized_start=1546
  _AUTHORIZEV2REQUEST_ENVIRONMENTENTRY._serialized_end=1655
  _AUTHORIZEV2RESPONSE._serialized_start=1719
  _AUTHORIZEV2RESPONSE._serialized_end=1976
  _AUTHORIZERSERVICE._serialized_start=4859
  _AUTHORIZERSERVICE._serialized_end=5029
# @@protoc_insertion_point(module_scope)
