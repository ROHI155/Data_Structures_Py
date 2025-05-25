class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        r = max(sum(i) for i in accounts) # Summing the list values and then storing it in the r with the maximum values through iterating the accounts 
        return r # Returning the r 