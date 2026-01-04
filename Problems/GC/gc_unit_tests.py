import pytest
from Common.bio_utils import SequenceType, FastaRecord
from Problems.GC.gc_methods import get_gc_content, get_record_with_highest_gc, get_printable_result

# Tuple format: (input_data, expected_result)
COUNTING_TEST_CASES = [
    ("AATT", 0.0),
    ("CCGG", 100.0),
    ("ATGC", 50.0),
    ("AUGC", 50.0),
]

FINDING_TEST_CASES = [
    ([
        FastaRecord("Rosalind_1", "AATT", SequenceType.DNA),
        FastaRecord("Rosalind_2", "CCGG", SequenceType.DNA),
        FastaRecord("Rosalind_3", "ATGC", SequenceType.DNA),
        FastaRecord("Rosalind_4", "AUGC", SequenceType.RNA),
    ], FastaRecord("Rosalind_2", "CCGG", SequenceType.DNA))
]

PRINTING_TEST_CASES = [
    (FastaRecord("Rosalind_2", "CCGG", SequenceType.DNA), "Rosalind_2\n100.000000")
]

@pytest.mark.parametrize("sequence, expected", COUNTING_TEST_CASES)
def TestCountingMethods(sequence, expected):
    assert get_gc_content(sequence) == expected

@pytest.mark.parametrize("sequence, expected", FINDING_TEST_CASES)
def TestFindingMethods(sequence, expected):
    assert get_record_with_highest_gc(sequence) == expected

@pytest.mark.parametrize("record, expected", PRINTING_TEST_CASES)
def TestPrintingMethods(record, expected):
    assert get_printable_result(record) == expected