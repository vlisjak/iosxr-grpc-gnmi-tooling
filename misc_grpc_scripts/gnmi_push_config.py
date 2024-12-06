from pygnmi.client import gNMIclient
import json
import pprint as pp

ip = '10.52.157.183'
port = 57344
user = 'cisco'
pwd = 'cisco123'

# json_payload = '''
# {
#     "Cisco-IOS-XR-segment-routing-ms-cfg:sr": {
#         "Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering": {
#             "maximum-sid-depth": 8
#         }
#     }
# }
# '''

# json_payload = '''
# {
#   "openconfig-interfaces:interfaces": {
#    "interface": [
#     {
#      "name": "GigabitEthernet0/0/0/3",
#      "config": {
#       "name": "GigabitEthernet0/0/0/3",
#       "type": "iana-if-type:ethernetCsmacd",
#       "enabled": false
#      }
#     }
#    ]
#  }
# }
# '''

json_payload = '''
{
  "openconfig-network-instance:network-instances": {
   "network-instance": [
    {
     "name": "DEFAULT",
     "protocols": {
      "protocol": [
       {
        "identifier": "openconfig-policy-types:STATIC",
        "name": "DEFAULT",
        "config": {
         "identifier": "openconfig-policy-types:STATIC",
         "name": "DEFAULT"
        },
        "static-routes": {
         "static": [
          {
           "prefix": "5.5.5.5/32",
           "config": {
            "prefix": "5.5.5.5/32"
           },
           "next-hops": {
            "next-hop": [
             {
              "index": "##DROP##",
              "config": {
               "index": "##DROP##",
               "next-hop": "openconfig-local-routing:DROP"
              }
             }
            ]
           }
          }
         ]
        }
       }
      ]
     }
    }
   ]
  }
 }
'''

gnmi_path = [
  "openconfig-network-instance:network-instances/network-instance[name=DEFAULT]/protocols/protocol[identifier=STATIC][name=DEFAULT]/static-routes/static[prefix=5.5.5.5/32]"
]

def config_update(update_payload):
  updates = []
  for key,val in json.loads(update_payload).items():
      updates.append((key,val))
  with gNMIclient(target=(ip, port), username=user, password=pwd, grpc_options=[("grpc.enable_http_proxy", 0),], insecure=True, debug=False) as gc:
      update_request = gc.set(update=updates, encoding='json_ietf')
      pp.pprint(update_request)

def config_get(path):
  with gNMIclient(target=(ip, port), username=user, password=pwd, grpc_options=[("grpc.enable_http_proxy", 0),], insecure=True, debug=True) as gc:
      update_request = gc.get(path=path, encoding='json_ietf')
      pp.pprint(update_request)

def config_delete(path):
  with gNMIclient(target=(ip, port), username=user, password=pwd, grpc_options=[("grpc.enable_http_proxy", 0),], insecure=True, debug=False) as gc:
      update_request = gc.set(delete=path, encoding='json_ietf')
      pp.pprint(update_request)

if __name__ == '__main__':
  # config_update(update_payload=json_payload)
  config_get(path=gnmi_path)
  # config_delete(path=gnmi_path)