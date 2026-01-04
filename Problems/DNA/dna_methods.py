from collections import Counter


def BuiltInCounter(dna: str) -> str:
    counts = Counter(dna)
    return f"{counts.get('A', 0)} {counts.get('C', 0)} {counts.get('G', 0)} {counts.get('T', 0)}"

def BuiltInCounter_2(dna: str) -> str:
    counts = Counter(dna)
    results = [counts.get(base, 0) for base in "ACGT"]
    return " ".join(map(str, results))

def IntuitiveCounter(dna: str) -> str:
    counts = {'A': 0, 'C': 0, 'G': 0,'T': 0}
    for base in dna:
        counts[base] += 1
    return f"{counts['A']} {counts['C']} {counts['G']} {counts['T']}"