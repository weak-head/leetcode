
def atoi(s: str) -> int:
    # trim (only) spaces from the left
    l_ix, s_len = 0, len(s)
    while l_ix < s_len and s[l_ix] == ' ':
        l_ix = l_ix + 1
    if l_ix >= s_len:
        return 0

    # parse the sign
    sign = 1
    if s[l_ix] in ['-', '+']:
        sign = -1 if s[l_ix] == '-' else 1
        l_ix = l_ix + 1

    # parse the value
    result, digit_base = 0, ord('0')
    while l_ix < s_len:
        digit = ord(s[l_ix]) - digit_base
        if (digit < 0 or digit > 9):
            break
        result = (result * 10) + digit
        l_ix = l_ix + 1

    # 32-bit integer
    return max(-2**31, min(sign * result, 2**31-1))

if __name__ == '__main__':
    assert atoi('') == 0
    assert atoi('   37') == 37
    assert atoi('   +37') == 37
    assert atoi('   -37') == -37
    assert atoi('   \t42') == 0
    assert atoi('db 44 2') == 0
    assert atoi('  -db') == 0
    assert atoi('-32db') == -32
    assert atoi(' -32 db') == -32
    assert atoi('-91283472332') == -2147483648

    print('done')