import pytest
from methods import BuiltInCounter, BuiltInCounter_2, IntuitiveCounter, IsValidDNA, NormalizeInput

# Tuple format: (input_data, expected_result)
NORMALIZATION_TEST_CASES = [
    ("  acgt  \n", "ACGT"),
    ("A C G T", "A C G T")
]

VALIDATION_TEST_CASES = [
    ("", True),
    ("ACGT", True),
    ("acgt", False),
    ("123", False),
    ("ACGTN", False)
]

CALCULATION_TEST_CASES = [
    ("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC", "20 12 17 21"),
    ("A", "1 0 0 0"),
    ("C", "0 1 0 0"),
    ("G", "0 0 1 0"),
    ("T", "0 0 0 1"),
    ("", "0 0 0 0")
]

@pytest.mark.parametrize("dna, expected", NORMALIZATION_TEST_CASES)
def TestNormalizationMethods(dna, expected):
    assert NormalizeInput(dna) == expected

@pytest.mark.parametrize("dna, expected", VALIDATION_TEST_CASES)
def TestValidationMethods(dna, expected):
    assert IsValidDNA(dna) == expected

@pytest.mark.parametrize("dna, expected", CALCULATION_TEST_CASES)
def TestCalculationMethods(dna, expected):
    assert BuiltInCounter(dna) == expected
    assert BuiltInCounter_2(dna) == expected
    assert IntuitiveCounter(dna) == expected