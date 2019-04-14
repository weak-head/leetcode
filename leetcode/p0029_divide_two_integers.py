
def divide(dividend: int, divisor: int) -> int:
    sign = 0 if dividend > 0 else 1
    sign = sign if divisor > 0 else sign + 1
    sign = -1 if (sign % 2) else 1

    dividend = abs(dividend)
    divisor = abs(divisor)
    result = 0

    while dividend >= divisor:
        acc_div, tr = divisor, 1
        while dividend >= acc_div:
            tr = tr << 1
            acc_div = acc_div << 1
        dividend = dividend - (acc_div >> 1)
        result = result + (tr >> 1)

    result = result * sign
    return min((2**31 - 1), max(-2**31, result))
