from typing import List


def spellchecker(wordlist: List[str], queries: List[str]) -> List[str]:
    """
    Time: O(max(n * c, m * q))
    Space: O(n * c)
        n - number of words in wordlist
        m - number of queries
        c - max length of the word in word list
        q - max length of the query
    """
    plain = {}
    capital = {}
    vowel = {}

    def key(word):
        k = []
        for char in word:
            c = char.lower()
            if c in {"a", "o", "i", "u", "e"}:
                k.append("*")
            else:
                k.append(c)
        return "".join(k)

    for word in wordlist:
        plain[word] = word

        lower = word.lower()
        if lower not in capital:
            capital[lower] = word

        wkey = key(word)
        if wkey not in vowel:
            vowel[wkey] = word

    r = []
    for query in queries:
        if query in plain:
            r.append(query)
            continue

        lower = query.lower()
        if lower in capital:
            r.append(capital[lower])
            continue

        wkey = key(query)
        if wkey in vowel:
            r.append(vowel[wkey])
            continue

        r.append("")

    return r
