def proteins(strand):
    protein_dict = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG":	"Serine",
        "UAU": "Tyrosine",
        "UAC":	"Tyrosine",
        "UGU": "Cysteine",
        "UGC":	"Cysteine",
        "UGG":	"Tryptophan"
    }
    stop_codons = ["UAA", "UAG", "UGA"]
    protein_seq = []

    # Split strand into 3 character sequences
    for codon in [strand[i:i+3] for i in range(0, len(strand), 3)]:
        if codon in stop_codons:
            break
        protein_seq.append(protein_dict[codon])
    return protein_seq
