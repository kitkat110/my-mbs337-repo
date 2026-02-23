# Homework 06

## About
This directory contains all the files for **Homework 06**, which focuses on containerization. The goal of this homework is to containerize the scripts from the first 3 exercises from Homework04 and the script from Homework05, run the container to generate output from each script, and push the container to Docker Hub.

## Directory Structure
```
my-mbs337-repo/
 └── homework06/
     ├── Dockerfile
     ├── README.md
     ├── fasta_filter.py
     ├── fasta_stats.py
     ├── fastq_filter.py
     ├── mmcif_summary.py
     ├── output_files
     │   ├── 4HHB_summary.json
     │   ├── immune_proteins_stats.txt
     │   ├── long_only.fasta
     │   └── sample1_cleanReads.fastq
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
- `fasta_stats.py`: Computes FASTA statistics, including total number of sequences, total number of residues, and accession ID and length of the longest and shortest sequence 

- `fasta_filter.py`: Writes a new FASTA file containing only sequences >= 1000 residues

- `fastq_filter.py`: Filters FASTQ reads by average Phred quality (>= 30) and writes results to a new FASTQ file

- `mmcif_summary.py`: Parses an mmCIF file, computes total number of residues, including standard and hetero residues, and writes the summary as a dictionary to a JSON file

## Output Files
Generated files are stored in `output_files/`:
- `immune_proteins_stats.txt`:

- `long_only.fasta`:

- `sample1_cleanReads.fastq`:

- `4HHB_summary.json`: JSON file containing a dictionary of hemoglobin chains and their residue counts