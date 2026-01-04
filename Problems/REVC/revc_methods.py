def GetComplimentDnaStrand(dna: str) -> str:
    # Note that return value is 5` to 3`
    table = str.maketrans("ATCGN", "TAGCN")
    return dna.translate(table)[::-1]