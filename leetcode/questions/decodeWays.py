# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.

# Example 1:

# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:

# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = []
        k = 2
        template = s[0]
        if int(template) == 0:
            return 0
        else:
            dp = [1,1]
        while 2 <= k <= len(s):
            new = s[k-1]
            template += new
            if int(new) == 0:
                if 0 < int(template[-2:]) <= 20:
                    dp.append(dp[-2])
                else:
                    return 0
            else:
                if 0 < int(template[-2:]) <= 26 and str(int(template[-2:])) == template[-2:]:
                    dp.append(dp[-1]+dp[-2])
                else:
                    dp.append(dp[-1])
            k += 1
        return dp[len(s)]
        