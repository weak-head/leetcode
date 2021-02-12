def numberOfSteps(num: int) -> int:
    """
    Time: O(log n)
    Space: O(1)
        n - number of bits
    """
    c = 0
    while num > 0:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num - 1
        c += 1
    return c
