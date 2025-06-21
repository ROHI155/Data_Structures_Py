class Solution(object):
    def maxDistance(self, s, k):
        result = 0 # Assign the result as 0.
        x = y = 0 # Assign the x and y axis as 0.
        for i , v in enumerate(s): # Using this loop iterate through each element in the s.
            if v == 'N': y += 1 # If v is equals to 'N' increment y by one.
            elif v == 'S': y -= 1 # If v is equals to 'S' decrement y by one.
            elif v == 'E': x += 1 # If v is equals to 'E' increment x by one.
            elif v == 'W': x -= 1 # If v is equals to 'W' decrement x by one.
            temp = abs(x) + abs(y) # Add the adbsolute values of x and y.
            result = max(result , (min(temp + 2*k , i + 1))) # From this obtain the max values by comparing  the result and minimum of the calculated values.
        return result # Returns the result.