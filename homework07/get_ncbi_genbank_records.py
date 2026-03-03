#!/usr/bin/env python3

import argparse
import json
import logging
import socket
import sys

from Bio import Entrez, SeqIO
import redis


# -------------------------
# Argument Parsing
# -------------------------
parser = argparse.ArgumentParser(
    description="Retrieve NCBI GenBank records and store in Redis."
)

parser.add_argument(
    "--output",
    type=str,
    default="genbank_records.txt",
    help="Path to output text file"
)

parser.add_argument(
    "--search",
    type=str,
    default="Arabidopsis thaliana AND AT5G10140",
    help="Search term for NCBI protein database"
)

parser.add_argument(
    "-l", "--loglevel",
    type=str,
    default="WARNING",
    help="Set log level to DEBUG, INFO, WARNING, ERROR, or CRITICAL"
)

args = parser.parse_args()


# -------------------------
# Logging setup
# -------------------------
format_str = (
    f'[%(asctime)s {socket.gethostname()}] '
    '%(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
)
logging.basicConfig(level=args.loglevel.upper(), format=format_str)


# -------------------------
# Functions
# -------------------------
def retrieve_gb_records(search_term: str, retmax: int = 30) -> list:
    """
    Search NCBI protein database and return matching records.

    Args:
        search_term: Search query for NCBI.
        retmax: Maximum number of records to retrieve.

    Returns:
        rec_list: List of the matching genbank records.
    """

    Entrez.email = "A.N.Other@example.com"

    try:
        logging.info(f"Searching NCBI database for {search_term}")

        with Entrez.esearch(db = "protein", term = search_term, retmax = retmax) as h:
            results = Entrez.read(h)

        GI_nums = results["IdList"]
        if not GI_nums:
            logging.warning("No records found.")
            return []

        rec_list = []
        for r in GI_nums:
            with Entrez.efetch(db = "protein", id = r, rettype = "gb", retmode = "text") as h:
                record = list(SeqIO.parse(h, "gb"))
                rec_list.extend(record)
        
        logging.info(f"Fetched {len(rec_list)} records.")
        return rec_list

    except Exception as e:
        logging.error(f"Error fetching records: {e}")
        return []


def store_and_write_records(records: list, output_file: str) -> None:
    """
    Store matched records in a Redis database and writes them to a txt file.

    Args:
        records: List of dictionaries of the matched records.
        output_file: Name of the output file.

    Returns:
        None: This function does not return a value; it writes output to disk.
    """

    try:
        rd = redis.Redis(host = "127.0.0.1", port = 6379, db = 0)
        logging.info("Connected to Redis.")

        for r in records:
            data = {
                "id": r.id,
                "name": r.name,
                "description": r.description,
                "sequence": str(r.seq)
            }
            rd.set(r.id, json.dumps(data))

        logging.info("Stored records in Redis.")

        keys = rd.keys()
        with open(output_file, "w") as outfile:
            for k in keys:
                k_str = k.decode("utf-8")
                value = rd.get(k_str)

                data = json.loads(value)
                outfile.write(f"ID: {data['id']}\n")
                outfile.write(f"Name: {data['name']}\n")
                outfile.write(f"Description: {data['description']}\n")
                outfile.write(f"Sequence: {data['sequence']}\n\n")

        logging.info(f"Successfully wrote records to {output_file}")

    except Exception as e:
        logging.error(f"Error storing or writing records: {e}")


# -------------------------
# Main
# -------------------------
def main():
    """
    Calls write_fasta_filter()

    Args:
        None: This function does not use any arguments

    Returns:
        None: This function does not return a value
    """

    records = retrieve_gb_records(args.search)
    if not records:
        logging.error("No records retrieved. Exiting.")
        sys.exit(1)

    store_and_write_records(records, args.output)
    logging.info("Retrieving GenBank records workflow complete.")

if __name__ == "__main__":
    main()

    
