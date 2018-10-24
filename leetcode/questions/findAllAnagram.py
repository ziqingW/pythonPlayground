# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

# Example 1:

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

import collections
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) == 0:
            return []
        len_p = len(p)
        sample_counter = collections.Counter(p)
        test_counter = collections.Counter(s[:len_p-1])
        result = []
        for i in range(len_p-1, len(s)):
            test_counter[s[i]] += 1
            if sample_counter == test_counter:
                result.append(i-len_p+1)
            test_counter[s[i-len_p+1]] -= 1
            if test_counter[s[i-len_p+1]] == 0:
                del test_counter[s[i-len_p+1]]
        return result