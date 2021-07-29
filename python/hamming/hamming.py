def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Arguments must be of the same length.")
    return len(strand_a) - sum([strand_a[i] == strand_b[i] for i in range(len(strand_a))])
