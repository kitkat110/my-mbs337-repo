import json
import csv

with open('proteins.json', 'r') as f:
    prot_data = json.load(f)

with open('proteins.csv', 'w') as o:
    csv_writer = csv.writer(o)

    # Manually write header row with flattened field names
    header = ['primaryAccession',
              'proteinName',
              'geneName',
              'organism_scientificName',
              'sequence_length',
              'sequence_mass',
              'function']
    csv_writer.writerow(header)

    # Write data rows, extracting nested values
    for prot in prot_data['protein_list']:
        row = [
            prot['primaryAccession'],
            prot['proteinName'],
            prot['geneName'],
            prot['organism']['scientificName'],
            prot['sequence']['length'],
            prot['sequence']['mass'],
            prot['function']
        ]
        csv_writer.writerow(row)

