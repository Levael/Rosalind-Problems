import pytest
from Common.bio_utils import normalize_input, SequenceType, FastaRecord, detect_sequence_type, parse_fasta

# Tuple format: (input_data, expected_result)
NORMALIZATION_TEST_CASES = [
    ("  ac gt  \n", "ACGT"),
    ("A C G T", "ACGT")
]

DETECTION_TEST_CASES = [
    ("ACGNT", SequenceType.DNA),
    ("ACGNU", SequenceType.RNA),
    ("ACGNTU", SequenceType.UNKNOWN),
    ("ACDEFGHIKLMNPQRSTVWYX", SequenceType.PROTEIN),
    ("123", SequenceType.UNKNOWN),
    ("", SequenceType.UNKNOWN)
]

# todo
FASTA_PARSING_TEST_CASES = [
    ("""\
    >Rosalind_1
    TCTACG
    >Rosalind_2
    UCUACG
    >Rosalind_3
    TCUACG
    >Rosalind_4
    MCTGCG
    >Rosalind_5
    MCTGCZ\
    """,
    [
        FastaRecord("Rosalind_1", "TCTACG", SequenceType.DNA),      # No U's, only T
        FastaRecord("Rosalind_2", "UCUACG", SequenceType.RNA),      # No T's, only U
        FastaRecord("Rosalind_3", "TCUACG", SequenceType.UNKNOWN),  # both T and U — not possible (normally)
        FastaRecord("Rosalind_4", "MCTGCG", SequenceType.PROTEIN),  # there is M — amino acid
        FastaRecord("Rosalind_5", "MCTGCZ", SequenceType.UNKNOWN)   # Z — does not exist
    ])
]

@pytest.mark.parametrize("sequence, expected", NORMALIZATION_TEST_CASES)
def TestNormalizationMethods(sequence, expected):
    assert normalize_input(sequence) == expected

@pytest.mark.parametrize("sequence, expected", DETECTION_TEST_CASES)
def TestDetectionMethods(sequence, expected):
    assert detect_sequence_type(sequence) == expected

@pytest.mark.parametrize("raw_fasta, expected", FASTA_PARSING_TEST_CASES)
def TestParsingMethods(raw_fasta, expected):
    assert parse_fasta(raw_fasta) == expected