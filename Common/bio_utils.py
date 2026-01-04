"""
BIO_UTILS.PY
...

Functions:
    - 
    - 
Classes:
    -
"""

# =============================================================================
# IMPORTS
# =============================================================================

from enum import Enum, auto

# =============================================================================
# CONSTANTS and ENUMS
# =============================================================================

RNA_CODONS_TO_AMINO_ACID_TABLE = {
    "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
    "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
    "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
    "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",

    "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
    "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
    "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
    "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",

    "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
    "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
    "UAA": ".", "CAA": "Q", "AAA": "K", "GAA": "E",
    "UAG": ".", "CAG": "Q", "AAG": "K", "GAG": "E",

    "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
    "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
    "UGA": ".", "CGA": "R", "AGA": "R", "GGA": "G",
    "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G",
}

MUTATIONS_TABLE = {
    "TRANSITION": {'A':'G', 'G':'A', 'C':'T', 'T':'C'},
    "TRANSVERSION": {'A':['C', 'T'], 'G':['C', 'T'], 'C':['A', 'G'], 'T':['A', 'G']}
}

class SequenceType(Enum):
    DNA = auto()
    RNA = auto()
    PROTEIN = auto()
    UNKNOWN = auto()

DNA_BASES = set("ACGNT")
RNA_BASES = set("ACGNU")
PROT_BASES = set("ACDEFGHIKLMNPQRSTVWYX")

# =============================================================================
# FUNCTIONS
# =============================================================================

def normalize_input(input_string: str) -> str:
    return "".join(input_string.upper().split())

def parse_fasta(raw_data: str) -> list:
    entries = list(filter(None, raw_data.split('>')))   # deletes (None, "", 0, [])
    results = []

    for entry in entries:
        clean_entry = entry.strip()
        if not clean_entry:
            continue
        lines = clean_entry.splitlines()        
        header = lines[0].strip()
        sequence = normalize_input("".join(lines[1:]))
        sequence_type = detect_sequence_type(sequence)
        results.append(FastaRecord(header, sequence, sequence_type))
        
    return results

def detect_sequence_type(sequence: str) -> SequenceType:
    if not sequence:
        return SequenceType.UNKNOWN
        
    chars = set(sequence.upper())
    
    if 'T' in chars and 'U' in chars:
        return SequenceType.UNKNOWN

    # Note: the order of checks matters here
    if chars.issubset(DNA_BASES):
        return SequenceType.DNA
    if chars.issubset(RNA_BASES):
        return SequenceType.RNA
    if chars.issubset(PROT_BASES):
        return SequenceType.PROTEIN
            
    return SequenceType.UNKNOWN

# =============================================================================
# CLASSES
# =============================================================================

class FastaRecord:
    def __init__(self, record_id: str, sequence: str, sequence_type: SequenceType):
        self.id = record_id
        self.sequence = sequence
        self.sequence_type = sequence_type

    def __eq__(self, other):
        if isinstance(other, FastaRecord):
            return (self.id == other.id and 
                    self.sequence == other.sequence and 
                    self.sequence_type == other.sequence_type)
        return False

    def __repr__(self):
        return f"FastaRecord(id={self.id!r}, type={self.sequence_type.name})"