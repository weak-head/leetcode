from typing import List


def floodFill(
    image: List[List[int]], sr: int, sc: int, newColor: int
) -> List[List[int]]:
    if image[sr][sc] == newColor:
        return image

    def fill(r, c, old, new):
        if not (0 <= r < len(image) and 0 <= c < len(image[0])):
            return

        if image[r][c] != old:
            return

        image[r][c] = new

        fill(r + 1, c, old, new)
        fill(r - 1, c, old, new)
        fill(r, c + 1, old, new)
        fill(r, c - 1, old, new)

    fill(sr, sc, image[sr][sc], newColor)
    return image
