class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r = []
        top , bottom = 0, len(matrix)-1
        left, right =  0, len(matrix[0])-1

        while top<=bottom and left<=right:
            for col in range(left,right+1):
                r.append(matrix[top][col])
            top += 1
            for row in range(top,bottom+1):
                r.append(matrix[row][right])
            right -= 1
            if top<= bottom:
                for col in range(right,left-1,-1):
                    r.append(matrix[bottom][col])
                bottom -= 1
            if left<= right:
                for row in range(bottom,top-1,-1):
                    r.append(matrix[row][left])
                left += 1
        return r