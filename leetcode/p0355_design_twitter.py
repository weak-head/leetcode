import itertools
import heapq
from collections import defaultdict, deque


class Twitter:
    """
    -- Design --

    Tweets:
        Dictionary: [userId] -> deque([timer, tweetId])

    Followers:
        Dictionary: [userId] -> set([userId])

    Timer:
        Iterator
    """

    def __init__(self):
        self.timer = itertools.count(step=-1)  # -1 for min heap
        self.tweets = defaultdict(deque)  # [followee] -> deque([(timestamp, tweetId)])
        self.followees = defaultdict(set)  # [followee] -> set([followers])

    def postTweet(self, userId, tweetId):
        """
        Time: O(1)
        """
        self.tweets[userId].appendleft((next(self.timer), tweetId))

    def getNewsFeed(self, userId):
        """
        Time: O(log n)
        """
        joined_followers = self.followees[userId] | {userId}
        joined_tweets = (self.tweets[u] for u in joined_followers)  # lazy generator
        tweets = heapq.merge(*joined_tweets)  # lazy generator
        top_10 = [
            tweetId for _, tweetId in heapq.nsmallest(10, tweets)
        ]  # force eval top 10
        return top_10

    def follow(self, followerId, followeeId):
        """
        Time: O(1)
        """
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Time: O(1)
        """
        self.followees[followerId].discard(followeeId)
