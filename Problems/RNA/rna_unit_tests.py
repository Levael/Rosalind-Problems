import pytest
from Problems.RNA.rna_methods import *

# Tuple format: (input_data, expected_result)
TRANSCRIPTION_TEST_CASES = [
    ("A", "A"),
    ("C", "C"),
    ("G", "G"),
    ("T", "U")
]

@pytest.mark.parametrize("dna, expected", TRANSCRIPTION_TEST_CASES)
def TestTranscriptionMethods(dna, expected):
    assert CodingDnaStrandToMessengerRnaTranscriber(dna) == expected