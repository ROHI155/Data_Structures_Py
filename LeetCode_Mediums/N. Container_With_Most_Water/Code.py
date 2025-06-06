class Solution(object):
    def maxArea(self, height):
        max_area = 0 # Assign the max_area as 0 Initially.
        n = len(height) # Assign the n as length of the height.
        l , r = 0, n-1 # Assign the left and the right pointer.
        while l<r: # Check the left pointer is lesser then the right pointer.
            Width = r - l # Calculate the width and the height from the values of left and right pointer.
            Height = min(height[l],height[r])
            Area = Width * Height # Using the width and height calculate and store the value of area.
            max_area = max(max_area,Area) # Compare maximum of max-area and area and store it in max_area.
            if height [l]<height[r]: # Check with the value of left is lesser then right then increment the left pointer.
                l += 1
            else: # Else Decrement the right pointer.
                r -= 1
        return max_area # At last return the max_area.