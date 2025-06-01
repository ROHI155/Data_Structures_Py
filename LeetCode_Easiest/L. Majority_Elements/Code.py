class Solution(object):
    def majorityElement(self, nums):
        max_cnt = 0  # Initializing the max and major as 0.
        major = nums[0] 
        for i in nums: # Loop to iterate through each element in the list.
            if max_cnt == 0: # Checking the numsis greater than max.
                major = i # Store the major as value of nums.
            max_cnt += (1 if i == major else -1) #Incrementing the count base on condition.
        return major # Return nums.
      