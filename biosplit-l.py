#!/usr/bin/env python3
"""
BioSplit by Length
------------------
A universal bioinformatics file splitter for FASTA/FASTQ files based on sequence length.

Features:
- Automatically detects whether sequences are nucleotide or amino acid.
- Splits file into two sets based on user-defined length threshold.
- Ensures no data loss and preserves all headers.
- Works on both protein and nucleotide FASTA files.

Author: Asim Mehmood
License: GPL v3
"""

import sys
import os
from itertools import groupby

def detect_type(seq):
    dna_letters = set("ATGCUatgcu")
    aa_letters = set("ABCDEFGHIKLMNPQRSTVWXYZabcdefghiklmnpqrstvwyz")
    seq_letters = set(seq)
    if seq_letters <= dna_letters:
        return "nucleotide"
    elif seq_letters <= aa_letters:
        return "protein"
    else:
        return "unknown"

def read_fasta(filepath):
    with open(filepath) as f:
        fasta_iter = (x[1] for x in groupby(f, lambda line: line.startswith(">")))
        for header in fasta_iter:
            header = next(header).strip()[1:]
            seq = "".join(s.strip() for s in next(fasta_iter))
            yield header, seq

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 bio_split_by_length.py -i <input_fasta> -t <threshold_length>")
        sys.exit(1)

    try:
        input_file = sys.argv[sys.argv.index("-i") + 1]
        threshold = int(sys.argv[sys.argv.index("-t") + 1])
    except (ValueError, IndexError):
        print("Error: Missing or invalid arguments.")
        sys.exit(1)

    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    # Read sequences and detect type
    sequences = list(read_fasta(input_file))
    if not sequences:
        print("No sequences found in file.")
        sys.exit(1)

    # Detect molecule type from first sequence
    seq_type = detect_type(sequences[0][1])
    print(f"Detected file type: {seq_type.upper()} sequences")

    short_out = os.path.splitext(input_file)[0] + f"_<=_{threshold}.fasta"
    long_out = os.path.splitext(input_file)[0] + f"_>_{threshold}.fasta"

    short_count = long_count = 0

    with open(short_out, "w") as short_f, open(long_out, "w") as long_f:
        for header, seq in sequences:
            if len(seq) <= threshold:
                short_f.write(f">{header}\n{seq}\n")
                short_count += 1
            else:
                long_f.write(f">{header}\n{seq}\n")
                long_count += 1

    print("\n✅ Splitting complete!")
    print(f"Total sequences processed: {len(sequences)}")
    print(f"≤ {threshold} {seq_type} sequences: {short_count} saved to {short_out}")
    print(f"> {threshold} {seq_type} sequences: {long_count} saved to {long_out}\n")

if __name__ == "__main__":
    main()

