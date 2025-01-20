import grpc
import iosxr_pb2 as pb2
import iosxr_pb2_grpc as pb2_grpc
import json
#from cisco_gnmi.auth import CiscoAuthPlugin

# Install:
# python -m pip install grpcio
# python -m pip install protobuf
# python -m pip install cisco_gnmi

# Download .proto file:
# https://github.com/nleiva/xrgrpc/blob/v0.6.0/proto/ems/ems_grpc.proto

# Run:
# python -m grpc_tools.protoc --proto_path=. ./iosxr.proto --python_out=. --grpc_python_out=.

def secure_grpc_call_with_ca(target, grpc_payload, metadata, ca_cert_path):
    # Load the CA certificate from the file
    with open(ca_cert_path, 'rb') as cert_file:
        trusted_certs = cert_file.read()
        print('CA Certificate is opened...')
    
    # Create SSL credentials using the CA certificate
    credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
    channel_options = (
    ("grpc.ssl_target_name_override", targetIP),  # Override the server name for target
    ("grpc.enable_http_proxy", 0),
    )

    with grpc.secure_channel(target, credentials, options=channel_options) as channel:
        stub = pb2_grpc.gRPCExecStub(channel)
        print('TLS Secure Channel Initiated..')

        message = pb2.ActionJSONArgs(ReqId=0, yangpathjson=json.dumps(grpc_payload))
        
        print('GRPC Payload to send to router:')
        print(grpc_payload)

        result = []
        for response in stub.ActionJSON(message, metadata=metadata):
            result.append(response)
            print(response, metadata)

    return result

if __name__ == "__main__":
    targetIP = "hostname.cisco.com"  # Replace with your actual target
    targetPort = "57344"
    target = (targetIP + ':' + targetPort)
    username = "cisco"
    password = "cisco"
    session_name = "FILESPAN"
    ca_cert_path = "data/CA.cer"  # Path to the CA certificate file

    grpc_payload = {
        'Cisco-IOS-XR-Ethernet-SPAN-act:packet-collection-start': { 
            'session': session_name 
            } 
        }

    metadata = (
        ("username", username),
        ("password", password),
    )

    try:
        results = secure_grpc_call_with_ca(target, grpc_payload, metadata, ca_cert_path)
        print("GRPC Call Results:", results)
    except grpc.RpcError as e:
        print(f"GRPC Call failed: {e.code()} - {e.details()}")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")