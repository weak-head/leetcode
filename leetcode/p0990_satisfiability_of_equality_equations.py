from typing import List


def equationsPossible(equations: List[str]) -> bool:
    """
    Union-find

    Time: O(n)
    Space: O(n)
        n - number of equations
    """
    n = 26  # up to 26 english characters

    parent = [i for i in range(n)]
    rank = [0] * n

    def ix(c):
        return ord(c) - ord("a")

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        xp, yp = find(x), find(y)
        if rank[xp] < rank[yp]:
            parent[xp] = yp
        else:
            parent[yp] = xp
            if rank[yp] == rank[xp]:
                rank[xp] += 1

    def connected(x, y):
        return find(x) == find(y)

    # union all connected
    for eq in equations:
        if eq[1] == "=":
            union(ix(eq[0]), ix(eq[3]))

    # check all disconnected
    for eq in equations:
        if eq[1] == "!":
            if connected(ix(eq[0]), ix(eq[3])):
                return False

    return True
