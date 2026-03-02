from Bio import Entrez, SeqIO

Entrez.email = "A.N.Other@example.com"

gb_rec = []
with Entrez.esearch(db="protein", term="Arabidopsis thaliana AND AT5G10140", rettype = "gb", retmax=30) as h:
    results = Entrez.read(h)
    record = SeqIO.parse(h, "gb")
    gb_rec = list(record)
    print(gb_rec[0])

    
