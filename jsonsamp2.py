import json

with open('loadfile1.json') as f:
  data = json.load(f)

for state in data['states']:
    print(state['name'],state['abbreviation'])
del state['area_codes']

with open('dumpfile1.json', 'w') as f:
  json.dump(data, f, indent=3)
    