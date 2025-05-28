class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = len(nums)-1 # Assigning the res as the length of nums.
        for i in range(len(nums)-2,-1,-1): # Open a for loop and list the range of len(nums) which needs to decrement till the last value.
            if nums[i] + i >= res: # If the sum of nums[i]+i is greater then or equal to the res means assign the res = i.
                res = i
        if res == 0: # In the outside of the loop check if the res equals to 0 means return True.
            return True
        else: # Else return false. 
            return False

        