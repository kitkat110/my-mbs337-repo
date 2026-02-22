#!/usr/bin/env python3

from Bio.SeqIO.FastaIO import SimpleFastaParser
import argparse
import logging
import socket
import os

# -------------------------
# Argument Parsing
# -------------------------
parser = argparse.ArgumentParser(
    description = "Parse a FASTA file and filter only sequences that are a certain length."
)

parser.add_argument(
    "input_fasta",
    type=str,
    help="Path to input FASTA file"
)

parser.add_argument(
    "output_fasta",
    type=str,
    help="Path to output txt summary file"
)

parser.add_argument(
    "min_seq_length",
    type=int,
    help="Minimum number of residues to filter by"
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
def write_fasta_filter(input_file: str, output_file: str, min_length: int) -> None:
    """
    Read input FASTA and output matches to a new output FASTA

    Args:
        input_file: Name of the input FASTA file
        output_file: Name of the output FASTA file
        min_length: Minimum number of residues to filter sequences by 

    Returns: None: This function does not return a value; it writes output to disk
    """
    try:
        with open(input_file, 'r') as infile, open (output_file, 'w') as outfile:
            for header, sequence in SimpleFastaParser(infile):
                if len(sequence) >= min_length:
                    outfile.write(f">{header}\n")
                    outfile.write(f"{sequence}\n")
        
        logging.info(f"Successfully wrote filtered sequences to {output_file}")
    
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
    write_fasta_filter(args.input_fasta, args.output_fasta, args.min_seq_length)

    logging.info("FASTA filter workflow complete")

if __name__ == '__main__':
    main()



        