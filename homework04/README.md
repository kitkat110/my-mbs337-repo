# Homework 04

## About
This directory contains all the files for **Homework 04**, which focuses on working with commonly used bioinformatics file formats: **FASTA**, **FASTQ**, and **mmCIF**. The goal of this homework is to gain hands-on experience parsing biological sequence and structure data using **Biopython**, performing basic analyses, filtering data, and and writing output files. 

## Directory Structure
```
my-mbs337-repo/
├── homework04/
│   ├── exercise1.py
│   ├── exercise2.py
│   ├── exercise3.py
│   ├── exercise4.py
│   ├── output_files/
│   │   ├── long_only.fasta
│   │   └── sample1_cleanReads.fastq
│   └── README.md
```

## Input Files
Input files are downloaded separately:

**FASTA**
```bash
wget https://github.com/TACC/mbs-337-sp26/raw/refs/heads/main/docs/unit03/sample-data/immune_proteins.fasta.gz
gunzip immune_proteins.fasta.gz
```

**FASTQ**
```bash
wget https://github.com/TACC/mbs-337-sp26/raw/refs/heads/main/docs/unit03/sample-data/sample1_rawReads.fastq.gz
gunzip sample1_rawReads.fastq.gz
```

**mmCIF**
```bash
wget https://files.rcsb.org/download/4HHB.cif.gz
gunzip 4HHB.cif.gz
```

## Scripts
- `exercise1.py`: Computes FASTA statistics, including total number of sequences, total number of residues, and accession ID and length of the longest and shortest sequence 

- `exercise2.py`: Writes a new FASTA file containing only sequences >= 1000 residues

- `exercise3.py`: Filters FASTQ reads by average Phred quality (>= 30) and writes results to a new FASTQ file

- `exercise4.py`: Parse an mmCIF file and reports residue and atom counts for each chain

## Output Files
Generated files are stored in `output_files/`:
- `long_only.fasta`
- `sample1_cleanReads.fastq`
