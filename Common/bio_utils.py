def NormalizeInput(input_string: str) -> str:
    return input_string.strip().upper()

def IsValidDNA(dna: str) -> bool:
    allowed = set("ACGT")
    return all(base in allowed for base in dna)