# Homework 07

## About
This directory contains all the files for **Homework 07**, which focuses on databases and APIs. The goal of this homework is to run a Redis database inside a Docker container, retrieve GenBank protein records from the NCBI API using Biopython, store them in Redis, and write the stored record to a text file. 

## Directory Structure
```
my-mbs337-repo/
├── homework07
    ├── docker-compose.yml
    ├── get_ncbi_genbank_records.py
    ├── output_files
    │   └── genbank_records.txt
```

## Summary Workflow
1. Clone repository
2. Create redis-data/ repository
3. Start Redis container using Docker Compose
4. Install dependencies (biopython, redis)
5. Run get_ncbi_genbank_records.py
6. Find generated text file in output_files/
7. Stop Redis container

## Starting the Redis database
Inside the `homework07/` directory:
```bash
mkdir redis-data
```
This directory is mounted to `/data` inside the container.

### Start the container
From inside the `homework07/` directory:
```bash
docker compose up -d
```
- `-d`: Runs the container in detached mode

Verify the container is running:
```bash
docker ps
```
You should see a container named `redis` running on port 6379

### Stop the Container
When finished:
```bash
docker compose down
```

## Python Script
`get_ncbi_genbank_records.py`: Retrieves matching GenBank records from the NCBI protein database, stores them in Redis as JSON, and writes the records to a text file.

### Parameters:
```bash
get_ncbi_genbank_records.py --search --output [-l LOGLEVEL]
```

- `search`: Search term for NCBI protein database; default is 'Arabidopsis thaliana AND AT5G10140'

- `output`: Path to output text file; default is 'genbank_records.txt'

- `-l` or `--loglevel`: Optional logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

### Example:
```bash
python3 get_ncbi_genbank_records.py \
  --search "Arabidopsis thaliana AND AT5G10140" \
  --output genbank_records.txt \
  -l INFO
```

## Output Files
All output files are written to the `output_files/` directory:
- `genbank_records.txt`: Summary of matching NCBI protein records, including ID, name, description, and sequence
