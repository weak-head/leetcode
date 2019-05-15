s_to_n = {"a": "1", "b": "2", "c": "3"}
n_to_s = {1: "a", 2: "b", 3: "c"}


def countAndSay(n: int) -> str:
    r = "1"
    for _ in range(n - 1):
        r = count(say(r))
    return r


def count(s: str) -> str:
    r = []
    for n in s:
        if n in s_to_n:
            r.append(s_to_n[n])
        else:
            r.append(n)
    return "".join(r)


def say(n: str) -> str:
    r = []
    c, k = n[0], 0
    for v in n:
        if v == c:
            k = k + 1
        else:
            r.append(n_to_s[k])
            r.append(c)
            c, k = v, 1
    r.append(n_to_s[k])
    r.append(c)
    return "".join(r)
