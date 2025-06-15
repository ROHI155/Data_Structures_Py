class Solution(object):
    def maxProfit(self, prices):
        profit = 0 # Initially assign the profit as 0.
        for i in range(1,len(prices)): # for iterate through each values in the list.
            if prices[i] > prices[i-1]: # Check the prices of current i and previous i is greater or not.
                profit += prices[i] - prices[i-1] # Then sum the profit with the difference of the current and the previous prices.
        return profit # Return profit.