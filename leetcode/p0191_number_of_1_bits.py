def hammingWeight(n: int) -> int:
    """
    Flip least significant bit to zero
    and count flips.

    Time: O(1) # because 'n' is 32-bit value
    Space: O(1)
    """
    c = 0
    while n:
        # flip least significant bit
        # of the number that is '1' to zero
        #        n   = 110100
        #      (n-1) = 110011
        #  n & (n-1) = 110000
        n &= n - 1
        c += 1
    return c


def hammingWeight2(n: int) -> int:
    """
    Convert to binary and count bits.

    Time: O(1)
    Space: O(1)
    """
    c, s = 0, bin(n)[2:]
    for v in s:
        c += 1 if v == "1" else 0
    return c
