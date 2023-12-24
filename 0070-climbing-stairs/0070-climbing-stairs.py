class Solution(object):
    def climbStairs(self, n):
        # n=3 [0,1,2,3]
        one, two = 1,1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one
        