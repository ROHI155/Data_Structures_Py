class Solution(object):
    def isSubsequence(self, s, t):
        j = 0 # Assign the j as o.
        if s == '': return True # Return True if the s is empty.
        # if s>t: return False # Return False if the s is greater then t.
        for i in range(len(t)):# Iterate through each element in the list of strings.
            if t[i] == s[j]: # Check if the value if t is equals to s.
                if j == len(s)-1: # Then check if the j is equals to the lenght of s-1.
                    return True # Returning True.
                j += 1 # Increment the j by plus 1.
        return False # Else, Return False.