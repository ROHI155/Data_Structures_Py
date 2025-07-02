class Solution(object):
    def isPalindrome(self, x):
        if x < 0: return False # If the x is lesser then 0 returning false
        org = x # Assign the org as x.
        rev = 0 # Assign the rev as 0.
        while x > 0: # A loop to perform calculations iteratively
            digit = x % 10 # The x is modulus with the 10 and stored in digit.
            rev = rev * 10 + digit # Performing the rev.
            x = x // 10 
        if org == rev: return True # If the org matches with the rev return true.
        else: return False # Else returning false.