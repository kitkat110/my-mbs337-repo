from Bio.PDB.MMCIFParser import MMCIFParser

# Create a parser using the MMCIFParser Class (blueprint)
parser = MMCIFParser()

with open('4HHB.cif', 'r') as infile:
    # Use .get_structure method on our parser to create a structure object
    structure = parser.get_structure('hemoglobin', infile)

# Iterate through full structure hierarachy
for model in structure:
    for chain in model:
        NH_res_count = 0
        atom_count = 0

        for residue in chain: 

            hetfield, resseq, icode = residue.get_id()
            if hetfield == ' ': # ' ' = standard amino acids and nucleic acids
                NH_res_count += 1

                for atom in residue: # Goes to count atoms only if it's a non-hetero residue
                    atom_count += 1

        print(f"Chain {chain.get_id()}: {NH_res_count} residues, {atom_count} atoms")