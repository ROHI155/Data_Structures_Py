class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = 0 # Assign the start and max length and the character index as 0.
        max_len = 0
        char_ind = {} 
        for i,c in enumerate (s): # Open a for loop to iterate through each element in the s.
            if c in char_ind and char_ind[c] >= start: # Check the c in char_ind and greater than equal to the start.
                start = char_ind[c]+1 # Update the start with the updation of char_ind plus 1.
            char_ind[c] = i # Assign the char_ind of c as i.
            max_len = max(max_len, i - start + 1) # Obtain the maximum length as max of max_len and i differenced with the start plus 1.
        return max_len # Return the maximum length.