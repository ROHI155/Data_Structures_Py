class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for col in range(len(matrix)-1):
            for row in range(len(matrix[0])-1):
                if matrix[col][row] != matrix[col+1][row+1]:
                    return False
        return True