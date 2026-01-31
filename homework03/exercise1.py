import json
from pydantic import BaseModel

class ProteinEntry(BaseModel):
    primaryAccession: str
    organism: dict
    proteinName: str
    sequence: dict
    geneName: str
    function: str

proteins = []
with open('proteins.json', 'r') as f:
    prot_data = json.load(f)
for prot in prot_data["protein_list"]:
    proteins.append(ProteinEntry(**prot))


# Finds total combined mass of all proteins in the dataset
def find_total_mass(proteins: list[ProteinEntry]) -> int:
    total_mass = 0

    for prot in proteins:
        total_mass += prot.sequence.get('mass')
    
    return total_mass

print(f"The total combined mass of all proteins is {find_total_mass(proteins)} Daltons")

# Finds any proteins with a sequence length greater than or equal to 1000
def find_large_proteins(proteins: list[ProteinEntry]) -> list:
    large_proteins = []

    for prot in proteins:
        if prot.sequence.get('length') >= 1000:
            large_proteins.append(prot.proteinName)

    return large_proteins

print(f"Proteins with a sequence length greater than or equal to 1000: {find_large_proteins(proteins)}")

# Finds any non-eukaryotic proteins

def find_non_eukaryotes(proteins: list[ProteinEntry]) -> list:
    non_eukaryotes = []

    for prot in proteins:
        if 'Eukaryota' not in prot.organism['lineage']:
            non_eukaryotes.append(prot.proteinName)
    
    return non_eukaryotes

print(f"Non-eukaryotic proteins: {find_non_eukaryotes(proteins)}")

