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

    target = "10.255.0.2:57400"
    username = "cisco"
    password = "cisco"

    # copy from http server to local disk
    grpc_payload = {
        "Cisco-IOS-XR-shellutil-copy-act:copy": {
            "sourcename": "test.txt",
            "sourcefilesystem": "http://10.255.0.1:8888/",
            "destinationname": "test.txt",
            "destinationfilesystem": "harddisk:/",
            "vrf": "clab-mgmt"
        }
    }

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

        try:
            result_json = json.loads(result[0].yangjson)
            print(result_json)
        except:
            result_json = json.loads(result[0].errors)
            print(result_json)
