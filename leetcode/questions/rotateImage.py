# You are given an n x n 2D matrix representing an image.

# Rotate the image by 90 degrees (clockwise).

# Note:

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Example 1:

# Given input matrix = 
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],

# rotate the input matrix in-place such that it becomes:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        k = 0
        t = len(matrix)
        while t > 1:            
            for i in range(t-1):
                # pos1 = matrix[k][i+k]
                # pos2 = matrix[i+k][len(matrix)-1-k]
                # pos3 = matrix[len(matrix)-1-k][len(matrix)-1-i-k]
                # pos4 = matrix[len(matrix)-1-i-k][k]
                # matrix[k][i+k] = pos4
                # matrix[i+k][len(matrix)-1-k] = pos1
                # matrix[len(matrix)-1-k][len(matrix)-1-i-k] = pos2
                # matrix[len(matrix)-1-i-k][k] = pos3
                matrix[k][i+k], matrix[i+k][len(matrix)-1-k], matrix[len(matrix)-1-k][len(matrix)-1-i-k], matrix[len(matrix)-1-i-k][k] = matrix[len(matrix)-1-i-k][k], matrix[k][i+k], matrix[i+k][len(matrix)-1-k], matrix[len(matrix)-1-k][len(matrix)-1-i-k]
            k += 1
            t = len(matrix) - k*2
        
                