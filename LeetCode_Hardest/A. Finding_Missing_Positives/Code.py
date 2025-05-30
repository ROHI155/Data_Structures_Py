class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        missing = 1 # Here we are assigning the missing as 1 and it increements in future loops.
        sort =  sorted(set(nums)) # Method used for sorting the arrays.
        print(sort)  # Printing it for reference purposes.
        for i in range(len(sort)): # Entering into a loop which uses the sorted array and increements i as index values.
            if (sort [i] > 0): # Condition to move out from the negative values.
                if(sort [i] == missing): # If the indexed element is equal to missing means. 
                    missing += 1  # Increments the missing values and leave.
                else: # Else break the loop.
                    break
        return missing # At the end of the array return the missing.