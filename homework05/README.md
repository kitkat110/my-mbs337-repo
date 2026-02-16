# Homework 05

## About
This directory contains all the files for **Homework 05**, which focuses best practices in Python. The goal of this homework is to build a proper Python script, applying **code organization**, **documentation**, **logging**, and **error handling**.

## Directory Structure
```
my-mbs337-repo/
├── homework05/
│   ├── mmcif_summary.py
│   ├── output_files/
│   │   └── 4HHB_summary.json
│   └── README.md
```

## Input Files
Input files are downloaded separately:

**mmCIF**
```bash
wget https://files.rcsb.org/download/4HHB.cif.gz
gunzip 4HHB.cif.gz
```

## Scripts
- `mmcif_summary.py`: Parses an mmCIF file, computes total number of residues, including standard and hetero residues, and writes the summary as a dictionary to a JSON file

## Output Files
Generated files are stored in `output_files/`:
- `4HHB_summary.json`: JSON file containing a dictionary of hemoglobin chains and their residue counts