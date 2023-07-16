import heapq
import time

class Twitter:

    def __init__(self):
        self.user_follower_dict = {}
        self.user_posts_dict = {}
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        ts = time.time()
        self.user_posts_dict[userId] = list(self.user_posts_dict.get(userId, []) + [[ts, tweetId]])

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.user_follower_dict.get(userId, [])
        posts = list(self.user_posts_dict.get(userId, []))
        for followee in followees:
#             print("followee", followee, self.user_posts_dict[followee])
            posts += list(self.user_posts_dict.get(followee, []))
#         print("posts ", posts)

        heapq._heapify_max(posts)
        result = []
        for i in range(min(10, len(posts))):
#             print("post post", self.user_posts_dict)
            result.append(heapq._heappop_max(posts)[1])
        
        return result
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        print(self.user_posts_dict)
        if self.user_follower_dict.get(followerId, None):
            self.user_follower_dict[followerId].add(followeeId)
        else:
            self.user_follower_dict[followerId] = set([followeeId])
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.user_follower_dict.get(followerId, None):
            self.user_follower_dict[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
