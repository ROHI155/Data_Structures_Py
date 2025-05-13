class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0 # Assigning the i pointer as 0.
        for j in range(len(nums)): # Declaraing the j as the len of nums as a range.
            if nums[j] != 0: # Checking the j is not equals to 0.   
                nums [j],nums[i] = nums [i],nums[j] # Swaping the values.
                i += 1 # Then increments the value of i.