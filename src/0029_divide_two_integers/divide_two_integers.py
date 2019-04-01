
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


if __name__ == '__main__':
    assert divide(1, 1) == 1

    assert divide(10, 3) == 3
    assert divide(10, -3) == -3
    assert divide(-10, 3) == -3
    assert divide(-10, -3) == 3

    assert divide(1234321, 1) == 1234321

    assert divide(-2**31, -1) == 2**31 - 1
    assert divide(2**31 - 1, -1) == (-2**31) + 1

    assert divide(2**10, 2) == 2**9
    assert divide(2**20, 2**10) == 2**10

    print('passed')