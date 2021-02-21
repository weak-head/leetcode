def brokenCalc(X: int, Y: int) -> int:
    """
    Time: O(log Y)
    Space: O(1)
    """
    ops = 0
    while Y > X:
        if Y % 2 == 0:
            Y = Y // 2
        else:
            Y = Y + 1
        ops += 1

    return ops + (X - Y)
