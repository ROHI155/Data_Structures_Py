class Solution(object):
    def isPalindrome(self, s):
        l,r = 0,len(s)-1 # Assigning the left pointer as 0 and right as last index s-1.
        while l<r: # Check l is lesser than r.
            while l<r and not s[l].isalnum(): # Check the value of left and the right is alphanumeric.
                l+=1 # Then increment the pointer by 1.
            while l<r and not s[r].isalnum(): # Check the value of the right is alphanumeric.
                r-=1 # Decrement the pointer by 1.
            if s[l].lower() != s[r].lower(): # Check if the left value is not equal to the right value.
                return False # True means return false.
            l+=1 # Increment and decrement the pointers by 1.
            r-=1
        return True # At the end return true.
