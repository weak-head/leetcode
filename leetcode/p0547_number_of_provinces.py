from typing import List
from collections import deque


def findCircleNum_uf(isConnected: List[List[int]]) -> int:
    """
    Disjoint set / union find

    Time: O(n^2)
    Space: O(n)
        n - number of cities
    """

    n = len(isConnected)
    parent = list(range(n))
    rank = [1] * n

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        xp = find(x)
        yp = find(y)
        if rank[xp] < rank[yp]:
            parent[xp] = yp
        else:
            parent[yp] = xp
            if rank[xp] != rank[yp]:
                rank[xp] += 1

    for i in range(n):
        for j in range(n):
            if i != j and isConnected[i][j]:
                union(i, j)

    return len({find(x) for x in parent})


def findCircaNum_bfs(isConnected):
    """
    BFS

    Time: O(n^2)
    Space: O(n)
    """

    n = len(isConnected)
    seen = set()
    res = 0

    def bfs(i):
        q = deque([i])
        seen.add(i)

        while q:
            ix = q.popleft()

            for j in range(n):
                if j not in seen and isConnected[ix][j]:
                    q.append(j)
                    seen.add(j)

    for i in range(n):
        if i not in seen:
            bfs(i)
            res += 1

    return res
