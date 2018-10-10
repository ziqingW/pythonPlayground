# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        for char in strs:
            newChar = ("").join(sorted(char))
            if newChar in hashmap:
                hashmap[newChar].append(char)
            else:
                hashmap[newChar] = [char]
        result = []
        for key in hashmap:
            result.append(hashmap[key])
        return result