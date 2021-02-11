from typing import List
from functools import lru_cache


def minHeightShelves_dp_bu(books: List[List[int]], shelf_width: int) -> int:
    """
    Dynamic programming, bottom up

    Time: O(n * min(n, w))
    Space: O(n)
        n - number of books
        w - shelf width
    """

    min_h = [float("inf")] * (len(books) + 1)
    min_h[-1] = 0

    for section_start in range(len(books) - 1, -1, -1):

        section_width = 0
        section_height = 0
        for section_end in range(section_start, len(books)):
            section_width += books[section_end][0]
            if section_width > shelf_width:
                break

            section_height = max(section_height, books[section_end][1])
            min_h[section_start] = min(
                min_h[section_start], section_height + min_h[section_end + 1]
            )

    return min_h[0]


def minHeightShelves_dp_td(books: List[List[int]], shelf_width: int) -> int:
    """
    Dynamic programming, top down

    Time: O(n * min(n, w))
    Space: O(n)
        n - number of books
        w - shelf width
    """

    @lru_cache(None)
    def dp(i):
        if i >= len(books):
            return 0

        min_h = float("inf")
        section_width = 0
        section_height = 0
        for section_end in range(i, len(books)):
            section_width += books[section_end][0]  # book width
            if section_width > shelf_width:
                break

            section_height = max(section_height, books[section_end][1])  # book height
            min_h = min(min_h, section_height + dp(section_end + 1))

        return min_h

    return dp(0)
