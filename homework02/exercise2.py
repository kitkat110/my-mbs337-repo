from Bio.Seq import Seq

dna_seq = Seq("GAACCGGGAGGTGGGAATCCGTCACATATGAGAAGGTATTTGCCCGATAA")
gc_count = dna_seq.count("G") + dna_seq.count("C")
gc_content = (gc_count / len(dna_seq)) * 100
print(f"GC content: {gc_content:.2f}%")