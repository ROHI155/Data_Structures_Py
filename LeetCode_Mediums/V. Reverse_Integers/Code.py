class Solution(object):
    def reverse(self, x):
        is_negative = x < 0 # Assigning the negative values.
        x = abs(x) # Assigning the absolute value of x and store it in x.
        rev_num = 0 # Inituially assigning the rev_num as 0.
        while x > 0: # Executes the following when the x is greater then 0.
            rev_num = rev_num * 10 + x % 10 # Performing calculation and stores each remainder as rev_num.
            x //= 10 # Performing the floor div on x. 
        if is_negative: # If the rev_num is negative then assign the negative of rev_num.
            rev_num = -rev_num
        if rev_num < -2**31 or rev_num > 2**31 - 1:  # Instead of 2**31
            return 0
        return rev_num # Return the reverse num.