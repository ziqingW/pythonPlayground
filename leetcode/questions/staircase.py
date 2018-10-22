# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

# Example 1:

# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # a recursive but slow method
        # if n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # else:
        #     return self.climbStairs(n-1) + self.climbStairs(n-2)
        
        # since it is a fibroncci list, Xn = Xn-1+ Xn-2, then:
        a,b = 1,2
        if n == 1:
            return a
        elif n == 2:
            return b
        else:
            for i in range(3, n+1):
                a, b = b, a+b
            return b