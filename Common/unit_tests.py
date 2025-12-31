import pytest
from Common.bio_utils import NormalizeInput, IsValidDNA

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

@pytest.mark.parametrize("dna, expected", NORMALIZATION_TEST_CASES)
def TestNormalizationMethods(dna, expected):
    assert NormalizeInput(dna) == expected

@pytest.mark.parametrize("dna, expected", VALIDATION_TEST_CASES)
def TestValidationMethods(dna, expected):
    assert IsValidDNA(dna) == expected