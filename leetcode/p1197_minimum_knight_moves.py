from functools import lru_cache
from collections import deque


def minKnightMoves_bfs_one_dir(x: int, y: int) -> int:
    """
    BFS from 0 to final point
    O(|x| * |y|)
    """
    q = deque([(0, 0, 0)])
    x, y, visited = abs(x), abs(y), set([(0, 0)])

    while True:
        cx, cy, step = q.popleft()
        if cx == x and cy == y:
            return step
        # since we have abs(x) and abs(y) we don't need to consider
        # (-1, -2) and (-2, -1)
        for dx, dy in [(1, 2), (2, 1), (1, -2), (-1, 2), (2, -1), (-2, 1)]:
            # Ignore visited and limit problem space to rectangle with (x,y) being
            # the upper right point
            if ((cx + dx, cy + dy) not in visited) and (
                -1 <= cx + dx <= x + 2 and -1 <= cy + dy <= y + 2
            ):
                visited.add((cx + dx, cy + dy))
                q.append((cx + dx, cy + dy, step + 1))


def minKnightMoves_bfs_two_dir(x: int, y: int) -> int:
    """
    BFS, dwo directional
    O(|x| * |y|)
    """
    x, y = abs(x), abs(y)

    vb = {(0, 0): 0}
    qb = deque([(0, 0, 0)])

    vf = {(x, y): 0}
    qf = deque([(x, y, 0)])

    while True:
        bx, by, bstep = qb.popleft()
        if (bx, by) in vf:
            return bstep + vf[(bx, by)]

        fx, fy, fstep = qf.popleft()
        if (fx, fy) in vb:
            return fstep + vb[(fx, fy)]

        for dx, dy in [
            (1, 2),
            (2, 1),
            (1, -2),
            (-1, 2),
            (2, -1),
            (-2, 1),
            (-1, -2),
            (-2, -1),
        ]:
            # steps from initial point
            if ((bx + dx, by + dy) not in vb) and (
                -1 <= bx + dx <= x + 2 and -1 <= by + dy <= y + 2
            ):
                vb[(bx + dx, by + dy)] = bstep + 1
                qb.append((bx + dx, by + dy, bstep + 1))

            # steps from final point
            if ((fx + dx, fy + dy) not in vf) and (
                -1 <= fx + dx <= x + 2 and -1 <= fy + dy <= y + 2
            ):
                vf[(fx + dx, fy + dy)] = fstep + 1
                qf.append((fx + dx, fy + dy, fstep + 1))


def minKnightMoves_dfs_dp(x: int, y: int) -> int:
    """
    DFS, DP
    O(log(max(|x|, |y|)))
    """

    @lru_cache(None)
    def step(x, y):
        # x == 0 and y == 0
        if x + y == 0:
            return 0

        # (x == 0 and y == 2) or (x == 1 and y == 1) or (x == 2 and y == 0)
        elif x + y == 2:
            return 2

        else:
            return min(step(abs(x - 1), abs(y - 2)), step(abs(x - 2), abs(y - 1))) + 1

    return step(abs(x), abs(y))


def minKnightMoves_math(x: int, y: int) -> int:
    """
    Math formula
    O(1)
    """
    x, y = abs(x), abs(y)

    if x < y:
        x, y = y, x

    if x == 1 and y == 0:
        return 3

    if x == 2 and y == 2:
        return 4

    delta = x - y

    if y > delta:
        return delta - 2 * int((delta - y) // 3)
    else:
        return delta - 2 * int((delta - y) // 4)
