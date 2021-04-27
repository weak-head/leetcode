def isPowerOfThree(n: int) -> bool:
    """
    'n' is limited to 32-bit integer.
    The max power of 3 withing 32-bit int is
        3 ^ 19 = 1_162_261_467
    3 is prime number, so for 'n' to be the power of 3,
    the (3 ^ 19) should be divisible by 'n'.

    Time: O(1)
    Space: O(1)
    """
    return n > 0 and 1_162_261_467 % n == 0
