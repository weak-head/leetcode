
def reverse(x: int) -> int:
    abs_x = abs(x)
    x_str = str(abs_x)
    x_rev = int(x_str[::-1])
    if (x < 0):
        x_rev = x_rev * -1
    # 32-bit signed int boundaries
    if (x_rev < (-2**31) or x_rev > (2**31)-1):
            return 0
    return x_rev