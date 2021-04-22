from typing import List
from collections import defaultdict


def leastBricks(wall: List[List[int]]) -> int:
    """
    Least bricks would be at
    the max number of spaces.

    By finding the max number of spaces,
    inside the wall, we can get the least
    number of bricks.

    Time: O(n)
    Space: O(n)
        n - number of bricks in the wall
    """
    c = defaultdict(int)  # location -> spaces
    for row in wall:
        location = 0
        for brick in row[:-1]:  # ignore the last brick
            location += brick
            c[location] += 1  # space at the location

    max_spaces = max(c.values())
    return len(wall) - max_spaces
