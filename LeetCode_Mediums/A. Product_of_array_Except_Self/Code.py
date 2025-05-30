class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final_list = [1]*len(nums) # Initializing a list with inserting with '1' with the length of nums.
        prefix = 1 # Assigning the prefix and suffix as 1.
        suffix = 1
        for i in range(len(nums)): # iterating throuh the for loop for calc of prefix.
            final_list[i]=prefix # assigning the final is equals to the prefix value.
            prefix = prefix*nums[i] # Performing calc of prefix value with index of nums
        for j in range(len(nums)-1,-1,-1): # Iterating through the for loop for calc of suffix. 
            final_list[j]=final_list[j]*suffix # Updating the list through multiplying the list with the suffix value.
            suffix =suffix*nums[j] 
        return final_list # Return the list at the end of the for loop.