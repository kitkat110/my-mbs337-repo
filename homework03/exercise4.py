import json
import yaml

with open('proteins.json', 'r') as f:
    prot_data = json.load(f)

with open('proteins.yaml', 'w') as o:
    yaml.dump(prot_data, o)