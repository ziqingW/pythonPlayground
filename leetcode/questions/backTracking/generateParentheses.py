# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def makeParentheses(temp, pos, n, opened, closed):
            if closed == n:
                results.append(temp)
                return
            if opened < n:
                temp[pos] = "("
                makeParentheses(temp, pos+1, n, opened+1, closed)
            if closed < opened:
                temp[pos] = ")"
                makeParentheses(temp, pos+1, n, opened, closed+1)

        template = [""]*2*n
        results = []
        makeParentheses(template, 0, n, 0, 0)
        return results
