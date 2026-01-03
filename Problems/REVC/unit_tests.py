import pytest
from Problems.REVC.methods import *

# Tuple format: (input_data, expected_result)
COMPLIMENTATION_TEST_CASES = [
    ("A", "T"),
    ("T", "A"),
    ("C", "G"),
    ("G", "C"),
    ("AC", "GT"),
    ("AAAACCCGGT", "ACCGGGTTTT")
]

@pytest.mark.parametrize("dna, expected", COMPLIMENTATION_TEST_CASES)
def TestComplimentationMethods(dna, expected):
    assert GetComplimentDnaStrand(dna) == expected