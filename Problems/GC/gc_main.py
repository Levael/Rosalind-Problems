from Common.io_utils import ReadInput, WriteOutput
from Common.bio_utils import normalize_input, SequenceType, parse_fasta
from Problems.GC.gc_methods import get_record_with_highest_gc, get_printable_result


if __name__ == "__main__":
    raw_input_text = ReadInput()
    parsed_input = parse_fasta(raw_input_text)
    is_all_nucleic = all(
        rec.sequence_type in [SequenceType.DNA, SequenceType.RNA] 
        for rec in parsed_input
    )

    if is_all_nucleic:
        # choose method here
        pre_solution = get_record_with_highest_gc(parsed_input)
        solution = get_printable_result(pre_solution)
    else:
        solution = None
    output_text = WriteOutput(solution)

    # for debug purposes
    print(output_text)