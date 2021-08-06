import collections


def is_isogram(string):
    c = collections.Counter(string.lower().replace("-", "").replace(" ", ""))
    return sum(c.values()) == len(c.values())
