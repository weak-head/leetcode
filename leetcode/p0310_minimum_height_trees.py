from collections import defaultdict
from typing import List
from sortedcontainers import SortedDict


def findMinHeightTrees_ts(n: int, edges: List[List[int]]) -> List[int]:
    """
    Topological sorting
    Remove leafs layer-by-layer

    Time: O(n)
    Space: O(n)
    """
    if n <= 2:
        return [i for i in range(n)]

    # build graph
    g = {i: set() for i in range(n)}
    for f, t in edges:
        g[f].add(t)
        g[t].add(f)

    # leaf nodes
    leafs = []
    for node in range(n):
        if len(g[node]) == 1:
            leafs.append(node)

    # remove leafs layer-by-layer
    left_nodes = n
    while left_nodes > 2:
        left_nodes -= len(leafs)
        new_leafs = []

        while leafs:
            leaf = leafs.pop()
            parent = g[leaf].pop()
            g[parent].remove(leaf)
            if len(g[parent]) == 1:
                new_leafs.append(parent)

        leafs = new_leafs

    return leafs


def findMinHeightTrees_brute_force(n: int, edges: List[List[int]]) -> List[int]:
    """
    Brute-force Depth First Search
    Time Limit Exceeded

    Time: O(n^2)
    Space: O(n)
    """
    if n == 0:
        return []

    # build graph
    g = defaultdict(list)
    for f, t in edges:
        g[f].append(t)
        g[t].append(f)

    # DFS
    def walk(node: int, level: int, visited):
        max_level = level
        visited.add(node)
        for child in g[node]:
            if child not in visited:
                max_level = max(max_level, walk(child, level + 1, visited))
        return max_level

    # keep max depth of each walk in sorted order
    sorted_dict = SortedDict()
    for root in range(n):
        max_level = walk(root, 0, set())
        if max_level not in sorted_dict:
            sorted_dict[max_level] = []
        sorted_dict[max_level].append(root)

    # min depth
    return sorted_dict[sorted_dict.keys()[0]]
