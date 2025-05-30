class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board) # Assigning the total row value from the board using len.
        col = len(board[0]) # Assigning the total colums from the board using len.
        P = len(word) # Taking the total length of the word.
        # Function to pass through the board and then mark the visited indexes.
        def soln (r,c,pos): # Here we are using the three variables r,c and pos.
            if (pos >= P): # Checking if the pos is greater than the p means return all as true.
                return True
            # Condition that checks the r and c range and the letter of [r][c] is equals to [pos] means exeutes the following.
            if( 0 <= r < row and 0 <= c < col and board[r][c] == word[pos]):
                original = board[r][c] # Marking the visited as '#'.
                board[r][c] = '#'
                # Here the found is used to check the all directions in the board.
                found = (soln(r - 1,c,pos + 1) or
                        soln(r + 1,c,pos + 1) or
                        soln(r,c - 1,pos + 1) or
                        soln(r,c + 1,pos + 1))
                board[r][c] = original # if not found means backtracks to normal again.
                return found
            return False # If the letter was not found means return as False.
        for r in range(row): # Iterate through rows.
            for c in range(col): # Iterate through cols.
                if soln(r,c,0): # if found at first means return true.
                    return True
        return False # At then end return false if no letter matches in the board.