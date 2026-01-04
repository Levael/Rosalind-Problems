import pytest
from Common.bio_utils import normalize_input
from Problems.PROT.prot_methods import *

# Tuple format: (input_data, expected_result)
TRANSLATION_TEST_CASES = [
    ("AUG GCC AUG UGA UCU", "MAM"),     # MAM.S
    ("AUG GCC AUG UGA UC", "MAM"),      # MAM.
    ("AUG GCC AUG UGA U", "MAM"),       # MAM.
    ("AUG GCC AUG AUA UCU", "MAMIS"),   # MAMIS
    ("AUG GCC AUG AUA UC", "MAMI"),     # MAMI
    ("UCU GCC AUG AUA UCU", "MIS"),     # SAMIS
    ("CU GCC AUG UGA UC", "M"),         # AM.
    ("U GCC AUG UGA U", "M"),           # AM.
    ("UGA AUG UGG UGG UGG", "MWWW"),    # .MWWW
    ("AUG AUG AUG AUG AUG", "MMMMM"),   # MMMMM
    ("AUG UGA AUG AUG AUG", "M"),       # M.MMM
    ("UCU GCC UCU AUA UCU", ""),        # SASIS
]

@pytest.mark.parametrize("dna, expected", TRANSLATION_TEST_CASES)
def TestTranslationMethods(dna, expected):
    assert GetProteinFromRna(normalize_input(dna)) == expected

'''
print(GetRawPreProteinSequences(NormalizeInput(TRANSLATION_TEST_CASES[0][0])))
print(GetRawPreProteinSequences(NormalizeInput(TRANSLATION_TEST_CASES[1][0])))
print(GetRawPreProteinSequences(NormalizeInput(TRANSLATION_TEST_CASES[2][0])))
print(GetRawPreProteinSequences(NormalizeInput(TRANSLATION_TEST_CASES[3][0])))
print(GetRawPreProteinSequences(NormalizeInput(TRANSLATION_TEST_CASES[4][0])))
print(GetRawPreProteinSequences(NormalizeInput(TRANSLATION_TEST_CASES[5][0])))
print(GetRawPreProteinSequences(NormalizeInput(TRANSLATION_TEST_CASES[6][0])))
print(GetRawPreProteinSequences(NormalizeInput(TRANSLATION_TEST_CASES[7][0])))
print(GetRawPreProteinSequences(NormalizeInput(TRANSLATION_TEST_CASES[8][0])))
print(GetRawPreProteinSequences(NormalizeInput(TRANSLATION_TEST_CASES[9][0])))
print(GetRawPreProteinSequences(NormalizeInput(TRANSLATION_TEST_CASES[10][0])))
'''