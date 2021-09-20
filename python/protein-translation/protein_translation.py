CODON_TO_PROTEIN = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan"
}

STOP_CODONS = {"UAA", "UAG", "UGA"}


def proteins(strand: str) -> list[str]:
    protein_seq = []

    # Split RNA strand into 3 character sequences called codons, which correspond to specific proteins.
    for i in range(0, len(strand), 3):
        codon = strand[i:i + 3]
        if codon in STOP_CODONS:
            break
        protein_seq.append(CODON_TO_PROTEIN[codon])
    return protein_seq
