from Common.bio_utils import RnaCodonsToProteinTable


def GetProteinFromRna(rna: str) -> str:
    start_pos = rna.find("AUG")
    if start_pos == -1:
        return ""
    
    protein_list = []
    for i in range(start_pos, len(rna) - 2, 3):
        codon = rna[i:i+3]
        amino = RnaCodonsToProteinTable.get(codon, "")
        
        if amino == ".":
            break
        if amino:
            protein_list.append(amino)
            
    return "".join(protein_list)

def GetRawPreProteinSequences(rna: str) -> list:
    pre_protein_1 = [RnaCodonsToProteinTable.get(rna[i:i+3], "") for i in range(0, len(rna), 3)]
    pre_protein_2 = [RnaCodonsToProteinTable.get(rna[i:i+3], "") for i in range(1, len(rna), 3)]
    pre_protein_3 = [RnaCodonsToProteinTable.get(rna[i:i+3], "") for i in range(2, len(rna), 3)]
    return [pre_protein_1, pre_protein_2, pre_protein_3]