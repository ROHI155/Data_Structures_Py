class Solution(object):
    def intToRoman(self, num):
        d = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),(100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),(10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')] # Speciffying all the symbols and the values.
        result = "" # Intially assigning the result as empty.
        for value,symbol in d: # Iterating therough each value of d.
            while value <= num: # Check if the value is lesser then the nums.
                result += symbol # Update the symbols in the result.
                num -= value # Reduce the nums.
        return result # Return the result.