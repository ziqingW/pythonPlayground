# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = []
        i = 0
        while i < len(s):
            if s[i] == "I":
                if i < len(s) - 1:
                    if s[i+1] == "V":
                        result.append(4)
                        i += 2
                    elif s[i+1] == "X":
                        result.append(9)
                        i += 2
                    else:
                        result.append(1)
                        i += 1
                else:
                    result.append(1)
                    i += 1
            elif s[i] == "V":
                result.append(5)
                i += 1
            elif s[i] == "X":
                if i < len(s) - 1:
                    if s[i+1] == "L":
                        result.append(40)
                        i += 2
                    elif s[i+1] == "C":
                        result.append(90)
                        i += 2
                    else:
                        result.append(10)
                        i += 1
                else:
                    result.append(10)
                    i += 1
            elif s[i] == "L":
                result.append(50)
                i += 1
            elif s[i] == "C":
                if i < len(s) - 1:
                    if s[i+1] == "D":
                        result.append(400)
                        i += 2
                    elif s[i+1] == "M":
                        result.append(900)
                        i += 2
                    else:
                        result.append(100)
                        i += 1
                else:
                    result.append(100)
                    i += 1
            elif s[i] == "D":
                result.append(500)
                i += 1
            else:
                result.append(1000)
                i += 1
        return sum(result)