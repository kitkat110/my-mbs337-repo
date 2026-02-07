from Bio.SeqIO.FastaIO import SimpleFastaParser

# Read input FASTA and output matches to a new output FASTA
with open('immune_proteins.fasta', 'r') as infile, open ('long_only.fasta', 'w') as outfile:
    for header, sequence in SimpleFastaParser(infile):
        if len(sequence) >= 1000:
            outfile.write(f">{header}\n")
            outfile.write(f"{sequence}\n")

            



        