from collections import deque
    
class RecentCounter(object):

    def __init__(self):
        self.requests = deque()

    def ping(self, t):
        self.requests.append(t)
        #only save request that happen in the last 3000s, which is in range[t-3000,t]: means any request that happen before t - 3000, we will delete any requests that has request time < t -3000)
        while self.requests and self.requests[0] < t - 3000: 
            self.requests.popleft()
        #return the number of requests that happens in range[t-3000,t]
        return len(self.requests)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)