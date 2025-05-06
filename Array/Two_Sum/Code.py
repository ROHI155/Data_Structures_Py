class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range (0,len(nums)):
            val = nums[i]
            diff = target - val
            if val not in dict: # if the values are new to dict is 
                dict[diff] = i
            else: # If the values are already stored in the dict means
                cur_val = i  # Current Index value
                prev_val = dict[val] # Previous index value
                return [cur_val,prev_val] # i should retun the answer in an order.