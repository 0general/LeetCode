from collections import deque

class Twitter:

    def __init__(self):
        self.t_time = 0
        self.following = [[False]*501 for _ in range(501)]
        self.feed = [deque() for _ in range(501)]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed[userId].append((self.t_time,tweetId))
        self.t_time -= 1
        if len(self.feed[userId]) > 10:
            self.feed[userId].popleft()
        
    def getNewsFeed(self, userId: int) -> List[int]:
        h = list(self.feed[userId])
        for i in range(501):
            if self.following[userId][i]:
                h.extend(list(self.feed[i]))
        h.sort(key = lambda x : x[0])
        ans = []
        for i in range(len(h)):
            if i >= 10:
                break
            ans.append(h[i][1])
        return ans
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId][followeeId] = True
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId][followeeId] = False
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)