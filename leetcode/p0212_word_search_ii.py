from typing import List


def findWords_optimized(board: List[List[str]], words: List[str]) -> List[str]:
    """
    Backtracking with trie and multiple optimizations
    to prune branching

    Time: O(r * c * (3 ** l))
    Space: O(l)
        r - number of rows
        c - number of cols
        l - max length of the word in list
    """

    word_key = "##"

    trie = {}
    for word in words:
        node = trie
        for char in word:
            node = node.setdefault(char, {})
        node[word_key] = word

    res = []

    def track(r, c, parent):
        letter = board[r][c]
        current = parent[letter]

        # optimization:
        # - avoid duplicates
        # - reduce the size of the trie
        word_match = current.pop(word_key, False)
        if word_match:
            res.append(word_match)

        # optimization to avoid re-visit
        board[r][c] = "#"

        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < len(board)
                and 0 <= nc < len(board[0])
                and board[nr][nc] in current
            ):
                track(nr, nc, current)

        # optimization to avoid re-checks:
        # - reduce the size of the trie
        if not current:
            parent.pop(letter)

        # restore
        board[r][c] = letter

    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] in trie:
                track(r, c, trie)

    return res


def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    """
    Backtracking, not optimized
    Extremely slow

    Time: O(r * c * (3 ** l))
    Space: O(l)
        r - number of rows
        c - number of cols
        l - max length of the word in list
    """
    ws = set(words)
    max_len = max(map(len, words))
    res = set()

    def track(r, c, path, word, l):
        wrd = "".join(word)
        if wrd in ws:
            res.add(wrd)

        if l >= max_len:
            return

        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < len(board)
                and 0 <= nc < len(board[0])
                and (nr, nc) not in path
            ):
                path.add((nr, nc))
                track(nr, nc, path, word + [board[nr][nc]], l + 1)
                path.remove((nr, nc))

    for r in range(len(board)):
        for c in range(len(board[0])):
            track(r, c, set([(r, c)]), [board[r][c]], 1)

    return res
