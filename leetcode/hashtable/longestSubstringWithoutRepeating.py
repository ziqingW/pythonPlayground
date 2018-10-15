# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        i = j = maximum = 0 
        counter = collections.defaultdict(int)
        while j < len(s):       
            if s[j] not in counter:
                counter[s[j]] = j
                length = j - i + 1
                if length >= maximum:
                    maximum = length 
            else:
                head = counter[s[j]] + 1
                for x in range(i, counter[s[j]]+1):
                    del counter[s[x]]
                i = head
                counter[s[j]] = j
            j += 1
        return maximum
