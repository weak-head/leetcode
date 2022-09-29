import heapq
from typing import List
from collections import deque, defaultdict


def findCheapestPrice1(
    n: int, flights: List[List[int]], src: int, dst: int, k: int
) -> int:
    """
    Dijkstra's Algorithm

    Time: O(v^2 * log v)
    Space: O(v^2)
        v - vertices
    """

    # build graph
    graph = defaultdict(list)
    for source, dest, price in flights:
        graph[source].append([price, dest])

    distances = [float("inf")] * n
    stops = [float("inf")] * n
    distances[src], stops[src] = 0, 0

    # min heap
    # (cost, stops, node)
    queue = [(0, 0, src)]

    while queue:
        cost, stop, node = heapq.heappop(queue)

        # if destination is reached,
        # we have found the min cost
        if node == dst:
            return cost

        # if there are no more stops left,
        # continue
        if stop > k:
            continue

        for price, dest in graph[node]:
            n_cost = cost + price

            # Better cost?
            if n_cost < distances[dest]:
                distances[dest] = n_cost
                heapq.heappush(queue, (n_cost, stop + 1, dest))
                stops[dest] = stop + 1

            # Better steps?
            elif stop < stops[dest]:
                heapq.heappush(queue, (n_cost, stop + 1, dest))

    return distances[dst] if distances[dst] != float("inf") else -1


def findCheapestPrice2(
    n: int, flights: List[List[int]], src: int, dst: int, k: int
) -> int:
    """
    Breadth-first search

    Time: O(e * k)
    Space: O(v^2 + v * k)
        v - vertices
        e - edges
        k - steps

        Each edge is processed at most (k+1) times
        Adjacency matrix (v^2) + distance map (v * k)
    """

    # adjacency matrix
    m = [[0 for _ in range(n)] for _ in range(n)]
    for s, d, w in flights:
        m[s][d] = w

    # shortest distance map
    # (node, stops) => min_distance
    distance = {}
    distance[(src, 0)] = 0

    # queue
    q = deque([src])

    # stops remaining
    stops = 0
    answer = float("inf")

    # iterate level-by-level,
    # until queue is empty or we cannot do more steps
    while q and stops <= k:

        # exhaust queue by "q_len" nodes
        # that represent the current "level"
        q_len = len(q)
        for _ in range(q_len):
            node = q.popleft()

            # check every connection that is
            # reachable from this node
            for connection in range(n):
                if m[node][connection] > 0:
                    n_distance = distance.get((node, stops), float("inf"))
                    c_distance = distance.get((connection, stops + 1), float("inf"))
                    nc_weight = m[node][connection]

                    # last stop, but not the destination
                    if stops == k and connection != dst:
                        continue

                    # new min distance to connection node
                    if n_distance + nc_weight < c_distance:
                        distance[(connection, stops + 1)] = n_distance + nc_weight
                        q.append(connection)

                        if connection == dst:
                            answer = min(answer, n_distance + nc_weight)

        stops += 1

    return -1 if answer == float("inf") else answer
