import pandas as pd
from Bio import SeqIO
import sys
import os

# Set paths based on expected SLURM working directory
WORKDIR = os.getcwd()
TARGET_LIST_FILE = os.path.join(WORKDIR, 'target_transcripts.txt')
BRAKER_AA_FILE = "/users/PDNU0014/usrname2/chacei_braker_rnaseq_V12/braker.aa"
OUTPUT_FILE = os.path.join(WORKDIR, 'query.faa')

# 1. Load Target Transcript IDs
target_ids = set()
try:
    with open(TARGET_LIST_FILE, 'r') as f:
        target_ids = {line.strip() for line in f if line.strip()}
except Exception as e:
    print(f"FATAL ERROR: Could not read target list: {e}")
    sys.exit(1)

# 2. Extract Sequences using Bio.SeqIO
extracted_sequences = []
try:
    print(f"Starting extraction of {len(target_ids)} sequences...")
    
    for record in SeqIO.parse(BRAKER_AA_FILE, "fasta"):
        transcript_id = record.id.split()[0]
        
        if transcript_id in target_ids:
            extracted_sequences.append(record)
            target_ids.remove(transcript_id)

    # 3. Write the extracted sequences to the final output file
    SeqIO.write(extracted_sequences, OUTPUT_FILE, "fasta")

    print(f"Extraction successful. {len(extracted_sequences)} sequences written to {OUTPUT_FILE}")
    if target_ids:
        print(f"WARNING: {len(target_ids)} sequences were not found in the braker.aa file.")
        
except Exception as e:
    print(f"FATAL EXTRACTION ERROR: {e}")
    sys.exit(1)