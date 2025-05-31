class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort() # Sorting the given list.
        i = 0 # Assigning the i as 0.
        while i < len(nums): # Loop to iterate through each element in the list.
            if nums[i] == val: # Check if the element is equal to the val.
                nums.pop(i) # If true means pop the element.
            else: # Else increment the i.
                i += 1
        return len(nums) # At the end return the length of nums.