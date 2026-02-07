from Bio.SeqIO.FastaIO import SimpleFastaParser

sequences = []

# Builds list of sequence dictionaries 
with open('immune_proteins.fasta', 'r') as f:
    for header, sequence in SimpleFastaParser(f):
        parts = header.split("|")
        entry = {
            "accession": parts[1], 
            "sequence": sequence,
            "length": len(sequence)
        }
        sequences.append(entry)


# Counts up the total number of residues 
res_count = 0

for seq in sequences:
    res_count += seq['length']


# Finds the shortest and longest sequence 
longest_length = 0
shortest_length = 1000000
longest_seq = None
shortest_seq = None

for seq in sequences:
    if seq['length'] > longest_length:
        longest_length = seq['length']
        longest_seq = seq
    elif seq['length'] < shortest_length:
        shortest_length = seq['length']
        shortest_seq = seq



# Print outputs 
print(f"Num Sequences {len(sequences)}")
print(f"Total Residues: {res_count}")
print(f"Longest Accession: {longest_seq['accession']} ({longest_seq['length']} residues)")
print(f"Shortest Accession: {shortest_seq['accession']} ({shortest_seq['length']} residues)")