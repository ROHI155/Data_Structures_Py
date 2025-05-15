class Solution:
    def trap(self, height: List[int]) -> int:
        # Here we are using the two pointer to find the maximum.
        l = 0  # Assigning the left most value index.
        r = len(height)-1 # Assigning the rightmost indexed value.
        max_l = height[l] # Assigning the particular value of the left pointer index's value.
        max_r = height[r] # Assigning the particular value of the right pointer index's value.
        total = 0 # Initialy the total is considered as 0.
# Checking while the value of left is lesser then the right then it executes accordingly.
        while l < r: 
            if height[l]<height[r]: # Checking the particular value of the left is lesser then the right. 
                max_l = max (height[l],max_l) # Then picking the max among the height[l] and max[l].
                total += max_l - height[l] # Then subtracting the total value with the difference of max_l  and the height[l].
                l += 1 # Increementing the pointer of left by one.
            elif height == 0: # If the height is 0 then return 0.
                return 0
            else : # Then l > r or l == r means executing the right side of the block.
                max_r = max (height[r],max_r) # Picking and assigning max value by comparing the height [r] and max [r].
                total += max_r - height[r] # then the total is summed with the difference of the max_r and height[r].
                r -= 1 # Then assign the decrement to the right pointer because it is starting fromt the right most end.
        return total  # Return the total value.