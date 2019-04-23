
def bitwiseComplement(N: int) -> int:
    if N == 0:
        return 1

    # finding most significant bit in N
    bits_num, n = 0, N
    while n != 0:
        bits_num = bits_num + 1
        n = n >> 1

    # populating all bits with '1' up to the most significant
    while bits_num != 0:
        n = (n << 1) | 1
        bits_num = bits_num - 1

    # complement
    return ~N & n