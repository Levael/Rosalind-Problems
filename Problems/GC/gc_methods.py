from Common.bio_utils import FastaRecord


def get_gc_content(sequence: str) -> float:
    if not sequence:
        return 0.0
        
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100

def get_record_with_highest_gc(records: list[FastaRecord]) -> FastaRecord:
    if not records:
        return None

    return max(records, key=lambda rec: get_gc_content(rec.sequence))

def get_printable_result(record: FastaRecord) -> str:
    if not record:
        return None
        
    gc_content = get_gc_content(record.sequence)
    return f"{record.id}\n{gc_content:.6f}"