import grpc

# from ems import ems_grpc_pb2, ems_grpc_pb2_grpc
import ems.ems_grpc_pb2 as pb2
import ems.ems_grpc_pb2_grpc as pb2_grpc
import json
from grpc import ssl_channel_credentials
from grpc import metadata_call_credentials
from urllib.parse import quote_plus
import base64

# source:
# - https://github.com/MeganSun19/grpc_file_copy/blob/main/copyfile.py
# - also look at: https://github.com/MeganSun19/gnoi_file


# Create basic authentication header for HTTPS access (for source filesystem)
def create_https_basic_auth_header(username, password):
    """
    Generate the basic authentication header for HTTPS access.
    """
    credentials = f"{username}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
    return f"Basic {encoded_credentials}"


# Load server credentials (CA certificate)
def load_ca_cert(cert_path):
    """
    Load the CA certificate for the SSL connection.
    """
    with open(cert_path, "rb") as f:
        return f.read()


# Initialize the GRPC channel with SSL and authentication for the gRPC device access
def create_grpc_secure_channel(target, grpc_username, grpc_password, ca_cert_path):
    """
    Create a secure gRPC channel with SSL and authentication to the device.
    """
    # Load CA cert
    ca_cert = load_ca_cert(ca_cert_path)

    # Create basic authentication for gRPC access (device username/password)
    auth_creds = grpc.metadata_call_credentials(lambda context, callback: callback([("username", grpc_username), ("password", grpc_password)], None))

    # Create secure channel credentials with the CA cert
    channel_creds = ssl_channel_credentials(root_certificates=ca_cert)

    # Composite credentials: SSL + gRPC Auth
    composite_creds = grpc.composite_channel_credentials(channel_creds, auth_creds)

    # Establish a secure channel with the target and composite credentials
    options = (("grpc.ssl_target_name_override", "PE1-NCS57C3"),)  # device hostname
    channel = grpc.secure_channel(target, composite_creds, options)

    return channel


# Main function to initiate GRPC call
def main():
    # gRPC Device access credentials (for authentication to the device)
    grpc_target = "{ip}:57344"
    grpc_username = "{grpc_username}"
    grpc_password = "{grpc_password}"

    # HTTPS Server credentials (for source filesystem)
    https_username = "{https_username}"
    https_password = "{https_password}"
    https_server = "{https_server}"
    https_file = "ncs5500-infra-1.0.0.1-r2421.CSCwk73569.x86_64.rpm"

    # CA certificate path for SSL connection (for gRPC)
    ca_cert_path = "CA.cer"  # Path to your CA certificate

    # Create the secure gRPC channel for device communication
    channel = create_grpc_secure_channel(grpc_target, grpc_username, grpc_password, ca_cert_path)

    # Create the gRPC stub for file copy service
    stub = pb2_grpc.gRPCExecStub(channel)

    # Prepare the HTTPS URL with basic auth
    https_auth_header = create_https_basic_auth_header(https_username, https_password)
    sourcename = f"//{quote_plus(https_username)}:{quote_plus(https_password)}@{https_server}:/{https_file}"

    # Copy from https server to router:
    grpc_payload = {
        "Cisco-IOS-XR-shellutil-copy-act:copy": {
            "sourcename": sourcename,
            "destinationname": "/ncs5500-infra-1.0.0.1-r2421.CSCwk73569.x86_64.rpm",
            "sourcefilesystem": "https:",
            "destinationfilesystem": "harddisk:",
        }
    }
    # Copy from Active RP to Standby RP:
    # grpc_payload = {
    #     "Cisco-IOS-XR-shellutil-copy-act:copy": {
    #         "sourcename": "ncs5500-goldenk9-x-7.10.2-7_10_2_OSPF_GNF2_SMU_2107.iso",
    #         "destinationname": "ncs5500-goldenk9-x-7.10.2-7_10_2_OSPF_GNF2_SMU_2107.iso",
    #         "sourcefilesystem": "harddisk:",
    #         "destinationfilesystem": "harddisk:",
    #         "sourcelocation": "0/RP0/CPU0",
    #         "destinationlocation": "0/RP1/CPU0"
    #     }
    # }

    # Print the payload for debugging
    print("Final gRPC Payload:")
    print(json.dumps(grpc_payload, indent=4))

    # Create the GRPC message with the payload
    message = pb2.ActionJSONArgs(ReqId=0, yangpathjson=json.dumps(grpc_payload))

    # Prepare metadata for gRPC request (device authentication)
    grpc_metadata = [("username", grpc_username), ("password", grpc_password)]

    try:
        # Send gRPC request
        result = []
        for m in stub.ActionJSON(message, metadata=grpc_metadata):
            result.append(m)

        # Check if result is empty or invalid
        if result:
            # Print the full response to debug
            print("Full gRPC response:")
            print(result[0])

            # If yangjson is present, attempt to parse it
            if hasattr(result[0], "yangjson"):
                try:
                    result_json = json.loads(result[0].yangjson)
                    print("File copy response:")
                    print(result_json)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
                    print(f"Raw response: {result[0].yangjson}")
            else:
                print("No valid 'yangjson' field in response.")
        else:
            print("No valid response received.")

    except grpc.RpcError as e:
        print(f"Error occurred during gRPC call: {e.details()}")
        print(f"Status Code: {e.code()}")


if __name__ == "__main__":
    main()
