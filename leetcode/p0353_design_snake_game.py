from collections import deque
from typing import List


class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.snake = deque([(0, 0)])
        self.snake_set = set([(0, 0)])
        self.food = deque(food)
        self.width = width
        self.height = height
        self.moves = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    def move(self, direction: str) -> int:
        """
        O(1)
        """

        newHead = (
            self.snake[-1][0] + self.moves[direction][0],
            self.snake[-1][1] + self.moves[direction][1],
        )

        verticalWallCollision = newHead[0] < 0 or newHead[0] >= self.height
        horizontalWallCollision = newHead[1] < 0 or newHead[1] >= self.width
        bitHerself = newHead in self.snake_set and newHead != self.snake[0]

        if verticalWallCollision or horizontalWallCollision or bitHerself:
            return -1

        if (
            self.food
            and (newHead[0] == self.food[0][0])
            and (newHead[1] == self.food[0][1])
        ):
            self.food.popleft()
        else:
            tail = self.snake.popleft()
            self.snake_set.remove(tail)

        self.snake.append(newHead)
        self.snake_set.add(newHead)

        return len(self.snake) - 1
