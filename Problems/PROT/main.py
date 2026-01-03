from Common.io_utils import ReadInput, WriteOutput
from Common.bio_utils import NormalizeInput, IsStrongValidRNA
from Problems.PROT.methods import *


if __name__ == "__main__":
    input_text = NormalizeInput(ReadInput())
    if IsStrongValidRNA(input_text):
        # choose method here
        solution = GetProteinFromRna(input_text)
    else:
        solution = None
    output_text = WriteOutput(solution)

    # for debug purposes
    print(output_text)                          