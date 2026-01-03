def GetComplimentDnaStrand(dna: str) -> str:
    # Note that return value is 5` to 3`
    table = str.maketrans("ATCG", "TAGC")
    return dna.translate(table)[::-1]