def divide(dividend: int, divisor: int) -> int:
    """
    The fast division that subtracts powers of divisor from dividend.

    Time: O(log n)
    Space: O(1)
        n - number of bits in dividend
    """
    sign = -1 if (divisor < 0 and dividend > 0) or (dividend < 0 and divisor > 0) else 1
    dividend, divisor = abs(dividend), abs(divisor)
    quotient = 0

    while dividend >= divisor:
        d, t = divisor, 1
        while dividend >= d:
            t, d = t << 1, d << 1
        dividend -= d >> 1
        quotient += t >> 1

    quotient = quotient * sign
    return min((2 ** 31 - 1), max(-(2 ** 31), quotient))
