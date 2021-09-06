from typing import List


def slowestKey(releaseTimes: List[int], keysPressed: str) -> str:
    longest = (releaseTimes[0], keysPressed[0])

    for i in range(1, len(releaseTimes)):
        longest = max(longest, (releaseTimes[i] - releaseTimes[i - 1], keysPressed[i]))

    return longest[1]
