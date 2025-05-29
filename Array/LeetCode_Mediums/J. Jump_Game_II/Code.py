class Solution:
    def jump(self, nums: List[int]) -> int:
        left = 0 # Using the two pointer method and assigning the left and right pointer as 0.
        right = 0
        res = 0 # Assigning the result as 0.
        while right < len(nums)-1: # Opening a loop to perform iteration
            max = 0 
            for i in range(left,right+1): # Iterating through each element in the list.
                if nums[i]+i > max: # If, max is lesser than nums[i]+[i] means store the max as nums[i]+[i].
                    max = i + nums[i]
            left = right + 1 # Increment and assign the pointers.
            right = max
            res += 1
        return res # Return result at the end