class Solution(object):
    def convert(self, s, numRows):
        if numRows <= 1 or len(s) <= 1 or numRows >= len(s): # Returning the s if the given range is 0.
            return s
        i = 0 # Assigning the i and a and rows with its perspectives.
        a = 1
        rows =[[] for _ in range(numRows)]
        for c in s: # For iterate through each element in the s.
            rows[i].append(c) # appending the i in c.
            if i == 0: # If the i is equals to 0 means assign the a equals to 1.
                a = 1
            elif i == numRows - 1: # check the is is equal to the numRows - 1 then assign the d as negative 1.
                a = -1
            i += a # Increment the i.
        
        ret = '' # Creaing the empty list.
        for i in range(numRows): # for joining the element in the ret.
            ret += ''.join(rows[i])
        return ret # Returning the ret.