import heapq
from collections import defaultdict
from typing import List


class FileSharing:
    def __init__(self, m: int):
        self.next_id = 1
        self.free_ids = []
        self.chunks = defaultdict(set)  # chunk -> [user]
        self.users = defaultdict(set)  # user -> [chunk]

    def join(self, ownedChunks: List[int]) -> int:
        user_id = None
        if self.free_ids:
            user_id = heapq.heappop(self.free_ids)
        else:
            user_id = self.next_id
            self.next_id += 1

        self.users[user_id] = set(ownedChunks)
        for chunk in ownedChunks:
            self.chunks[chunk].add(user_id)

        return user_id

    def leave(self, userID: int) -> None:
        for chunk in self.users[userID]:
            self.chunks[chunk].remove(userID)
        del self.users[userID]
        heapq.heappush(self.free_ids, userID)

    def request(self, userID: int, chunkID: int) -> List[int]:
        users = sorted(self.chunks[chunkID])
        if users:
            self.users[userID].add(chunkID)
            self.chunks[chunkID].add(userID)
        return users
