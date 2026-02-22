#!/usr/bin/env python3

from Bio import SeqIO
import argparse
import logging
import socket
import os

# -------------------------
# Argument Parsing
# -------------------------
parser = argparse.ArgumentParser(
    description = "Parse a FASTQ file and filter only sequences that meet the Phred score threshold."
)

parser.add_argument(
    "input_fastq",
    type=str,
    help="Path to input FASTQ file"
)

parser.add_argument(
    "output_fastq",
    type=str,
    help="Path to output txt summary file"
)

parser.add_argument(
    "phred_threshold",
    type=int,
    help="Minimum average Phred score to filter by"
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

logging.basicConfig(level=args.loglevel, format=format_str)


# -------------------------
# Functions
# -------------------------

def write_fastq_filter(input_file: str, output_file: str, phred_threshold: int) -> None:
    """
    Read input FASTQ, filters by average phred, and adds those filtered reads to a new FASTQ file

    Args:
        input_file: Name of the input FASTQ file
        output_file: Name of the output FASTQ file
        phred_threshold: Minimum average Phred score to filter by

    Returns: None: This function does not return a value; it writes output to disk
    """
    goodreads_count = 0
    read_count = 0

    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for record in SeqIO.parse(infile, 'fastq-sanger'):
                read_count += 1
        
                # Calculate average phred quality
                avg_phred = sum(record.letter_annotations['phred_quality']) / len(record.letter_annotations['phred_quality'])

                if avg_phred >= phred_threshold:
                    goodreads_count += 1
                    SeqIO.write(record, outfile, "fastq")
            
        logging.info(f"Total reads in original file: {read_count}")
        logging.info(f"Reads passing filter: {goodreads_count}")
    
    except FileNotFoundError:
        logging.error(f"Could not open input file {input_file}")
        return None

def main():
    """
    Calls write_fasta_filter()

    Args:
        None: This function does not use any arguments

    Returns:
        None: This function does not return a value
    """
    write_fastq_filter(args.input_fastq, args.output_fastq, args.phred_threshold)

    logging.info("FASTQ filter workflow complete")

if __name__ == '__main__':
    main()
