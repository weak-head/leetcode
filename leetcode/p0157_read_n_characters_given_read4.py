def read4(buf4):
    buf4[0] = "a"
    buf4[1] = "b"
    buf4[2] = "c"
    buf4[3] = "d"
    return 4


def read(buf, n):
    read = 0
    buf4 = [""] * 4

    while read < n:
        got = read4(buf4)

        if not got:
            return read

        for i in range(got):
            buf[read] = buf4[i]
            read += 1

            if read == n:
                return read

    return read
