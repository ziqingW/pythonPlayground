# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = {}
        for i,char in enumerate(s):
            if char not in result:
                result[char] = i
            else:
                result[char] = None
        result = [result[char] for char in result if result[char]!=None]
        if result:
            return min(result)
        return -1