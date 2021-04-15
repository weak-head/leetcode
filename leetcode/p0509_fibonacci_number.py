def fib(n: int) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    if n in {0, 1}:
        return n

    p1, p2, f = 0, 1, 0
    while n > 1:
        f = p1 + p2
        p1, p2 = p2, f
        n -= 1
    return f
