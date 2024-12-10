import pytest
from seq_analysis import SequenceAnalyzer

class TestSequenceAnalyzer:
    def test_sequence_validation(self, sample_sequences):
        """Test sequence validation"""
        SequenceAnalyzer(sample_sequences['basic'])  # Should not raise
        SequenceAnalyzer('atcg')  # Should handle lowercase
        
        with pytest.raises(ValueError):
            SequenceAnalyzer('ATXG')

    def test_gc_content(self, analyzer, gc_rich_analyzer, at_rich_analyzer):
        """Test GC content calculation"""
        assert analyzer.gc_content() == 50.0
        assert gc_rich_analyzer.gc_content() == 100.0
        assert at_rich_analyzer.gc_content() == 0.0
        
        empty_seq = SequenceAnalyzer('')
        assert empty_seq.gc_content() == 0.0

    def test_count_kmers(self, analyzer):
        """Test k-mer counting"""
        # Test k=2
        expected_2mers = {
            'AT': 1, 'TC': 1, 'CG': 2, 
            'GC': 1, 'GT': 1, 'TA': 1
        }
        assert analyzer.count_kmers(2) == expected_2mers
        
        # Test invalid k values
        with pytest.raises(ValueError):
            analyzer.count_kmers(0)
        with pytest.raises(ValueError):
            analyzer.count_kmers(-1)
        with pytest.raises(ValueError):
            analyzer.count_kmers(9)

    def test_find_patterns(self, pattern_analyzer):
        """Test pattern finding"""
        assert pattern_analyzer.find_patterns("ATCG") == [0, 4, 8]
        assert pattern_analyzer.find_patterns("CG") == [2, 6, 10]
        assert pattern_analyzer.find_patterns("XXX") == []
        # Test case insensitivity
        assert pattern_analyzer.find_patterns("atcg") == [0, 4, 8]

    def test_transcribe(self, analyzer):
        """Test DNA to RNA transcription"""
        assert analyzer.transcribe() == "AUCGCGUA"
        
        seq = SequenceAnalyzer("TTTT")
        assert seq.transcribe() == "UUUU"
        
        empty_seq = SequenceAnalyzer("")
        assert empty_seq.transcribe() == ""

    def test_reverse_complement(self, analyzer):
        """Test reverse complement generation"""
        assert analyzer.reverse_complement() == "TACGCGAT"
        
        seq = SequenceAnalyzer("AATT")
        assert seq.reverse_complement() == "AATT"
        
        empty_seq = SequenceAnalyzer("")
        assert empty_seq.reverse_complement() == ""

    def test_invalid_sequences(self, invalid_sequences):
        """Test invalid sequence handling"""
        for seq in invalid_sequences:
            with pytest.raises(ValueError):
                SequenceAnalyzer(seq)