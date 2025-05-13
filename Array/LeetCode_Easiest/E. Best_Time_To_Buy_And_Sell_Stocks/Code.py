class Solution:
    def maxProfit(self, prices): # Here we are using the Two pointer method
        left = 0 
        right = 1
        max = 0
        while right<len(prices):
            if prices[right]>prices[left]:
                profit = prices[right] - prices[left]
                if profit>max:
                    max = profit
            else:
                left = right
            right += 1
        return max