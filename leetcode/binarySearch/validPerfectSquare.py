# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.

class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right= 1, num
        while left <= right:
            mid = (left+right)//2
            if mid**2 == num:
                return True
            elif mid**2<num:
                left = mid + 1
            else:
                right = mid - 1
        return False