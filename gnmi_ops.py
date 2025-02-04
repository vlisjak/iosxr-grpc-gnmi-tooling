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

from data.gnmi_payload import prefix

try:
  from data.gnmi_payload import gnmi_path
except:
  print("ERROR --> gnmi_path undefined in data/gnmi_payload.py")

try:
  from data.gnmi_payload import json_payload
except:
  print("ERROR --> json_payload undefined in data/gnmi_payload.py")

def config_update(update_payload, gnmi_target):
  updates = []
  for key,val in json.loads(update_payload).items():
      updates.append((key,val))
  with gNMIclient(**gnmi_target) as gc:
      result = gc.set(prefix=prefix, update=updates, encoding='json_ietf')
      pp.pprint(result)

def get(path, gnmi_target):
  with gNMIclient(**gnmi_target) as gc:
      result = gc.get(prefix = prefix, path=path, encoding='json_ietf', datatype='all')
      pp.pprint(result)

def get_cli(path, gnmi_target):
  """Execute "show" commands with gnmi, such as "show version", "show running"..."""
  with gNMIclient(**gnmi_target) as gc:
      result = gc.get(prefix = prefix, path=path, encoding='ascii', datatype='all')
      pp.pprint(result)

def config_delete(path, gnmi_target):
  with gNMIclient(**gnmi_target) as gc:
      result = gc.set(delete=path, encoding='json_ietf')
      pp.pprint(result)

if __name__ == '__main__':
  # config_update(update_payload=json_payload, gnmi_target=gnmi_target)
  # get(path=gnmi_path, gnmi_target=gnmi_target)
  get_cli(path=gnmi_path, gnmi_target=gnmi_target)
  # config_delete(path=gnmi_path, gnmi_target=gnmi_target)
