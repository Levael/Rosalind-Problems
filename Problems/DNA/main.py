import sys
import os

# Adding project root to sys.path so we can import from 'Common'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Common.housekeeping_codes import ReadInput, WriteOutput
from methods import BuiltInCounter, BuiltInCounter_2, IntuitiveCounter, IsValidDNA, NormalizeInput


if __name__ == "__main__":
    input_text = ReadInput()
    input_text = NormalizeInput(input_text)
    if IsValidDNA(input_text):
        solution = IntuitiveCounter(input_text) # choose method here
    else:
        solution = None
    output_text = WriteOutput(solution)
    print(output_text)                          # for debug purposes