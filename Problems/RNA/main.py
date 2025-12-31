from Common.io_utils import ReadInput, WriteOutput
from Common.bio_utils import NormalizeInput, IsValidDNA
from Problems.RNA.methods import *


if __name__ == "__main__":
    input_text = NormalizeInput(ReadInput())
    if IsValidDNA(input_text):
        # choose method here
        solution = CodingDnaStrandToMessengerRnaTranscriber(input_text)
    else:
        solution = None
    output_text = WriteOutput(solution)

    # for debug purposes
    print(output_text)                          