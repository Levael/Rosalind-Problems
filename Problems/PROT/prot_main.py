from Common.io_utils import ReadInput, WriteOutput
from Common.bio_utils import normalize_input, detect_sequence_type, SequenceType
from Problems.PROT.prot_methods import *


if __name__ == "__main__":
    input_text = normalize_input(ReadInput())
    if detect_sequence_type(input_text) == SequenceType.RNA:
        # choose method here
        solution = GetProteinFromRna(input_text)
    else:
        solution = None
    output_text = WriteOutput(solution)

    # for debug purposes
    print(output_text)