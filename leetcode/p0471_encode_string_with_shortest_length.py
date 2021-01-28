def encode(s: str, memo={}) -> str:
    if s not in memo:
        n = len(s)

        # Depending on alg: O(n) up to O(n^2)
        # (i = n) if there are no repetitions
        # (i < n) if 's' is composed out of repetition
        # 'i' the index of first repetition
        i = (s + s).find(s, 1)

        # Try to encode the string 's' as 'k[val]'
        # where 'val' is our repetition represtented by s[:i].
        # (n / i) - number of repetitions of substring s[:i] in string 's'
        one = "%d[%s]" % (n / i, encode(s[:i])) if i < n else s

        # O(n^2) => Theare total of (n^2) substrings of original string 's'
        # try to encode each substring separately
        multi = [encode(s[:split]) + encode(s[split:]) for split in range(1, n)]

        # pick the solution with minimal length and memoize it
        memo[s] = min([s, one] + multi, key=len)

    return memo[s]
