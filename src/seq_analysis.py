#!/usr/bin/env python3

import argparse
import sys
from collections import defaultdict
import numpy as np
from typing import Dict, List

class SequenceAnalyzer:
    def __init__(self, sequence: str):
        self.sequence = sequence.upper()
        self.validate_sequence()
    
    def validate_sequence(self) -> None:
        """Validate DNA sequence"""
        if not all(base in 'ATCG' for base in self.sequence):
            raise ValueError("Invalid sequence. Only A, T, C, G allowed.")
    
    def gc_content(self) -> float:
        """Calculate GC content"""
        gc_count = self.sequence.count('G') + self.sequence.count('C')
        return (gc_count / len(self.sequence)) * 100 if self.sequence else 0
    
    def count_kmers(self, k: int) -> Dict[str, int]:
        """Count k-mers in sequence"""
        if k <= 0 or k > len(self.sequence):
            raise ValueError("Invalid k value")
        
        kmers = defaultdict(int)
        for i in range(len(self.sequence) - k + 1):
            kmer = self.sequence[i:i+k]
            kmers[kmer] += 1
        return dict(kmers)
    
    def find_patterns(self, pattern: str) -> List[int]:
        """Find all occurrences of a pattern"""
        pattern = pattern.upper()
        positions = []
        for i in range(len(self.sequence) - len(pattern) + 1):
            if self.sequence[i:i+len(pattern)] == pattern:
                positions.append(i)
        return positions
    
    def transcribe(self) -> str:
        """Transcribe DNA to RNA"""
        return self.sequence.replace('T', 'U')
    
    def reverse_complement(self) -> str:
        """Generate reverse complement"""
        complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        return ''.join(complement[base] for base in reversed(self.sequence))

def main():
    parser = argparse.ArgumentParser(description='DNA Sequence Analysis Tools')
    parser.add_argument('sequence', help='DNA sequence')
    parser.add_argument('--gc', action='store_true', help='Calculate GC content')
    parser.add_argument('--kmer', type=int, help='Count k-mers (specify k)')
    parser.add_argument('--pattern', help='Find pattern occurrences')
    parser.add_argument('--transcribe', action='store_true', help='Transcribe to RNA')
    parser.add_argument('--reverse-complement', action='store_true', 
                       help='Generate reverse complement')
    
    args = parser.parse_args()
    
    try:
        analyzer = SequenceAnalyzer(args.sequence)
        
        if args.gc:
            print(f"GC Content: {analyzer.gc_content():.2f}%")
        
        if args.kmer:
            kmers = analyzer.count_kmers(args.kmer)
            print("\nK-mer Counts:")
            for kmer, count in sorted(kmers.items()):
                print(f"{kmer}: {count}")
        
        if args.pattern:
            positions = analyzer.find_patterns(args.pattern)
            print(f"\nPattern '{args.pattern}' found at positions: {positions}")
        
        if args.transcribe:
            print(f"\nRNA Sequence: {analyzer.transcribe()}")
        
        if args.reverse_complement:
            print(f"\nReverse Complement: {analyzer.reverse_complement()}")
            
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()