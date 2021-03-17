import random
from typing import List


class Solution:
    """
    Rejection sampling
    """

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center
        self.x_min = x_center - radius
        self.x_max = x_center + radius
        self.y_min = y_center - radius
        self.y_max = y_center + radius

    def randPoint(self) -> List[float]:
        """
        Time: O(1), worst case O(infinity)
        Space: O(1)
        """
        while True:
            xr = random.uniform(self.x_min, self.x_max)
            yr = random.uniform(self.y_min, self.y_max)
            if (xr - self.x) ** 2 + (yr - self.y) ** 2 <= self.r ** 2:
                return [xr, yr]
