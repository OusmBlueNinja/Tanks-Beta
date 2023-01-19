import json, os
path = os.path.dirname(os.path.realpath(__file__))

# Prints string if debug is enabled
def debug(data):
  saveDir = f"{path}.json"
  f = open(f'{saveDir}')
  data = json.load(f)
  DEBUG = data['config']['debug']
  if DEBUG:
    print(data)