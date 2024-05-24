'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

 

Example 1:

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

 

Constraints:

    board.length == 9
    board[i].length == 9
    board[i][j] is a digit 1-9 or '.'.


'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def get_block(row, col):
            return [
                [board[row-1][col-1],board[row-1][col],board[row-1][col+1]],
                [board[ row ][col-1],board[ row ][col],board[ row ][col+1]],
                [board[row+1][col-1],board[row+1][col],board[row+1][col+1]],
            ]
        def get_col(board, col_idx):
            col = []
            for row in board:
                col.append(row[col_idx])
            return col

        def valid_row(row, value):
            return row.count(value) < 2

        def valid_col(col,value):
            return col.count(value) < 2

        def valid_block(block, value):
            total = 0
            for row in block:
                total += row.count(value)
            return total < 2

        
        for row_idx, row in enumerate(board):
            for col_idx, value in enumerate(row):
                if value == '.':
                    continue
                if not valid_row(row, value):
                    return False
                col = get_col(board, col_idx)
                if not valid_col(col, value):
                    return False

                for trow in range(3):
                    row_idx = (3*trow)+1
                    for tcol in range(3):
                        col_idx = (3*tcol)+1
                        block = get_block(col_idx, row_idx)
                        if not valid_block(block, value):
                            return False
        return True
