from Common.io_utils import ReadInput, WriteOutput
from Common.bio_utils import NormalizeInput, IsStrongValidDNA
from Problems.DNA.methods import *


if __name__ == "__main__":
    input_text = NormalizeInput(ReadInput())
    if IsStrongValidDNA(input_text):
        # choose method here
        solution = IntuitiveCounter(input_text)
    else:
        solution = None
    output_text = WriteOutput(solution)

    # for debug purposes
    print(output_text)