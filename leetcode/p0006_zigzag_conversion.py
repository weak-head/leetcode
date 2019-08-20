from math import ceil


def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    converted_str = []
    pattern_length = (numRows - 1) * 2
    s_length = len(s)
    patterns_in_string = ceil(s_length / pattern_length)

    for row_ix in range(0, numRows):
        for pattern_ix in range(0, patterns_in_string):
            next_element_ix = pattern_ix * pattern_length + row_ix
            if next_element_ix >= s_length:
                break
            converted_str.append(s[next_element_ix])

            # the first and the last rows are having one element from the pattern
            # all other intermediate rows are having two elements
            if row_ix != 0 and row_ix != numRows - 1:
                next_element_ix = pattern_ix * pattern_length + (
                    pattern_length - row_ix
                )
                if next_element_ix >= s_length:
                    break
                converted_str.append(s[next_element_ix])
    return "".join(converted_str)


def convert2(s: str, numRows: int) -> str:
    """
    Instead of computing indexes, we can just
    follow the movement of the string flow.
    The zigzag pattern makes the string flow
    up and down that is easy to follow.
    """
    if numRows == 1 or numRows > len(s):
        return s

    # Initially all rows are empty
    row = [""] * numRows

    # The initial direction is 'down'
    i, direction = 0, False

    for c in s:

        # append the next character
        # to the end of current row
        row[i] += c

        # we have to switch movement direction
        # as soon as we have reached the begining
        # or end of rows
        if i == 0 or i == numRows - 1:
            direction = not direction

        # move to next (or previous) row
        # based on the current movement direction
        i += 1 if direction else -1

    return "".join(row)
