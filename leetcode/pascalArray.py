# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
class Solution:
    def generate(self, n):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        elif n == 1:
            results = [[1]]
        elif n == 2:
            results = [[1], [1,1]]
        elif n > 2:
            results = [[1], [1,1]]
            for i in range(3, n+1):
                newArray = [1]*i
                for j in range(1, i-1):
                    newArray[j] = results[-1][j-1] + results[-1][j]
                results.append(newArray)
        return results