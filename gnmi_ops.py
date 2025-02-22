from pygnmi.client import gNMIclient
import json
import pprint as pp

try:
  from data.gnmi_targets import gnmi_target
except:
  print("ERROR --> gnmi_target undefined in data/gnmi_targets.py")

try:
  from data.gnmi_targets_private import gnmi_target
except:
  print("ERROR --> gnmi_target undefined in data/gnmi_targets_private.py")

try:
  from data.gnmi_payload import prefix
except:
    print("ERROR --> gnmi_prefix undefined in data/gnmi_payload.py")

try:
  from data.gnmi_payload import gnmi_path
except:
  print("ERROR --> gnmi_path undefined in data/gnmi_payload.py")

try:
  from data.gnmi_payload import json_payload
except:
  print("ERROR --> json_payload undefined in data/gnmi_payload.py")

try:
  from data.gnmi_payload import update_paths
except:
    print("ERROR --> update_paths undefined in data/gnmi_payload.py")


def config_update(prefix, update_payload, gnmi_target):
  updates = []
  for key,val in json.loads(update_payload).items():
      updates.append((key,val))
  with gNMIclient(**gnmi_target) as gc:
      result = gc.set(prefix=prefix, update=updates, encoding='json_ietf')
      pp.pprint(result)

def config_replace(update_payload, gnmi_target):
  updates = []
  for key,val in json.loads(update_payload).items():
      updates.append((key,val))
  with gNMIclient(**gnmi_target) as gc:
      result = gc.set(replace=updates, encoding='json_ietf')
      pp.pprint(result)

def config_replace_file(json_file_payload, gnmi_target):
  with open(json_file_payload, 'r') as f:
      replace_payload = json.loads(f.read())
  replace_list = []
  for items in replace_payload:
      replace_list.append((items[0], items[1]))

  print(f'rpc_list root: {replace_list}')
  input('ok?')

  with gNMIclient(**gnmi_target) as gc:
      result = gc.set(replace=replace_list, encoding='json_ietf')
      pp.pprint(result)


def get(prefix, path, gnmi_target):
  with gNMIclient(**gnmi_target) as gc:
      result = gc.get(prefix=prefix, path=path, encoding='json_ietf', datatype='all')
      pp.pprint(result)

def get_full_config(gnmi_target):
  with gNMIclient(**gnmi_target) as gc:
      # note: this returns also openconfig, but only if the config was pushed as OC!
      result = gc.get(prefix='cisco_native:', path=['cisco_native:'], encoding='json_ietf', datatype='CONFIG')
      # note: we shall see openconfig only when device was also configured via OC !
      # result = gc.get(prefix='openconfig:', path=[], encoding='json_ietf', datatype='CONFIG')
      pp.pprint(result)

def get_cli(prefix, path, gnmi_target):
  """Execute "show" commands with gnmi, such as "show version", "show running"..."""
  with gNMIclient(**gnmi_target) as gc:
      result = gc.get(prefix=prefix, path=path, encoding='ascii', datatype='all')
      pp.pprint(result)

def config_delete(path, gnmi_target):
  with gNMIclient(**gnmi_target) as gc:
      result = gc.set(delete=path, encoding='json_ietf')
      pp.pprint(result)

if __name__ == '__main__':
  # config_replace_file(json_file_payload='data/gnmi_test_payload.json', gnmi_target=gnmi_target)
  # config_update(prefix=prefix, update_payload=json_payload, gnmi_target=gnmi_target)
  # config_replace(update_payload=json_payload, gnmi_target=gnmi_target)
  # get(prefix=prefix, path=gnmi_path, gnmi_target=gnmi_target)
  # get(prefix="", path="", gnmi_target=gnmi_target)
  # get_full_config(gnmi_target=gnmi_target)
  get_cli(prefix=prefix, path=gnmi_path, gnmi_target=gnmi_target)
  # config_delete(path=gnmi_path, gnmi_target=gnmi_target)
