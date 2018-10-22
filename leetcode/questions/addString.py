# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

# Note:

# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.


# it was accepted, although very slow
class Solution:
    
    def calculate(self, s):
        nums = [0,1,2,3,4,5,6,7,8,9]
        result = 0
        for i in range(len(s)):
            digit = nums[int(s[i])]*(10**(len(s)-i-1))
            result += digit
        return result
            
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = self.calculate(num1)
        num2 = self.calculate(num2)
        return str(num1 + num2)
            
        
        