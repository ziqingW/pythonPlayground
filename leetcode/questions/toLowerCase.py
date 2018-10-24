# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

 

# Example 1:

# Input: "Hello"
# Output: "hello"
# Example 2:

# Input: "here"
# Output: "here"

class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        S = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        s = "abcdefghijklmnopqrstuvwxyz"
        d = dict(zip(S,s))
        result = ""
        for char in str:
            if char in d:
                result += d[char]
            else:
                result += char
        return result