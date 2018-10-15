# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        nums = [str(num) for num in range(1,10)]
        for k in range(9):
            hashmapRow = {}
            row = ("").join(board[k]).replace(".", "")
            for i,char in enumerate(row):
                if char not in nums or char in hashmapRow:
                    return False
                hashmapRow[char] = i
            column = [row[k] for row in board]
            hashmapCol = {}
            column = ("").join(column).replace(".", "")
            for i,char in enumerate(column):
                if char not in nums or char in hashmapCol:
                    return False
                hashmapCol[char] = i           
            hashmapBlock = {}
            j = k // 3
            l = k % 3
            block = [board[x][y] for x in range(j*3, 3*(j+1)) for y in range(3*l,3*(l+1))]
            block = ("").join(block).replace(".", "")
            for i, char in enumerate(block):
                if char not in nums or char in hashmapBlock:
                    return False
                hashmapBlock[char] = i
        return True
            