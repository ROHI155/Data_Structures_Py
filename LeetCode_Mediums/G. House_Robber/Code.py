class Solution:
    def rob(self, nums: List[int]) -> int:
        r1 = 0 # Assign the r1 and r2 as 0 initially.
        r2 = 0
        for vals in nums: # Iterate through each values in nums
            res = max(vals + r1,r2) # Store the max of calc performed using the vals + r1 or r2. Varies upon max values.
            r1 = r2 # Storing the r2 in the r1.
            r2 = res # Storing the res to r2.
        return res # Returning the res or r2.