from typing import List
from collections import defaultdict, deque


def numBusesToDestination(routes: List[List[int]], source: int, target: int) -> int:
    """
    Breadth First Search
    Each bus route is a single node.
    Nodes are connected if routes intersect.

    Time: O(n * n * m)
    Space: O(n * n)
        n - number of routes (nodes)
        m - max number of stops in the route
    """
    if source == target:
        return 0

    routes = list(map(set, routes))

    # each route is a single note in the graph,
    # nodes are connected if routes intersect
    graph = defaultdict(set)
    for ix1, route1 in enumerate(routes):
        for ix2 in range(ix1 + 1, len(routes)):
            route2 = routes[ix2]

            # route intersect
            if any(r in route2 for r in route1):
                graph[ix1].add(ix2)
                graph[ix2].add(ix1)

    # seen - all routes that intersect source
    # targets - all routes that intersect target
    seen = set()
    targets = set()
    for node, route in enumerate(routes):
        if source in route:
            seen.add(node)

        if target in route:
            targets.add(node)

    # (node, num_buses)
    queue = deque([(node, 1) for node in seen])

    # BFS
    while queue:
        node, buses = queue.popleft()

        if node in targets:
            return buses

        for connected_node in graph[node]:
            if connected_node not in seen:
                seen.add(connected_node)
                queue.append((connected_node, buses + 1))

    return -1
