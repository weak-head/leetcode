def power(x: float, n: int) -> float:
    """
    https://en.wikipedia.org/wiki/Exponentiation_by_squaring
    """
    if n == 0:
        return 1

    if n == 1:
        return x

    if n == -1:
        return 1 / x

    a = power(x * x, n // 2)
    b = power(x, n % 2)
    return a * b


def power2(x, n):
    """
    Another variant
    """
    if n == 0 or x == 1:
        return 1

    if n < 0:
        x = 1 / x
        n = -n

    rt = power2(x, n // 2)

    if n % 2 == 0:
        return rt * rt
    else:
        return x * rt * rt
