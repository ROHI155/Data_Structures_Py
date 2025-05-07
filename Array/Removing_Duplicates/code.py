class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1 # Left Pointer
        for right in range(1,len(nums)): # For loop fixed in right pointer increments the index and until the end of the nums
            if nums[right]!=nums[right-1]: # Checks if the val.right is equal to the val.right - 1
                nums[left]=nums[right] # Assignns the val.left equals to the val.right
                left +=1 # Increments the left pointer and the right pointer will automatically increases
        return left # Return the left pointer at the end of the for loop only. 