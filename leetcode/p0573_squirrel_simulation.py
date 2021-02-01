from typing import List


def minDistance(
    height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]
) -> int:
    """
    Order of picking all nuts except the first doesn't matter.
    We need to find the nut that yields the best saving of distance.

    Time: O(n)
    Space: O(1)
        n - number of nuts
    """
    tx, ty = tree
    sx, sy = squirrel
    total_dist = 0

    best_nut_saving = float("-inf")
    for nx, ny in nuts:
        tree_to_nut = abs(tx - nx) + abs(ty - ny)
        squirrel_to_nut = abs(sx - nx) + abs(sy - ny)

        # saving in case if squirrel picks this nut first
        distance_saving = tree_to_nut - squirrel_to_nut
        best_nut_saving = max(best_nut_saving, distance_saving)

        total_dist += tree_to_nut * 2

    total_dist -= best_nut_saving
    return total_dist
