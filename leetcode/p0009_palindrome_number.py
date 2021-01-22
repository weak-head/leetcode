def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    number = []
    while x != 0:
        x, digit = divmod(x, 10)
        number.append(digit)
    number_len = len(number) - 1
    for ix in range(0, (number_len + 1) >> 1):
        if number[ix] != number[number_len - ix]:
            return False
    return True


def isPalindrome_2(x: int) -> bool:
    num = str(x)
    return num == num[::-1]
