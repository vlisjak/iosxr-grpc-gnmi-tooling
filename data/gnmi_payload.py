
# configure MSID
# json_payload = '''
# {
#     "Cisco-IOS-XR-segment-routing-ms-cfg:sr": {
#         "Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering": {
#             "maximum-sid-depth": 8
#         }
#     }
# }
# '''

# configure link shutdown 
json_payload = '''
{
  "openconfig-interfaces:interfaces": {
   "interface": [
    {
     "name": "Loopback200",
     "config": {
      "name": "Loopback200",
      "type": "iana-if-type:softwareLoopback",
      "enabled": false
     }
    }
   ]
 }
}
'''

# configure Null0 static route
# json_payload = '''
# {
#   "openconfig-network-instance:network-instances": {
#    "network-instance": [
#     {
#      "name": "DEFAULT",
#      "protocols": {
#       "protocol": [
#        {
#         "identifier": "openconfig-policy-types:STATIC",
#         "name": "DEFAULT",
#         "config": {
#          "identifier": "openconfig-policy-types:STATIC",
#          "name": "DEFAULT"
#         },
#         "static-routes": {
#          "static": [
#           {
#            "prefix": "5.5.5.5/32",
#            "config": {
#             "prefix": "5.5.5.5/32"
#            },
#            "next-hops": {
#             "next-hop": [
#              {
#               "index": "##DROP##",
#               "config": {
#                "index": "##DROP##",
#                "next-hop": "openconfig-local-routing:DROP"
#               }
#              }
#             ]
#            }
#           }
#          ]
#         }
#        }
#       ]
#      }
#     }
#    ]
#   }
#  }
# '''

# apply SR-TE affinity to core link -> this is wrong because it conifgures mpls rsvp-te affinity!
# json_payload = '''
# {
#   "openconfig-network-instance:network-instances": {
#    "network-instance": [
#     {
#       "name": "DEFAULT",
#       "mpls": {
#         "te-interface-attributes": {
#           "interface": [
#             {
#               "interface-id": "GigabitEthernet0/0/0/5",
#               "config": {
#                 "interface-id": "GigabitEthernet0/0/0/5",
#                 "admin-group": [
#                   "R10-R11"
#                 ]
#               }
#             }
#           ]
#         }
#       }
#     }
#    ]
#   }
# }
# '''

# # apply SR-TE affinity to core link
# json_payload = '''
# {
#   "Cisco-IOS-XR-segment-routing-ms-cfg:sr": {
#     "Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering": {
#       "srte-interfaces": {
#         "srte-interface": [
#           {
#             "srte-interface-name": "GigabitEthernet0/0/0/5",
#             "interface-affinities": {
#               "interface-affinity": [
#                 {
#                   "affinity-name": "R10-R11"
#                 }
#               ]
#             }
#           }
#         ]
#       }
#     }
#   }
# }
# '''

# apply "loopback external" under interface
# json_payload = '''
# {
#   "Cisco-IOS-XR-um-interface-cfg:interfaces": {
#     "interface": [
#       {
#         "interface-name": "HundredGigE0/0/0/24",
#         "Cisco-IOS-XR-um-if-ethernet-cfg:loopback": "internal"
#       }
#     ]
#   }
# }
# '''

# apply "loopback" under interface
# TERMINAL -> loopback internal
# FACILITY -> loopback line
# >> we do not have OC keyword to configure loopback external!
# json_payload = '''
# {
#   "openconfig-interfaces:interfaces": {
#     "interface": [
#       {
#         "config": {
#           "loopback-mode": "NONE",
#           "name": "HundredGigE0/0/0/24",
#           "type": "iana-if-type:ethernetCsmacd"
#         },
#         "name": "HundredGigE0/0/0/24"
#       }
#     ]
#   }
# }
# '''

# prefix = "openconfig://"
# gnmi_path = [
#   "openconfig-network-instance:network-instances/network-instance[name=DEFAULT]/protocols/protocol[identifier=STATIC][name=DEFAULT]/static-routes/static[prefix=5.5.5.5/32]"
# ]

