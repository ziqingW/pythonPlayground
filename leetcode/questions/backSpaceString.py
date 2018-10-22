# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

# Example 1:

# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:

# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:

# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:

# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".

class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s = ""
        count_1 = 0
        for i in range(len(S)):
            if S[i] != "#":
                if count_1 != 0:
                    s = s[:-count_1]
                    count_1 = 0
                s += S[i]
            else:
                count_1 += 1
        if count_1 != 0:
            s = s[:-count_1]
            
        t = ""
        count_2 = 0
        for j in range(len(T)):
            if T[j] != "#":
                if count_2 != 0:
                    t = t[:-count_2]
                    count_2 = 0
                t += T[j]
            else:
                count_2 += 1
        if count_2 != 0:
            t = t[:-count_2]
        return s == t
            