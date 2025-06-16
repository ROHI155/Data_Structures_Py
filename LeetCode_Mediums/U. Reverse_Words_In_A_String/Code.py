class Solution(object):
    def reverseWords(self, s):
        s = s.split() # Splitting the given strings.
        s.reverse() # Reversing the entire strings.
        return ' '.join(s) # Return the reversed strings without extra spaces.
        