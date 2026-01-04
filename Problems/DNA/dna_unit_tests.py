import pytest
from Problems.DNA.dna_methods import *

# Tuple format: (input_data, expected_result)
CALCULATION_TEST_CASES = [
    ("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC", "20 12 17 21"),
    ("A", "1 0 0 0"),
    ("C", "0 1 0 0"),
    ("G", "0 0 1 0"),
    ("T", "0 0 0 1"),
    ("", "0 0 0 0")
]

@pytest.mark.parametrize("dna, expected", CALCULATION_TEST_CASES)
def TestCalculationMethods(dna, expected):
    assert BuiltInCounter(dna) == expected
    assert BuiltInCounter_2(dna) == expected
    assert IntuitiveCounter(dna) == expected