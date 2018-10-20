# Implement int sqrt(int x).

# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        left = 1
        right = x
        while left <= right:
            mean = (left+right)//2
            if mean*mean > x:
                right = mean - 1
            else:
                if (mean+1)*(mean+1) > x:
                    return mean
                left = mean + 1
        
        
        
        