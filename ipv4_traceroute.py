#!/usr/bin/env python

import grpc
import iosxr_pb2 as pb2
import iosxr_pb2_grpc as pb2_grpc
import json

# Install:
# python -m pip install grpcio
# python -m pip install protobuf

# Download .proto file:
# https://github.com/nleiva/xrgrpc/blob/v0.6.0/proto/ems/ems_grpc.proto

# Run:
# python -m grpc_tools.protoc --proto_path=. ./iosxr.proto --python_out=. --grpc_python_out=.

if __name__ == "__main__":

    target = "192.168.101.41:57400"
    username = "cisco"
    password = "Cisco!123"

    destination = "10.255.1.43"
    source = "10.255.1.41"

    grpc_payload = {"Cisco-IOS-XR-traceroute-act:traceroute": {"ipv4": {"source": source, "destination": destination, "numeric": True}}}

    metadata = (
        ("username", username),
        ("password", password),
    )

    with grpc.insecure_channel(target, options=(("grpc.enable_http_proxy", 0),)) as channel:
        stub = pb2_grpc.gRPCExecStub(channel)

        message = pb2.ActionJSONArgs(ReqId=0, yangpathjson=json.dumps(grpc_payload))

        result = []
        for m in stub.ActionJSON(message, metadata=metadata):
            result.append(m)

        result_json = json.loads(result[0].yangjson)
        for hop in result_json["Cisco-IOS-XR-traceroute-act:output"]["traceroute-response"]["ipv4"]["hops"]["hop"]:
            print(hop["hop-index"], hop["hop-address"])
