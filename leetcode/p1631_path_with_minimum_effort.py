from typing import List
import heapq
import math


def minimumEffortPath_bf(heights: List[List[int]]) -> int:
    """
    Brute force with optimization: backtracking (dfs) + greedy pick,
    exponential time

    Time: O(3 ^ (r * c))
        3 -> possible choices from each cell (avoid going back)
        r -> number of rows
        c -> number of columns

    Space: O(r * c)

    Leetcode: Time Limit Exceeded
    """

    rn, cn = len(heights), len(heights[0])
    effort = [[float("inf") for _ in range(cn)] for _ in range(rn)]

    def dfs(r, c, prev_height, max_effort):
        nonlocal effort, rn, cn

        # out of boundary
        if r < 0 or c < 0 or r >= rn or c >= cn:
            return

        # no need to check this cell if the effort is same
        # also it helps to avoid the cycle
        move_effort = max(abs(heights[r][c] - prev_height), max_effort)
        if effort[r][c] <= move_effort:
            return

        effort[r][c] = move_effort

        def delta(move, r, c):
            if (
                r + move[0] < 0
                or c + move[1] < 0
                or r + move[0] >= rn
                or c + move[1] >= cn
            ):
                return float("inf")

            return abs(heights[r][c] - heights[r + move[0]][c + move[1]])

        # greedy, pick the min effort first
        moves_delta = sorted(
            [(move, delta(move, r, c)) for move in [(0, -1), (1, 0), (0, 1), (-1, 0)]],
            key=lambda x: x[1],
        )
        for move, _ in moves_delta:
            dfs(r + move[0], c + move[1], heights[r][c], move_effort)

    dfs(0, 0, heights[0][0], 0)
    return effort[rn - 1][cn - 1]


def minimumEffortPath_dijkstra(heights: List[List[int]]) -> int:
    """
    Use Dijkstra's algorithm to find the shortest path in a weighted graph,
    the weight between vertices is the absolute difference of heights.
    https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

    Time: O( (r*c) * log(r*c) )
        r - number of rows
        c - number of columns

    Space: O(r * c)
    """
    rn, cn = len(heights), len(heights[0])
    effort = [[math.inf for _ in range(cn)] for _ in range(rn)]

    # We could have multiple same nodes in the queue with different effort.
    # When we extract the node from queue and process it - it has the minimal effort,
    # so we don't need to process any other instances of the node in the queue.
    # The calculation is idempotent, so this check is optional, but it speeds up
    # the processing a bit, but it doesn't affect the time complexity.
    processed = [[False for _ in range(cn)] for _ in range(rn)]

    effort[0][0] = 0
    q = [(0, 0, 0)]  # effort, row, col
    while q:
        _, r, c = heapq.heappop(q)
        processed[r][c] = True

        for rd, cd in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            new_r, new_c = r + rd, c + cd

            # if in the boundary and not processed yet
            if 0 <= new_r < rn and 0 <= new_c < cn and not processed[new_r][new_c]:
                move_effort = max(
                    effort[r][c],
                    abs(heights[r][c] - heights[new_r][new_c]),
                )

                if move_effort < effort[new_r][new_c]:
                    effort[new_r][new_c] = move_effort
                    heapq.heappush(q, (move_effort, new_r, new_c))

    return effort[-1][-1]


def minimumEffortPath_binary_bfs(heights: List[List[int]]) -> int:
    """
    This could be achieved using either DFS or BFS.
    This version uses BFS.

    Use binary search to narrow down the max effort [O(log h)],
    and for every search attempt walk the graph [O(r * c)] to the end,
    picking nodes based on effort condition.

    Time: O(r * c * log(h))
        r - number of rows
        c - number of columns
        h - max possible height

    Space: O(r * c)

    Leetcode: Extremely slow because of the [log(h)] part.
    """
    rn, cn = len(heights), len(heights[0])

    def canReachDestinaton(mid):
        """
        Returns True if there exist path from (0, 0) to (row-1, col-1),
        with effort less than 'mid'.
        """
        visited = [[False] * cn for _ in range(rn)]
        queue = [(0, 0)]  # x, y
        while queue:
            r, c = queue.pop(0)
            if r == rn - 1 and c == cn - 1:
                return True

            visited[r][c] = True
            for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                new_r, new_c = r + dr, c + dc

                if 0 <= new_r < rn and 0 <= new_c < cn and not visited[new_r][new_c]:
                    move_effort = abs(heights[new_r][new_c] - heights[r][c])
                    if move_effort <= mid:
                        visited[new_r][new_c] = True
                        queue.append((new_r, new_c))

    left, right = 0, 10000000
    while left < right:
        mid = (left + right) // 2
        if canReachDestinaton(mid):
            right = mid
        else:
            left = mid + 1

    return left
