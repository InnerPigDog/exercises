import math


def score(x, y):
    r = math.sqrt(x**2+y**2)

    if r <= 1:
        return 10
    if r <= 5:
        return 5
    if r <= 10:
        return 1
    if r > 10:
        return 0
