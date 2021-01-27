from collections import deque


def concatenatedBinary_slow(n: int) -> int:
    """
    Just for fun

    Time: O(n * log(n))
        n - input number
    """

    def next(base):
        """
        Gets the next binary number
        Time: O(n)
            n - number of bits
        """
        r, c = deque(), 1
        for ix in reversed(range(len(base))):
            r.appendleft(base[ix] ^ c)
            c = base[ix] and c

        if c:
            r.appendleft(1)

        return r

    def to_dec(binary):
        """
        Converts binary to decimal
        Time: O(n)
            n - number of bits
        """
        dec = 0
        for ix in range(0, len(binary)):
            dec += pow(2, ix) if binary[-(ix + 1)] else 0
        return dec

    v, r = [1], [1]
    for i in range(2, n + 1):  # O(n)
        v = next(v)  # O(log(n))
        r.extend(v)

    return to_dec(r) % (pow(10, 9) + 7)


def concatenatedBinary_fast(n: int) -> int:
    """
    Time: O(n * log(n))
    """
    concatenation = "".join(bin(i)[2:] for i in range(n + 1))
    return int(concatenation, 2) % (10 ** 9 + 7)
