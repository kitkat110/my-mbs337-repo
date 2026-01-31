import json
import xmltodict

with open('proteins.json', 'r') as f:
    prot_data = json.load(f)

root = {}
root['prot_data'] = prot_data

with open('proteins.xml', 'w') as o:
    o.write(xmltodict.unparse(root, pretty=True))
