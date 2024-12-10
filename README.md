# **DNA Sequence Analysis Tool**
### A Python command-line tool for analyzing DNA sequences. This tool provides various functionalities for DNA sequence manipulation and analysis, including GC content calculation, k-mer counting, pattern finding, transcription, and reverse complement generation.

### Features
- GC Content Calculation: Compute the percentage of G and C bases in a DNA sequence
- K-mer Counting: Count occurrences of all possible k-length subsequences
- Pattern Finding: Locate specific patterns within the sequence
- DNA to RNA Transcription: Convert DNA sequences to RNA
- Reverse Complement: Generate the reverse complement of a DNA sequence

## Installation

`git clone https://github.com/BhargavaUdayagiriRaghunath/dna_seq_analysis`

`cd dna_seq_analysis`

`chmod +x src/seq_analysis.py`

## Usage Examples
### Calculate GC Content

`./src/seq_analysis.py ATCGCGTA --gc`
#### Output: GC Content: 50.00%

### Count K-mers

`./src/seq_analysis.py ATCGCGTA --kmer 2`
#### Output:
 - K-mer Counts:
    - AT: 1
    - CG: 2  
    - GC: 1
    - GT: 1
    - TA: 1

### Find Pattern Occurrences

`./src/seq_analysis.py ATCGCGTA --pattern CG`
#### Output: Pattern 'CG' found at positions: [2, 4]

### Transcribe DNA to RNA

`./src/seq_analysis.py ATCGCGTA --transcribe`
#### Output: RNA Sequence: AUCGCGUA

### Generate Reverse Complement

`./src/seq_analysis.py ATCGCGTA --reverse-complement`
#### Output: Reverse Complement: TACGCGAT

### Requirements
- Python 3.6 or higher
- NumPy
- argparse (included in Python standard library)
- Error Handling
- The tool includes validation for:
- Invalid DNA sequences (only A, T, C, G allowed)
- Invalid k-mer lengths
- Invalid input patterns