# BioSplit by Length

A lightweight, researcher-friendly command-line tool to split FASTA files by **sequence length** — useful for filtering proteins or genes above or below a specific threshold.

---

## 🧠 Features
- Automatically detects if the input file contains **amino acids** or **nucleotides**
- Splits sequences into two FASTA files based on **user-defined threshold**
- Preserves all headers and sequences (no data loss)
- Compatible with both **FASTA** and **multi-sequence files**

---

## 🚀 Usage

```bash
python3 bio_split_by_length.py -i input.fasta -t 300


Output:

input_<=_300.fasta → sequences ≤ 300 aa/nt

input_>_300.fasta → sequences > 300 aa/nt

Example

python3 bio_split_by_length.py -i proteins.fasta -t 300


Detected file type: PROTEIN sequences
✅ Splitting complete!
Total sequences processed: 994
≤ 300 protein sequences: 678 saved to proteins_<=_300.fasta
> 300 protein sequences: 316 saved to proteins_>_300.fasta


Author

Asim Mehmood
Helping researchers automate tedious bioinformatics preprocessing tasks.
