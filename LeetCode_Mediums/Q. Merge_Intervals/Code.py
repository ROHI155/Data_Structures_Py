class Solution(object):
    def merge(self, intervals):
        out = []
        for i in sorted(intervals, key = lambda i:i[0]): # This loop sorts the intervals based on the 0th element of every set.
            if out and i[0] <= out[-1][1]: # Check the out is not empty and the ith value is lesser then or equal to the previous value means executes the following.
                out[-1][1] = max(out[-1][1],i[1]) # Update the out with the maximum of the out of previous values and the current values.
            else: # If the out is empty means append the values.
                out.append(i)
        return out # Return the out.

        