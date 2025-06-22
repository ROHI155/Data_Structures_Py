class Solution(object):
    def searchMatrix(self, matrix, target):
        r = 0 # Assigning the row and column as 0 and length of the matrix.
        c = len(matrix[0]) - 1
        while r <= len(matrix) - 1  and c >= 0: # A loop to iterate through each element in the list.
            if target == matrix[r][c]: # Check if the target is equals to matric of r and c.
                return True # Then return True.
            elif target < matrix[r][c]: # else increment the row and column.
                c -= 1
            else:
                r += 1
        return False  # aReturn False at the end of the loop.