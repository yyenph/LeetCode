class Solution(object):
    def maxProfit(self, prices):
        maxprofit = 0
        left = 0
        right = 1
        
        while right < len(prices) :
            if prices[left] < prices[right]:
                maxprofit = max(maxprofit, (prices[right] - prices[left]))
                print(prices[left],prices[left],maxprofit)
            else:
                left = right
            right = right + 1
        return maxprofit