# default if not specified: 'openconfig' 
# # -> Error: gNMI: invalid YangGetGnmi: rpc error: code = Internal desc = prefix and path origins do not match

# prefix = "cisco_native://"
# gnmi_path = [
#   # "/Cisco-IOS-XR-clns-isis-oper:isis/instances/instance/levels/level/detailed-lsps"
#   "/Cisco-IOS-XR-clns-isis-oper:isis/instances/instance[instance-name=1]/levels/level[level=level2]/detailed-lsps/detailed-lsp[lsp-id=0100.4900.2000.00-00]"
# ]

# prefix = "cisco_native://"
# gnmi_path = [
#   "/Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/srte-interfaces/srte-interface[srte-interface-name=GigabitEthernet0/0/0/5]"
# ]

# prefix = "openconfig://"
# prefix = "cisco_native://"
# gnmi_path = [
  # "/openconfig-interfaces:interfaces/interface[name=HundredGigE0/0/0/24]/state/loopback-mode"
  # "/Cisco-IOS-XR-ifmgr-oper:interface-properties/data-nodes/data-node/locationviews/locationview/interfaces/interface[interface-name=HundredGigE0/0/0/7]"
  # "/Cisco-IOS-XR-ifmgr-oper:interface-properties"
  # "/openconfig-interfaces:interfaces/interface[name=HundredGigE0/0/0/24]"
  # "/openconfig-interfaces:interfaces/interface[name=HundredGigE0/0/0/24]/subinterfaces/subinterface[index=0]/openconfig-if-ip:ipv4/addresses/address"
  # "/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/interface-xr/interface[interface-name=HundredGigE0/0/0/24]/loopback-configuration"
# ]

prefix = "cisco_native://"
gnmi_path = [
  # "/Cisco-IOS-XR-ipv4-bgp-oper:/bgp/instances/instance/instance-active"
  # "/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib"
  "/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table"
]

# get affinity of a link in isis database
# prefix = "openconfig://"
# gnmi_path = [
#   # First find the path for link with given IP address:
#   # "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/extended-is-reachability/neighbors/neighbor/instances/instance/subtlvs/subtlv/ipv4-interface-address[state=10.10.10.100]/"
#   # Then use the specific path to fetch affinity (admin-group)
#   "/openconfig-network-instance:network-instances/network-instance[name=DEFAULT]/protocols/protocol[identifier=ISIS][name=1]/isis/levels/level[level-number=2]/link-state-database/lsp[lsp-id=0100.4900.2000.00-00]/tlvs/tlv[type=EXTENDED_IS_REACHABILITY]/extended-is-reachability/neighbors/neighbor[system-id=0100.4900.2010]/instances/instance[id=8740929536]/subtlvs/subtlv/admin-group"
# ]

# Get InQ/OutQ from "show bgp all all sum"
# Get # of prefixes sent to neighbor
# prefix = "openconfig://"
# gnmi_path = [
#   # "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state/queues"
#   # "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state/queues/input"
#   # "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state/queues/output"
#   # "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state/peer-group",
#   # "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state/neighbor-address"
#   # "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor[neighbor-address=11.0.0.88]/state/queues",
#   # "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor[neighbor-address=11.0.0.88]/afi-safis/afi-safi/state/prefixes/sent",
#   # "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor[neighbor-address=2000:1:0:a3::]/state/session-state"
# ]

# prefix = "cli://"
# gnmi_path = [
#   # "show version"
#   # "show bgp sum"
#   # "show bgp ipv4 flowspec Dest:20.20.1.0/24,DPort:=443/72"
#   "show bgp ipv4 flowspec dest-prefix 20.20.1.0/24"
# ]

# gnmic get --path 'cli:/show bgp ipv4 flowspec dest-prefix 20.20.1.0/24' --skip-verify --username cisco --password cisco --port 57344 -a 10.52.158.238  -e ascii --timeout 180s