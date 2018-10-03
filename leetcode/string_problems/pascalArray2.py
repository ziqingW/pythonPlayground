# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

# Note that the row index starts from 0.
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if 0 <= rowIndex <= 1:
            return [1] * (rowIndex+1)
        elif rowIndex > 1:
            result = [1,1]
            for i in range(2, rowIndex+1):
                newRow = [1] * (i+1)
                j = 1
                while j < i:
                    newRow[j] = result[j-1] + result[j]
                    j += 1
                result = newRow[:]
        return result