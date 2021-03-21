from collections import Counter


def reorderedPowerOf2(n: int) -> bool:
    """
    Count frequency of digits,
    and compare it with frequencies of digits
    in powers of two.

    Time: log(n)
    Space: log(n)
    """
    cnt = Counter(str(n))
    power = 1
    for _ in range(31):
        if cnt == Counter(str(power)):
            return True
        power = power << 1
    return False
