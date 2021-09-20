LETTERS_VALUES = {
    "AEIOULNRST": 1,
    "DG": 2,
    "BCMP": 3,
    "FHVWY": 4,
    "K": 5,
    "JX": 8,
    "QZ": 10

}


def score(word: str) -> int:
    return sum([LETTERS_VALUES[key] for letter in word.upper()
                for key in LETTERS_VALUES.keys() if letter in key])

# LETTER_VALUES = {
#     "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
#     "D": 2, "G": 2,
#     "B": 3, "C": 3, "M": 3, "P": 3,
#     "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
#     "K": 5,
#     "J": 8, "X": 8,
#     "Q": 10, "Z": 10
# }


# def score(word: str) -> int:
#     return sum([LETTER_VALUES[letter] for letter in word.upper()])
