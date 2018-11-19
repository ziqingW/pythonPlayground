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


# another method
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def helper(nums):
            counter = {}
            for num in nums:
                if num != ".":
                    try:
                        num = int(num)
                    except:
                        return False
                    else:
                        if 1 <= num <= 9:
                            if num not in counter:
                                counter[num] = True
                            else:
                                return False
                        else:
                            return False
            return True
        
        for row in board:
            if not helper(row):
                return False
        columns = [[row[i] for row in board] for i in range(9)]
        for column in columns:
            if not helper(column):
                return False
        subboxes = [board[i][j:j+3]+board[i+1][j:j+3]+board[i+2][j:j+3] for j in range(0,7,3) for i in range(0,7,3)]
        for subbox in subboxes:
            if not helper(subbox):
                return False
        return True
        # for k in range(9):
        #     if not helper(board[k]):
        #         return False
        #     if not helper([row[k] for row in board]):
        #         return False
        #     i = k // 3
        #     j = k % 3
        #     subbox = board[i*3][j*3:j*3+3]+board[i*3+1][j*3:j*3+3]+board[i*3+2][j*3:j*3+3]
        #     if not helper(subbox):
        #         return False
        # return True
            