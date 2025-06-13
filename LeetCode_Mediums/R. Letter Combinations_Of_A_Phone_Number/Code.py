class Solution(object):
    def letterCombinations(self, digits):
        Letters = { 
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    } # Creating a dictionary of all the necessary mappings of nums and letters.
        if not digits: return [] # Check if the digits is empty and return the empty list.
        result = [""] # Create a empty list to store the values.

        for d in digits: # Iterate through each elements in the digits.
            temp =[] # Create a temporary list to store values.
            for l in Letters[d]: # Iterate through the created letters corresponding to the digits.
                for r in result: # A loop to store the results.
                    temp.append(r+l) # Adding the each combinations of letters to previous stored combinations.
            result = temp # Assigning the temp to result. 
        return result # Returning the result.