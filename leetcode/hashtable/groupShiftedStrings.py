# Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

# Example:

# Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
# Output: 
# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]

class Solution:
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for text in strings:
            k = ("").join([alphabet[ord(char)-ord(text[0]) if ord(char)-ord(text[0]) >= 0 else ord(char)-ord(text[0]) + 26] for char in text])
            if k in hashmap:
                hashmap[k].append(text)
            else:
                hashmap[k] = [text]
        result = []
        for key in hashmap:
            result.append(hashmap[key])
        return result
        
            