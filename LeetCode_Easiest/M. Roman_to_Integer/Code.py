class Solution(object):
    def romanToInt(self, s):
        d = { 'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000} # Storing the symbols and values as key value pairs.
        length = len(s) # Storing the length of the 's'.
        i = 0 # Assigning the i and result as 0.
        result = 0
        while i<length: # Loop for performing the calculation and iteration through each element.
            if i<length-1 and d[s[i]] < d[s[i+1]]: # Check if the i+1 is lesser than i.
                result += d[s[i+1]] - d[s[i]] # True means difference the values and store it in the result.
                i += 2 # Here we need to increment the pointer to 2 values because we are checking the i and i + 1 th element.
            else: # Else increment the element and i.
                result += d[s[i]]
                i += 1
        return result # Return the result.