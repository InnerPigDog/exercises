import collections


def is_isogram(string):
    c = collections.Counter(string.lower())
    # Ignore hyphens and spaces. Works if there is no hyphen or space.
    c['-'] = 1
    c[' '] = 1
    return sum(c.values()) == len(c.values())
