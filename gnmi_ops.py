from pygnmi.client import gNMIclient
import json
import pprint as pp

from data.gnmi_targets import gnmi_target
# from data.gnmi_targets_private import gnmi_target
from data.gnmi_payload import prefix
from data.gnmi_payload import gnmi_path
from data.gnmi_payload import json_payload

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

def config_delete(path, gnmi_target):
  with gNMIclient(**gnmi_target) as gc:
      result = gc.set(delete=path, encoding='json_ietf')
      pp.pprint(result)

if __name__ == '__main__':
  config_update(update_payload=json_payload, gnmi_target=gnmi_target)
  get(path=gnmi_path, gnmi_target=gnmi_target)
  # config_delete(path=gnmi_path, gnmi_target=gnmi_target)
