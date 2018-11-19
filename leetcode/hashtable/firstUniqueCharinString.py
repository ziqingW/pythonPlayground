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
        
        
        # another method
        # counter = {}
        # counter['single'] = {}
        # for i, char in enumerate(s):
        #     if char not in counter:
        #         counter[char] = True
        #         counter['single'][char] = i
        #     else:
        #         if char in counter['single']:
        #             del counter['single'][char]
        # singles = counter['single'].values()
        # if len(singles) > 0:
        #     return min(singles)
        # return -1