def square(number: int) -> int:
    if not 0 < number < 65:
        raise ValueError("ValueError exception thrown")
    return 2 ** (number - 1)


def total():
    return sum_squares(64)


def sum_squares(n: int) -> int:
    """
    .. math:: $\sum_{i=0}^{n-1} 2^{i}=2^{n}-1$
    :param n: int
    :return: int - Sum of 2**i from i=0 to i=n
    """
    return 2 ** n - 1
