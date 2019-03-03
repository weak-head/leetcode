from math import ceil

def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    converted_str  = []
    pattern_length = (numRows - 1) * 2
    s_length       = len(s)
    patterns_in_string = ceil(s_length / pattern_length)

    for row_ix in range(0, numRows):
        for pattern_ix in range(0, patterns_in_string):
            next_element_ix = pattern_ix * pattern_length + row_ix
            if next_element_ix >= s_length:
                break
            converted_str.append(s[next_element_ix])

            # the first and the last rows are having one element from the pattern
            # all other intermediate rows are having two elements
            if row_ix != 0 and row_ix != numRows-1:
                next_element_ix = pattern_ix * pattern_length + (pattern_length - row_ix)
                if next_element_ix >= s_length:
                    break
                converted_str.append(s[next_element_ix])
    return ''.join(converted_str)

if __name__ == '__main__':
    assert convert('', 10) == ''
    assert convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
    assert convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'
    assert convert('PAYPALISHIRING', 99) == 'PAYPALISHIRING'
    assert convert('PAYPALISHIRING', 1) == 'PAYPALISHIRING'
    assert convert('PAYPALISHIRING', 2) == 'PYAIHRNAPLSIIG'

    print('passed')
