from collections import Counter


def count_words(sentence: str) -> Counter[str, int]:
    # Replace all characters with a space, which are not alphanumerical or an
    # apostrophe (to keep e.g. it's as one word).
    words = "".join(sentence[i] if sentence[i].isalnum() or sentence[i] == "'"
                    else " " for i in range(len(sentence)))
    return Counter([word.strip("'") for word in words.lower().split()])
