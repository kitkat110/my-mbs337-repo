import json
from Bio.PDB.MMCIFParser import MMCIFParser
import argparse
import logging
import socket


# -------------------------
# Constants (configuration)
# -------------------------
CIF_FILE = "4HHB.cif"
STRUCTURE_ID = "hemoglobin"
JSON_FILE = "4HHB_summary.json"


# -------------------------
# Logging setup
# -------------------------
log_parser = argparse.ArgumentParser()
log_parser.add_argument(
    '-l', '--loglevel',
    type=str,
    required=False,
    default='WARNING',
    help='set log level to DEBUG, INFO, WARNING, ERROR, or CRITICAL'
)
args = log_parser.parse_args()

format_str = (
    f'[%(asctime)s {socket.gethostname()}] '
    '%(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
)
logging.basicConfig(level=args.loglevel, format=format_str)


# -------------------------
# Functions
# -------------------------
def parse_cif(input_file: str, structure_id: str) -> object:
    """
    Create parser, open mmCIF file, and create a BioPython Structure object

    Args:
        input_file: Name of the input mmCIF file
        structure_id: the id that will be used to name the structure

    Returns:
        structure: A single mmCIF protein structure produced by BioPython's mmCIF parser
    """
    parser = MMCIFParser()
    
    with open(input_file, 'r') as infile:
        try:
            structure = parser.get_structure(structure_id, infile)
            logging.info(f'Successfully loaded {input_file}')
            
            return structure
        except FileNotFoundError:
            logging.error(f'Could not open input file {input_file}')
        
        return None

def count_res_chains(structure: object) -> dict:
    """
    Given a single structure object, computes the total number of residues, number of hetero residues,
    and number of standard residues for each chain in each model

    Args:
        structure: A single mmCIF protein structure produced by BioPython's mmCIF parser

    Returns:
        chain_res_counts: A dictionary of the chains' residue counts
    """
    logging.debug(f'Counting chain residues of {structure}')

    chain_res_counts = {"chains": []}

    for model in structure:
        for chain in model:
            total_residues = 0
            hetero_res_count = 0
            standard_residues = 0

            for residue in chain: 
                total_residues += 1

                hetfield, resseq, icode = residue.get_id()
                # Standard amino acids
                if hetfield == ' ':
                    standard_residues += 1
                else:
                    hetero_res_count += 1

            chain_res_counts["chains"].append({
                "chain_id": chain.get_id(),
                "total_residues": total_residues,
                "standard_residues": standard_residues,
                "hetero_residue_count": hetero_res_count
            })

        return chain_res_counts
            
def write_summary_to_json(count_summary: dict, output_file: str) -> None:
    """
    Given a dictionary of residue counts of each chain, write it to a JSON file

    Args:
        count_summary: A dictionary of the residue counts of a structure's chains
        output_file: Name of the output JSON file

    Returns:
        None: This function does not return a value; it writes output to disk
    """
    with open(output_file, 'w') as outfile:
        json.dump(count_summary, outfile, indent=2)

        logging.info(f'Successfully wrote summary to {output_file}')

def main():
    """
    Calls parse_cif(), count_res_chains(), and write_summary_to_json()

    Args:
        None: This function does not use any arguments

    Returns:
        None: This function does not return a value
    """
    structure = parse_cif(CIF_FILE, STRUCTURE_ID)
    summary = count_res_chains(structure)
    write_summary_to_json(summary, JSON_FILE)

    logging.info(f'MMCIF summary workflow complete')

if __name__ == '__main__':
    main()