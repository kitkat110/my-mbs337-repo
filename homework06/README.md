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

## Summary Workflow
1. Clone repository
2. Download input files
3. Build Docker image
4. Run each script using `docker run` with proper options
5. Find generated output files in output_files/

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

All input files should be placed in the `homework06/` directory before running the container.

## Building the Docker Image
From inside the `homework06/` directory, build the container:
```bash
docker build -t kitkat110/bio-container:1.0 .
```

- `-t`: Assign a name and tag to the image
- `.`: Tells Docker to use the Dockerfile in the current directory

Verify the image was created:
```bash
docker images
```

## Running the Container
All scripts are executed using `docker run`.

To ensure proper file permissions and access to input/output files, the following options must be used:

- `--rm`: Remove the container on exit

- `-v $PWD:/data`: Mount the current directory to `/data`

- `-u $(id -u):$(id -g)`: Run container as current user so output files aren't owned by root

### General format:
```bash
docker run --rm \
  -u $(id -u):$(id -g) \
  -v $PWD:/data \
  kitkat110/bio-container:1.0 \
  <script_name> <arguments>
```

## Script Usage and Parameters
`fasta_stats.py`: Computes FASTA statistics, including total number of sequences, total number of residues, and accession ID and length of the longest and shortest sequence 

### Parameters:
```bash
fasta_stats.py input_fasta output_txt [-l LOGLEVEL]
```

- `input_fasta`: Path to FASTA file

- `output_file`: Path to output text file

- `-l` or `--loglevel`: Optional logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

### Example:
```bash
docker run --rm -u $(id -u):$(id -g) -v $PWD:/data \
kitkat110/bio-container:1.0 \
fasta_stats.py \
/data/immune_proteins.fasta \
/data/output_files/immune_proteins_stats.txt
```

`fasta_filter.py`: Writes a new FASTA file containing only sequences >= 1000 residues

### Parameters:
```bash
fasta_filter.py input_fasta output_fasta min_seq_length [-l LOGLEVEL]
```

- `input_fasta`: Path to input FASTA file
- `output_fasta`: Path to output FASTA file
- `min_seq_length`: Integer minimum residue length
- `-l` or `--loglevel`: Optional logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

### Example:
```bash
docker run --rm -u $(id -u):$(id -g) -v $PWD:/data \
kitkat110/bio-container:1.0 \
fasta_filter.py \
/data/immune_proteins.fasta \
/data/output_files/long_only.fasta \
1000
```

`fastq_filter.py`: Filters FASTQ reads by average Phred quality (>= 30) and writes results to a new FASTQ file

### Parameters:
```bash
fastq_filter.py input_fastq output_fastq phred_threshold [-l LOGLEVEL]
```

- `input_fastq`: Path to input FASTQ file
- `output_fastq`: Path to output FASTQ file
- `phred_threshold`: Integer minimum phred score
- `-l` or `--loglevel`: Optional logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

### Example:
```bash
docker run --rm -u $(id -u):$(id -g) -v $PWD:/data \
kitkat110/bio-container:1.0 \
fastq_filter.py \
/data/sample1_rawReads.fastq \
/data/output_files/sample1_cleanReads.fastq \
30
```

`mmcif_summary.py`: Parses an mmCIF file, computes total number of residues, including standard and hetero residues, and writes the summary as a dictionary to a JSON file

### Parameters:
```bash
mmcif_summary.py input_cif output_json structure_id [-l LOGLEVEL]
```

- `input_cif`: Path to input mmCIF file
- `output_json`: Path to output JSON file
- `structure_id`: Structure ID to assign to parsed structure
- `-l` or `--loglevel`: Optional logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

### Example:
```bash
docker run --rm -u $(id -u):$(id -g) -v $PWD:/data \
kitkat110/bio-container:1.0 \
mmcif_summary.py \
/data/4HHB.cif \
/data/output_files/4HHB_summary.json
```

## Output Files
All output files are written to the `output_files/` directory because it's inside the mounted `$PWD`:
- `immune_proteins_stats.txt`: FASTA statistics summary

- `long_only.fasta`: Filtered FASTA sequences >= 1000 residues

- `sample1_cleanReads.fastq`: Filtered FASTQ reads where Phred score >= 30

- `4HHB_summary.json`: JSON file containing a dictionary of hemoglobin chains and residue counts