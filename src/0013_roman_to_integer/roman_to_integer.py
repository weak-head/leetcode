
roman_map = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

def romanToInt(s: str) -> int:
    num, current_value = 0, 0
    for c in reversed(s):
        if not c in roman_map:
            raise "Invalid input"
        next_value = roman_map[c]
        if next_value >= current_value:
            num = num + current_value
            current_value = next_value
        else:
            current_value = current_value - next_value
    return num + current_value

if __name__ == '__main__':
    assert romanToInt('I') == 1
    assert romanToInt('IV') == 4
    assert romanToInt('VII') == 7
    assert romanToInt('IIX') == 8
    assert romanToInt('XVII') == 17
    assert romanToInt('IVIV') == 8

    print('done')