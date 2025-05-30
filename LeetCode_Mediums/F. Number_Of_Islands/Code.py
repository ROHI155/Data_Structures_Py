class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row ,cols = len(grid),len(grid[0]) # Assigning the len of rows and cols.
        nums_Islands = 0 # Assigning the nums_Islands as 0.
        # Creating a function to mark the Islands as 0 using dfs.
        def dfs(i,j):
            if i < 0 or i >= row  or j < 0 or j >= cols or grid[i][j] != '1': # Check the condition i will be in the range of 0 to rows and similarly for cols and then the grid value not equals to 1 means return.
                return 
            else: # Else executes means the grid value contains the '1', So we are makring it as '0'.
                grid[i][j] = '0' # Here it converts the all '1' as '0' in all directions.
                dfs(i + 1,j)  # Row wise.
                dfs(i - 1,j)
                dfs(i,j + 1)  # Column wise.
                dfs(i,j - 1)
        for i in range(row): # Iterating through the row.
            for j in range(cols): # Iterating through cols.
                if grid [i][j] == '1': # If the gird value is '1' means increment the nums_Islands as plus 1.
                    nums_Islands += 1
                    dfs(i,j) # Here for marking all the neighbor one as '0'.
        return nums_Islands # returning the nums_Islands.