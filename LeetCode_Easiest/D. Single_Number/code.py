class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {} # Intializing a empty dict to store the values
        for i in nums: # For updating the each elements in 'i'
            if i not in d: # if the element is not present in the 'd' (dict) means update the count and register the element
                d[i] = 1 # Setting the count to the corresponding element
            else: # Else the element already present means delete the element
                del d[i]
        return list(d.keys())[0] # Return only the keys as list 
        # Here we need to return the 0th index because the dict contains only one element only