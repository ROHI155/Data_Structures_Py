class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = [] #Overall List for all rows.
        for i in range(len(image)): # Iterate through the number of values in image.
            res = [] # Stores the each row for each iteration.
            for j in range(len(image[i])-1,-1,-1): # To pick the element from the reverse order.
                if image[i][j] == 1: # If the [i][j] are equals to 1 means then append 1 else o.
                    res.append(0)
                else:
                    res.append(1)
            result.append(res) # Append the list to the main list which contains the result of all rows.
        return result # Return the result.