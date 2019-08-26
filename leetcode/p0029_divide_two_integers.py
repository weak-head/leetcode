def divide(dividend: int, divisor: int) -> int:
    """
    The fast division that subtracts powers of divisor from dividend.
    """
    sign = -1 if (divisor < 0 and dividend > 0) or (dividend < 0 and divisor > 0) else 1
    dividend, divisor = abs(dividend), abs(divisor)
    result = 0

    while dividend >= divisor:
        acc_div, tr = divisor, 1
        while dividend >= acc_div:
            tr = tr << 1
            acc_div = acc_div << 1
        dividend -= acc_div >> 1
        result += tr >> 1

    result = result * sign
    return min((2 ** 31 - 1), max(-2 ** 31, result))
