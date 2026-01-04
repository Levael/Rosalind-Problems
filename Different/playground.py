from Common.io_utils import ReadInput, WriteOutput
from Common.bio_utils import normalize_input, is_valid_rna
from Common.bio_utils import MUTATIONS_TABLE
from Problems.PROT.methods import *

# Point mutation in DNA -> protein
if __name__ == "__main__":
    dna = "ATGGTGATTTGTGATGGCAGCGGACGTGCCTCGGACATCCTGTCCTTTGCGCACTAG"
    mutated_base_number = 39
    mutated_base_index = mutated_base_number - 1
    mutated_dna = dna[:mutated_base_index] + MUTATIONS_TABLE["TRANSITION"][dna[mutated_base_index]] + dna[mutated_base_index+1:]
    protein = GetProteinFromDna(dna)
    mutated_protein = GetProteinFromDna(mutated_dna)
    is_protein_changed = protein != mutated_protein

    print(dna)
    print(mutated_dna)

    print(protein)
    print(mutated_protein)
    print("Is protein changed: ", is_protein_changed)

    '''
    input_text = NormalizeInput(dna)
    if IsStrongValidRNA(input_text):
        # choose method here
        solution = GetProteinFromRna(input_text)
    else:
        solution = None
    output_text = WriteOutput(solution)

    # for debug purposes
    print(output_text)
    '''