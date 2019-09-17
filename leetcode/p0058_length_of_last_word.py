def length_of_last_word(s: str) -> int:
    slen = len(s)
    end_ix = None

    for start_ix in range(slen - 1, -1, -1):
        if s[start_ix] == " ":
            if end_ix:
                return end_ix - start_ix
        else:
            if end_ix is None:
                end_ix = start_ix

    if end_ix is not None:
        return end_ix + 1
    else:
        return 0
