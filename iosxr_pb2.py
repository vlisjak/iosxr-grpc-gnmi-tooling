# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: iosxr.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 27, 2, "", "iosxr.proto")
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0biosxr.proto\x12"IOSXRExtensibleManagabilityService"4\n\rConfigGetArgs\x12\r\n\x05ReqId\x18\x01 \x01(\x03\x12\x14\n\x0cyangpathjson\x18\x02 \x01(\t"D\n\x0e\x43onfigGetReply\x12\x10\n\x08ResReqId\x18\x01 \x01(\x03\x12\x10\n\x08yangjson\x18\x02 \x01(\t\x12\x0e\n\x06\x65rrors\x18\x03 \x01(\t"2\n\x0bGetOperArgs\x12\r\n\x05ReqId\x18\x01 \x01(\x03\x12\x14\n\x0cyangpathjson\x18\x02 \x01(\t"B\n\x0cGetOperReply\x12\x10\n\x08ResReqId\x18\x01 \x01(\x03\x12\x10\n\x08yangjson\x18\x02 \x01(\t\x12\x0e\n\x06\x65rrors\x18\x03 \x01(\t"X\n\nConfigArgs\x12\r\n\x05ReqId\x18\x01 \x01(\x03\x12\x10\n\x08yangjson\x18\x02 \x01(\t\x12\x11\n\tConfirmed\x18\x03 \x01(\x08\x12\x16\n\x0e\x43onfirmTimeout\x18\x04 \x01(\r"A\n\x0b\x43onfigReply\x12\x10\n\x08ResReqId\x18\x01 \x01(\x03\x12\x0e\n\x06\x65rrors\x18\x02 \x01(\t\x12\x10\n\x08\x43ommitID\x18\x03 \x01(\r"V\n\rCliConfigArgs\x12\r\n\x05ReqId\x18\x01 \x01(\x03\x12\x0b\n\x03\x63li\x18\x02 \x01(\t\x12\x11\n\tConfirmed\x18\x03 \x01(\x08\x12\x16\n\x0e\x43onfirmTimeout\x18\x04 \x01(\r"D\n\x0e\x43liConfigReply\x12\x10\n\x08ResReqId\x18\x01 \x01(\x03\x12\x0e\n\x06\x65rrors\x18\x02 \x01(\t\x12\x10\n\x08\x43ommitID\x18\x03 \x01(\r"A\n\x11\x43ommitReplaceArgs\x12\r\n\x05ReqId\x18\x01 \x01(\x03\x12\x0b\n\x03\x63li\x18\x02 \x01(\t\x12\x10\n\x08yangjson\x18\x03 \x01(\t"6\n\x12\x43ommitReplaceReply\x12\x10\n\x08ResReqId\x18\x01 \x01(\x03\x12\x0e\n\x06\x65rrors\x18\x02 \x01(\t"+\n\tCommitMsg\x12\r\n\x05label\x18\x01 \x01(\t\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t"-\n\nCommitArgs\x12\r\n\x05ReqId\x18\x01 \x01(\x03\x12\x10\n\x08\x43ommitID\x18\x02 \x01(\r"/\n\x0b\x43ommitReply\x12\x10\n\x08ResReqId\x18\x01 \x01(\x03\x12\x0e\n\x06\x65rrors\x18\x02 \x01(\t"#\n\x12\x44iscardChangesArgs\x12\r\n\x05ReqId\x18\x01 \x01(\x03"7\n\x13\x44iscardChangesReply\x12\x10\n\x08ResReqId\x18\x01 \x01(\x03\x12\x0e\n\x06\x65rrors\x18\x02 \x01(\t")\n\x0bShowCmdArgs\x12\r\n\x05ReqId\x18\x01 \x01(\x03\x12\x0b\n\x03\x63li\x18\x02 \x01(\t"D\n\x10ShowCmdTextReply\x12\x10\n\x08ResReqId\x18\x01 \x01(\x03\x12\x0e\n\x06output\x18\x02 \x01(\t\x12\x0e\n\x06\x65rrors\x18\x03 \x01(\t"H\n\x10ShowCmdJSONReply\x12\x10\n\x08ResReqId\x18\x01 \x01(\x03\x12\x12\n\njsonoutput\x18\x02 \x01(\t\x12\x0e\n\x06\x65rrors\x18\x03 \x01(\t"\x1d\n\nQOSMarking\x12\x0f\n\x07marking\x18\x01 \x01(\r"\x95\x01\n\x0e\x43reateSubsArgs\x12\r\n\x05ReqId\x18\x01 \x01(\x03\x12\x0e\n\x06\x65ncode\x18\x02 \x01(\x03\x12\x10\n\x08subidstr\x18\x03 \x01(\t\x12;\n\x03qos\x18\x04 \x01(\x0b\x32..IOSXRExtensibleManagabilityService.QOSMarking\x12\x15\n\rSubscriptions\x18\x05 \x03(\t"5\n\x0e\x41\x63tionJSONArgs\x12\r\n\x05ReqId\x18\x01 \x01(\x03\x12\x14\n\x0cyangpathjson\x18\x02 \x01(\t"E\n\x0f\x41\x63tionJSONReply\x12\x10\n\x08ResReqId\x18\x01 \x01(\x03\x12\x10\n\x08yangjson\x18\x02 \x01(\t\x12\x0e\n\x06\x65rrors\x18\x03 \x01(\t"A\n\x0f\x43reateSubsReply\x12\x10\n\x08ResReqId\x18\x01 \x01(\x03\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\x0e\n\x06\x65rrors\x18\x03 \x01(\t"w\n\x10SubscribeRequest\x12\r\n\x05ReqId\x18\x01 \x01(\x03\x12I\n\tsubscribe\x18\x02 \x01(\x0b\x32\x34.IOSXRExtensibleManagabilityService.SubscriptionListH\x00\x42\t\n\x07request"\xdc\x01\n\x1aTelemetryStreamDestination\x12\x1b\n\x13\x64\x65stination_address\x18\x01 \x01(\t\x12\x18\n\x10\x64\x65stination_port\x18\x02 \x01(\r\x12\x65\n\x19telemetry_stream_protocol\x18\x03 \x01(\x0e\x32\x42.IOSXRExtensibleManagabilityService.TelemetryStreamDestination.TSP" \n\x03TSP\x12\x0b\n\x07TSP_TCP\x10\x00\x12\x0c\n\x08TSP_GRPC\x10\x01"\x1d\n\rTelemetryPath\x12\x0c\n\x04Path\x18\x01 \x01(\t"\x92\x03\n\x10SubscriptionList\x12\x63\n\x1bTelemetryStreamDestinations\x18\x01 \x03(\x0b\x32>.IOSXRExtensibleManagabilityService.TelemetryStreamDestination\x12I\n\x0eTelemetryPaths\x18\x02 \x03(\x0b\x32\x31.IOSXRExtensibleManagabilityService.TelemetryPath\x12\x17\n\x0fsample_interval\x18\x03 \x01(\x04\x12O\n\x08\x65ncoding\x18\x04 \x01(\x0e\x32=.IOSXRExtensibleManagabilityService.SubscriptionList.ENC_SPEC\x12;\n\x03qos\x18\x05 \x01(\x0b\x32..IOSXRExtensibleManagabilityService.QOSMarking"\'\n\x08\x45NC_SPEC\x12\x0e\n\nENC_KV_GPB\x10\x00\x12\x0b\n\x07\x45NC_GPB\x10\x01"n\n\x0eStatusResponse\x12\x14\n\x0cmessage_json\x18\x01 \x01(\t\x12\x46\n\x04\x63ode\x18\x02 \x01(\x0e\x32\x38.IOSXRExtensibleManagabilityService.OC_RPC_RESPONSE_TYPE"\x1c\n\x0cNotification\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c"\xd4\x01\n\x11SubscribeResponse\x12\x10\n\x08ResReqId\x18\x01 \x01(\x03\x12\x17\n\x0fsubscription_id\x18\x02 \x01(\x04\x12\x42\n\x06update\x18\x03 \x01(\x0b\x32\x30.IOSXRExtensibleManagabilityService.NotificationH\x00\x12\x44\n\x06status\x18\x04 \x01(\x0b\x32\x32.IOSXRExtensibleManagabilityService.StatusResponseH\x00\x42\n\n\x08response"<\n\x12\x43\x61ncelSubscribeReq\x12\r\n\x05ReqId\x18\x01 \x01(\x03\x12\x17\n\x0fsubscription_id\x18\x02 \x01(\x04"\xe0\x01\n\x0eGetModelsInput\x12\x11\n\trequestId\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tnamespace\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\x12Z\n\x0brequestType\x18\x05 \x01(\x0e\x32\x45.IOSXRExtensibleManagabilityService.GetModelsInput.MODLE_REQUEST_TYPE"-\n\x12MODLE_REQUEST_TYPE\x12\x0b\n\x07SUMMARY\x10\x00\x12\n\n\x06\x44\x45TAIL\x10\x01"\xea\x02\n\x0fGetModelsOutput\x12\x11\n\trequestId\x18\x01 \x01(\x04\x12M\n\x06models\x18\x02 \x03(\x0b\x32=.IOSXRExtensibleManagabilityService.GetModelsOutput.ModelInfo\x12N\n\x0cresponseCode\x18\x03 \x01(\x0e\x32\x38.IOSXRExtensibleManagabilityService.OC_RPC_RESPONSE_TYPE\x12\x0b\n\x03msg\x18\x04 \x01(\t\x1a\x97\x01\n\tModelInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tnamespace\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x45\n\tmodelType\x18\x04 \x01(\x0e\x32\x32.IOSXRExtensibleManagabilityService.GET_MODEL_TYPE\x12\x11\n\tmodelData\x18\x05 \x01(\t"3\n\x10GetProtoFileArgs\x12\r\n\x05reqId\x18\x01 \x01(\x03\x12\x10\n\x08yangPath\x18\x02 \x01(\t"H\n\x11GetProtoFileReply\x12\r\n\x05reqId\x18\x01 \x01(\x03\x12\x14\n\x0cprotoContent\x18\x02 \x01(\t\x12\x0e\n\x06\x65rrors\x18\x03 \x01(\t*3\n\x0c\x43ommitResult\x12\n\n\x06\x43HANGE\x10\x00\x12\r\n\tNO_CHANGE\x10\x01\x12\x08\n\x04\x46\x41IL\x10\x02*\xbb\x01\n\x14OC_RPC_RESPONSE_TYPE\x12\x06\n\x02OK\x10\x00\x12\x07\n\x03NOK\x10\x01\x12\x14\n\x10UNSUPPORTED_PATH\x10\x02\x12\x10\n\x0cINVALID_PATH\x10\x03\x12\x19\n\x15INVALID_CONFIGURATION\x10\x04\x12\x18\n\x14UNSUPPORTED_INTERVAL\x10\x05\x12\x18\n\x14UNSUPPORTED_ENCODING\x10\x06\x12\x1b\n\x17INVALID_SUBSCRIPTION_ID\x10\x07*I\n\x0eGET_MODEL_TYPE\x12\n\n\x06MODULE\x10\x00\x12\x10\n\x0c\x41UGMENTATION\x10\x01\x12\r\n\tDEVIATION\x10\x02\x12\n\n\x06\x42UNDLE\x10\x03\x32\xba\x0b\n\x0egRPCConfigOper\x12v\n\tGetConfig\x12\x31.IOSXRExtensibleManagabilityService.ConfigGetArgs\x1a\x32.IOSXRExtensibleManagabilityService.ConfigGetReply"\x00\x30\x01\x12p\n\x0bMergeConfig\x12..IOSXRExtensibleManagabilityService.ConfigArgs\x1a/.IOSXRExtensibleManagabilityService.ConfigReply"\x00\x12q\n\x0c\x44\x65leteConfig\x12..IOSXRExtensibleManagabilityService.ConfigArgs\x1a/.IOSXRExtensibleManagabilityService.ConfigReply"\x00\x12q\n\x0cRemoveConfig\x12..IOSXRExtensibleManagabilityService.ConfigArgs\x1a/.IOSXRExtensibleManagabilityService.ConfigReply"\x00\x12r\n\rReplaceConfig\x12..IOSXRExtensibleManagabilityService.ConfigArgs\x1a/.IOSXRExtensibleManagabilityService.ConfigReply"\x00\x12t\n\tCliConfig\x12\x31.IOSXRExtensibleManagabilityService.CliConfigArgs\x1a\x32.IOSXRExtensibleManagabilityService.CliConfigReply"\x00\x12\x80\x01\n\rCommitReplace\x12\x35.IOSXRExtensibleManagabilityService.CommitReplaceArgs\x1a\x36.IOSXRExtensibleManagabilityService.CommitReplaceReply"\x00\x12q\n\x0c\x43ommitConfig\x12..IOSXRExtensibleManagabilityService.CommitArgs\x1a/.IOSXRExtensibleManagabilityService.CommitReply"\x00\x12\x89\x01\n\x14\x43onfigDiscardChanges\x12\x36.IOSXRExtensibleManagabilityService.DiscardChangesArgs\x1a\x37.IOSXRExtensibleManagabilityService.DiscardChangesReply"\x00\x12p\n\x07GetOper\x12/.IOSXRExtensibleManagabilityService.GetOperArgs\x1a\x30.IOSXRExtensibleManagabilityService.GetOperReply"\x00\x30\x01\x12y\n\nCreateSubs\x12\x32.IOSXRExtensibleManagabilityService.CreateSubsArgs\x1a\x33.IOSXRExtensibleManagabilityService.CreateSubsReply"\x00\x30\x01\x12\x7f\n\x0cGetProtoFile\x12\x34.IOSXRExtensibleManagabilityService.GetProtoFileArgs\x1a\x35.IOSXRExtensibleManagabilityService.GetProtoFileReply"\x00\x30\x01\x32\x85\x03\n\x08gRPCExec\x12~\n\x11ShowCmdTextOutput\x12/.IOSXRExtensibleManagabilityService.ShowCmdArgs\x1a\x34.IOSXRExtensibleManagabilityService.ShowCmdTextReply"\x00\x30\x01\x12~\n\x11ShowCmdJSONOutput\x12/.IOSXRExtensibleManagabilityService.ShowCmdArgs\x1a\x34.IOSXRExtensibleManagabilityService.ShowCmdJSONReply"\x00\x30\x01\x12y\n\nActionJSON\x12\x32.IOSXRExtensibleManagabilityService.ActionJSONArgs\x1a\x33.IOSXRExtensibleManagabilityService.ActionJSONReply"\x00\x30\x01\x32\x9a\x03\n\x0eOpenConfiggRPC\x12\x85\x01\n\x12SubscribeTelemetry\x12\x34.IOSXRExtensibleManagabilityService.SubscribeRequest\x1a\x35.IOSXRExtensibleManagabilityService.SubscribeResponse"\x00\x30\x01\x12\x87\x01\n\x14UnSubscribeTelemetry\x12\x36.IOSXRExtensibleManagabilityService.CancelSubscribeReq\x1a\x35.IOSXRExtensibleManagabilityService.SubscribeResponse"\x00\x12v\n\tGetModels\x12\x32.IOSXRExtensibleManagabilityService.GetModelsInput\x1a\x33.IOSXRExtensibleManagabilityService.GetModelsOutput"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "iosxr_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals["_COMMITRESULT"]._serialized_start = 3449
    _globals["_COMMITRESULT"]._serialized_end = 3500
    _globals["_OC_RPC_RESPONSE_TYPE"]._serialized_start = 3503
    _globals["_OC_RPC_RESPONSE_TYPE"]._serialized_end = 3690
    _globals["_GET_MODEL_TYPE"]._serialized_start = 3692
    _globals["_GET_MODEL_TYPE"]._serialized_end = 3765
    _globals["_CONFIGGETARGS"]._serialized_start = 51
    _globals["_CONFIGGETARGS"]._serialized_end = 103
    _globals["_CONFIGGETREPLY"]._serialized_start = 105
    _globals["_CONFIGGETREPLY"]._serialized_end = 173
    _globals["_GETOPERARGS"]._serialized_start = 175
    _globals["_GETOPERARGS"]._serialized_end = 225
    _globals["_GETOPERREPLY"]._serialized_start = 227
    _globals["_GETOPERREPLY"]._serialized_end = 293
    _globals["_CONFIGARGS"]._serialized_start = 295
    _globals["_CONFIGARGS"]._serialized_end = 383
    _globals["_CONFIGREPLY"]._serialized_start = 385
    _globals["_CONFIGREPLY"]._serialized_end = 450
    _globals["_CLICONFIGARGS"]._serialized_start = 452
    _globals["_CLICONFIGARGS"]._serialized_end = 538
    _globals["_CLICONFIGREPLY"]._serialized_start = 540
    _globals["_CLICONFIGREPLY"]._serialized_end = 608
    _globals["_COMMITREPLACEARGS"]._serialized_start = 610
    _globals["_COMMITREPLACEARGS"]._serialized_end = 675
    _globals["_COMMITREPLACEREPLY"]._serialized_start = 677
    _globals["_COMMITREPLACEREPLY"]._serialized_end = 731
    _globals["_COMMITMSG"]._serialized_start = 733
    _globals["_COMMITMSG"]._serialized_end = 776
    _globals["_COMMITARGS"]._serialized_start = 778
    _globals["_COMMITARGS"]._serialized_end = 823
    _globals["_COMMITREPLY"]._serialized_start = 825
    _globals["_COMMITREPLY"]._serialized_end = 872
    _globals["_DISCARDCHANGESARGS"]._serialized_start = 874
    _globals["_DISCARDCHANGESARGS"]._serialized_end = 909
    _globals["_DISCARDCHANGESREPLY"]._serialized_start = 911
    _globals["_DISCARDCHANGESREPLY"]._serialized_end = 966
    _globals["_SHOWCMDARGS"]._serialized_start = 968
    _globals["_SHOWCMDARGS"]._serialized_end = 1009
    _globals["_SHOWCMDTEXTREPLY"]._serialized_start = 1011
    _globals["_SHOWCMDTEXTREPLY"]._serialized_end = 1079
    _globals["_SHOWCMDJSONREPLY"]._serialized_start = 1081
    _globals["_SHOWCMDJSONREPLY"]._serialized_end = 1153
    _globals["_QOSMARKING"]._serialized_start = 1155
    _globals["_QOSMARKING"]._serialized_end = 1184
    _globals["_CREATESUBSARGS"]._serialized_start = 1187
    _globals["_CREATESUBSARGS"]._serialized_end = 1336
    _globals["_ACTIONJSONARGS"]._serialized_start = 1338
    _globals["_ACTIONJSONARGS"]._serialized_end = 1391
    _globals["_ACTIONJSONREPLY"]._serialized_start = 1393
    _globals["_ACTIONJSONREPLY"]._serialized_end = 1462
    _globals["_CREATESUBSREPLY"]._serialized_start = 1464
    _globals["_CREATESUBSREPLY"]._serialized_end = 1529
    _globals["_SUBSCRIBEREQUEST"]._serialized_start = 1531
    _globals["_SUBSCRIBEREQUEST"]._serialized_end = 1650
    _globals["_TELEMETRYSTREAMDESTINATION"]._serialized_start = 1653
    _globals["_TELEMETRYSTREAMDESTINATION"]._serialized_end = 1873
    _globals["_TELEMETRYSTREAMDESTINATION_TSP"]._serialized_start = 1841
    _globals["_TELEMETRYSTREAMDESTINATION_TSP"]._serialized_end = 1873
    _globals["_TELEMETRYPATH"]._serialized_start = 1875
    _globals["_TELEMETRYPATH"]._serialized_end = 1904
    _globals["_SUBSCRIPTIONLIST"]._serialized_start = 1907
    _globals["_SUBSCRIPTIONLIST"]._serialized_end = 2309
    _globals["_SUBSCRIPTIONLIST_ENC_SPEC"]._serialized_start = 2270
    _globals["_SUBSCRIPTIONLIST_ENC_SPEC"]._serialized_end = 2309
    _globals["_STATUSRESPONSE"]._serialized_start = 2311
    _globals["_STATUSRESPONSE"]._serialized_end = 2421
    _globals["_NOTIFICATION"]._serialized_start = 2423
    _globals["_NOTIFICATION"]._serialized_end = 2451
    _globals["_SUBSCRIBERESPONSE"]._serialized_start = 2454
    _globals["_SUBSCRIBERESPONSE"]._serialized_end = 2666
    _globals["_CANCELSUBSCRIBEREQ"]._serialized_start = 2668
    _globals["_CANCELSUBSCRIBEREQ"]._serialized_end = 2728
    _globals["_GETMODELSINPUT"]._serialized_start = 2731
    _globals["_GETMODELSINPUT"]._serialized_end = 2955
    _globals["_GETMODELSINPUT_MODLE_REQUEST_TYPE"]._serialized_start = 2910
    _globals["_GETMODELSINPUT_MODLE_REQUEST_TYPE"]._serialized_end = 2955
    _globals["_GETMODELSOUTPUT"]._serialized_start = 2958
    _globals["_GETMODELSOUTPUT"]._serialized_end = 3320
    _globals["_GETMODELSOUTPUT_MODELINFO"]._serialized_start = 3169
    _globals["_GETMODELSOUTPUT_MODELINFO"]._serialized_end = 3320
    _globals["_GETPROTOFILEARGS"]._serialized_start = 3322
    _globals["_GETPROTOFILEARGS"]._serialized_end = 3373
    _globals["_GETPROTOFILEREPLY"]._serialized_start = 3375
    _globals["_GETPROTOFILEREPLY"]._serialized_end = 3447
    _globals["_GRPCCONFIGOPER"]._serialized_start = 3768
    _globals["_GRPCCONFIGOPER"]._serialized_end = 5234
    _globals["_GRPCEXEC"]._serialized_start = 5237
    _globals["_GRPCEXEC"]._serialized_end = 5626
    _globals["_OPENCONFIGGRPC"]._serialized_start = 5629
    _globals["_OPENCONFIGGRPC"]._serialized_end = 6039
# @@protoc_insertion_point(module_scope)
