from typing import List
from collections import deque


def dailyTemperatures(t: List[int]) -> List[int]:
    """
    Monotonic stack

    Time: O(n)
    Space: O(n)
        n - length of the array
    """
    r = deque()
    s = []
    for i in range(len(t) - 1, -1, -1):

        while s and t[s[-1]] <= t[i]:
            s.pop()

        next_warm = 0 if not s else s[-1] - i
        r.appendleft(next_warm)
        s.append(i)

    return r


def dailyTemperatures2(t: List[int]) -> List[int]:
    """
    Time: O(n)
    Space: O(1)
        n - length of the array
    """
    n = len(t)
    hottest = 0
    answer = [0] * n

    for curr_day in range(n - 1, -1, -1):
        current_temp = t[curr_day]
        if current_temp >= hottest:
            hottest = current_temp
            continue

        days = 1
        while t[curr_day + days] <= current_temp:
            days += answer[curr_day + days]

        answer[curr_day] = days

    return answer
