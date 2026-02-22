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
    description = "Parse a FASTA file and calculate basic statistics."
)

parser.add_argument(
    "input_fasta",
    type=str,
    help="Path to input FASTA file"
)

parser.add_argument(
    "output_txt",
    type=str,
    help="Path to output txt summary file"
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
def build_seq(input_file: str) -> list:
    """
    Given an input FASTA file, builds list of sequence dictionaries 

    Args:
        input_file: Name of the input FASTA file
    
    Returns:
        sequences: A list of sequence dictionaries

    """
    logging.info(f'Starting parse of {input_file}')
    sequences = []

    try:
        with open(input_file, 'r') as infile:
            for header, sequence in SimpleFastaParser(infile):
                parts = header.split("|")
                entry = {
                        "accession": parts[1], 
                        "sequence": sequence,
                        "length": len(sequence)
                }
                sequences.append(entry)

        logging.info(f"Successfully loaded {input_file}")
        return sequences
    
    except FileNotFoundError:
        logging.error(f"Could not open input file {input_file}")
        return None

def count_res(sequences: list) -> int:
    """
    Counts up the total number of residues 

    Args:
        sequences: A list of sequence dictionaries

    Returns:
        res_count = Count of total number of residues
    """
    res_count = 0

    for seq in sequences:
        res_count += seq['length']

    return res_count

def calc_lengths(sequences: list) -> tuple:
    """
    Finds the shortest and longest sequence 

    Args:
        sequences: A list of sequence dictionaries
    
    Returns:
        longest_seq: The longest sequence in the list
        shortest_seq: The shortest sequence in the list
    """
    longest_length = 0
    shortest_length = 1000000
    longest_seq = None
    shortest_seq = None

    for seq in sequences:
        if seq['length'] > longest_length:
            longest_length = seq['length']
            longest_seq = seq
        elif seq['length'] < shortest_length:
            shortest_length = seq['length']
            shortest_seq = seq
    return longest_seq, shortest_seq

def write_summary_to_txt(output_file: str, 
                         sequences: list, 
                         total_res: int, 
                         longest_seq: dict, 
                         shortest_seq: dict) -> None:
    """
    Writes summary statistics to a txt file

    Args:
        output_file: Name of the output txt file
        sequences: A list of sequence dictionaries
        total_res: Count of the total number of residues
        longest_seq: The longest sequence in the list
        shortest_seq: The shortest sequence in the list

    Returns:
        None: This function does not return a value; it writes output to disk
    """
    try:
        logging.info(f"Writing summary to {output_file}")

        with open(output_file, "w") as outfile:
            outfile.write(f"Num Sequences: {len(sequences)}\n")
            outfile.write(f"Total Residues: {total_res}\n")
            outfile.write(
                f"Longest Accession: {longest_seq['accession']} "
                f"({longest_seq['length']} residues)\n"
            )
            outfile.write(
                f"Shortest Accession: {shortest_seq['accession']} "
                f"({shortest_seq['length']} residues)\n"
            )

        logging.info(f"Successfully wrote summary to {output_file}")

    except Exception as e:
        logging.error(f"Failed to write txt file: {e}")

def main():
    """
    Calls build_seq(), count_res(), calc_lengths(), and write_summary_to_txt()

    Args:
        None: This function does not use any arguments

    Returns:
        None: This function does not return a value
    """
    sequences = build_seq(args.input_fasta)

    if sequences is None:
        return

    total_res = count_res(sequences)
    longest_seq, shortest_seq = calc_lengths(sequences)

    write_summary_to_txt(
        args.output_txt,
        sequences,
        total_res,
        longest_seq,
        shortest_seq
    )

    logging.info("FASTA summary workflow complete")

if __name__ == '__main__':
    main()