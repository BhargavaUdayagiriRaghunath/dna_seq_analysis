import os
import sys
import pytest
from typing import Generator

# Adding src dir to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from seq_analysis import SequenceAnalyzer

@pytest.fixture
def sample_sequences() -> dict:
    """Some common test seq"""
    return {
        'basic': 'ATCGCGTA',
        'gc_rich': 'GCGCGCGC',
        'at_rich': 'ATATATAT',
        'empty': '',
        'with_pattern': 'ATCGATCGATCG'
    }

@pytest.fixture
def analyzer(sample_sequences) -> SequenceAnalyzer:
    """Basic seq analyzer"""
    return SequenceAnalyzer(sample_sequences['basic'])

@pytest.fixture
def gc_rich_analyzer(sample_sequences) -> SequenceAnalyzer:
    """GC-rich seq analyzer"""
    return SequenceAnalyzer(sample_sequences['gc_rich'])

@pytest.fixture
def at_rich_analyzer(sample_sequences) -> SequenceAnalyzer:
    """AT-rich seq-analyzer"""
    return SequenceAnalyzer(sample_sequences['at_rich'])

@pytest.fixture
def pattern_analyzer(sample_sequences) -> SequenceAnalyzer:
    """Sequence analyzer with repeating pattern"""
    return SequenceAnalyzer(sample_sequences['with_pattern'])

@pytest.fixture
def invalid_sequences() -> list:
    """Invalid seq examples"""
    return [
        'ATXG',    # Invalid character
        'AT1G',    # Number
        'AT-G',    # Special character
        'ATNG',    # Invalid base
    ]