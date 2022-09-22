from typing import List
import heapq


def minCostConnectPoints1(points: List[List[int]]) -> int:
    """
    Kruskal algorithm
    Disjoint Set / Union Find

    Time: O(n^2 * log n)
    Space: O(n^2)
    """

    parent = [i for i in range(len(points))]
    rank = [1] * len(points)

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        xp = find(x)
        yp = find(y)

        # will create a cycle
        if xp == yp:
            return False

        if rank[xp] > rank[yp]:
            parent[yp] = xp
        elif rank[yp] > rank[xp]:
            parent[xp] = yp
        else:
            parent[xp] = yp
            rank[yp] += 1
        return True

    edges = []
    for first in range(len(points)):
        for second in range(first + 1, len(points)):
            weight = abs(points[first][0] - points[second][0]) + abs(
                points[first][1] - points[second][1]
            )
            edges.append((weight, first, second))

    # Greedy
    edges.sort()

    min_cost = 0
    used_edges = 0
    for weight, first, second in edges:
        if union(first, second):
            min_cost += weight
            used_edges += 1
            if used_edges == len(points) - 1:
                break

    return min_cost


def minCostConnectPoints2(points: List[List[int]]) -> int:
    """
    Prim's algorithm

    Time: O(n^2 * log n)
    Space: O(n^2)
    """

    h = [(0, 0)]
    min_cost = 0
    used_edges = 0
    used_nodes = [False] * len(points)

    # n-1 edges for minimal spanning tree with n nodes
    while used_edges < len(points):
        weight, node = heapq.heappop(h)

        if used_nodes[node]:
            continue

        used_nodes[node] = True
        used_edges += 1
        min_cost += weight

        for other_node in range(len(points)):
            if not used_nodes[other_node]:
                weight = abs(points[node][0] - points[other_node][0]) + abs(
                    points[node][1] - points[other_node][1]
                )
                heapq.heappush(h, (weight, other_node))

    return min_cost


def minCostConnectPoints3(points: List[List[int]]) -> int:
    """
    Prim's algorithm (optimized)

    Time: O(n^2)
    Space: O(n)
    """
    min_cost = 0
    edges_used = 0

    used_nodes = [False] * len(points)
    min_weight = [float("inf")] * len(points)
    min_weight[0] = 0

    while edges_used < len(points):
        weight = float("inf")
        node = -1

        # Find the minimal weight edge
        for i in range(len(points)):
            if not used_nodes[i] and min_weight[i] < weight:
                weight = min_weight[i]
                node = i

        min_cost += weight
        edges_used += 1
        used_nodes[node] = True

        for i in range(len(points)):
            weight = abs(points[node][0] - points[i][0]) + abs(
                points[node][1] - points[i][1]
            )

            if not used_nodes[i] and weight < min_weight[i]:
                min_weight[i] = weight

    return min_cost
