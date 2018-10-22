# The count-and-say sequence is the sequence of integers with the first five terms as following:

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.

# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

# Note: Each term of the sequence of integers will be represented as a string.

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        elif n == 2:
            return "11"
        else:
            previous = self.countAndSay(n-1)
            i = 1
            count = 1
            counter_total = 0
            char = previous[0]
            result = ""
            while i < len(previous):
                if previous[i] == previous[i-1]:
                    count += 1
                    i += 1
                else:
                    result += str(count) + char
                    count = 1
                    counter_total += count
                    char = previous[i]
                    i += 1
            if counter_total < len(previous):
                result += str(count) + char
            return result