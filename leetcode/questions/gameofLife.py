# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

# Example:

# Input: 
# [
#   [0,1,0],
#   [0,0,1],
#   [1,1,1],
#   [0,0,0]
# ]
# Output: 
# [
#   [0,0,0],
#   [1,0,1],
#   [0,1,1],
#   [0,1,0]
# ]

class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        results = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                result = 0
                if i - 1 >= 0:
                    if j - 1 >= 0:
                        result += board[i-1][j-1]
                    if j+1 < len(board[0]):
                        result += board[i-1][j+1]
                    result += board[i-1][j]
                if j - 1 >= 0:
                    result += board[i][j-1]
                if j + 1 < len(board[0]):
                    result += board[i][j+1]
                if i + 1 < len(board):
                    if j - 1 >= 0:
                        result += board[i+1][j-1]
                    if j+1 < len(board[0]):
                        result += board[i+1][j+1]
                    result += board[i+1][j]
                results.append(result)
        k = 0
        while k < len(results):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == 1:
                        if results[k] < 2 or results[k] > 3:
                            board[i][j] = 0
                    else:
                        if results[k] == 3:
                            board[i][j] = 1
                    k += 1
                    
                