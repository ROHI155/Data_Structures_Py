class Solution(object):
    def rotate(self, matrix):
        n = len(matrix) # Storing the length of the matrix in n.
        matrix.reverse() # Reversing the entire matrix using the reverse function.
        for r in range(n): # For iterating through each rows.
            for c in range(r): # For iterating through each columns.
                matrix[r][c],matrix[c][r] = matrix[c][r],matrix[r][c] # Swaping the elements in the matrix.
        return matrix # Return the matrix.