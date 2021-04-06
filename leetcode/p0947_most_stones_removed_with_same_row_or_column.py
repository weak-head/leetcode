from collections import defaultdict
from typing import List


def removeStones(stones: List[List[int]]) -> int:
    """
    Union-find

    Time: O(n)
    Space: O(n)
        n - number of stones
    """
    parent = [i for i in range(len(stones))]
    rank = [0] * len(stones)

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        pa = find(a)
        pb = find(b)
        if rank[pa] > rank[pb]:
            parent[pb] = pa
        else:
            parent[pa] = pb
            if rank[pa] == rank[pb]:
                rank[pb] += 1

    cols = {}
    rows = {}

    # Union stones based on col and row
    for ix, (col, row) in enumerate(stones):
        if col in cols:
            union(ix, cols[col])
        else:
            cols[col] = ix

        if row in rows:
            union(ix, rows[row])
        else:
            rows[row] = ix

    # Evaluate stone groups
    groups = defaultdict(int)
    for ix in range(len(stones)):
        groups[find(ix)] += 1

    res = 0
    for val in groups.values():
        res += val - 1  # one stone is left in the end

    return res
