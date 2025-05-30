class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l,output = 0,0 # Initializes two variables for the left pointer and the output as 0.
        
        for r,n in enumerate (nums): # Here we are enumerating the index of lists to the right pointer and n.
            if n==0: # Check if the n is equals to 0.
                l=r+1 # Update the left index value.
            output = max(output,r-l+1) # Store the max consecutive number count.
        return output # Return the output at the end of the for loop.