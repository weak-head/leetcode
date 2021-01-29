from typing import List
from collections import Counter, defaultdict
import math
import itertools


def countCornerRectangles1(grid: List[List[int]]) -> int:
    """
    Time: O(r * c * c)
    Space: O(c * c)
        r - number of rows
        c - number of columns
    """

    count = Counter()
    total_count = 0
    for row in grid:
        for cl_ix, cl_val in enumerate(row):

            # left corner
            if cl_val:
                for cr_ix in range(cl_ix + 1, len(row)):

                    # right corner
                    if row[cr_ix]:

                        # The number of rectangles that we can compose
                        # from the vertical line of '1's is a simple
                        # arithmetic sequence.
                        # If we have n == 5 '1's in the column,
                        # we can create [(n-1) * n] / 2 ==
                        # [4 * 5] / 2 == 10 rectangles.
                        #   count[(l, r)] - n in the sequence
                        # . total_count - accumulates the values
                        total_count += count[(cl_ix, cr_ix)]
                        count[(cl_ix, cr_ix)] += 1

    return total_count


def countCornerRectangles2(grid: List[List[int]]) -> int:
    ones = defaultdict(set)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                ones[col].add(row)

    counter = 0
    for key1, key2 in itertools.combinations(ones.keys(), 2):
        counter += math.comb(len(ones[key1].intersection(ones[key2])), 2)

    return counter
