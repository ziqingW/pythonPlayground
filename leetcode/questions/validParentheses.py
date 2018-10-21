# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# method 1
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        dict_par = collections.defaultdict(int)
        new = []
        for char in s:
            if char == "(":
                dict_par["a"] += 1
                new.append("a")
            elif char == ")":
                dict_par["a"] -= 1
                if dict_par["a"] < 0:
                    return False
                if new.pop() != "a":
                    return False
            elif char == "[":
                dict_par["b"] += 1
                new.append("b")
            elif char == "]":
                dict_par["b"] -= 1
                if dict_par["b"] < 0:
                    return False
                if new.pop() != "b":
                    return False
            elif char == "{":
                dict_par["c"] += 1
                new.append ("c")
            elif char == "}":
                dict_par["c"] -= 1
                if dict_par["c"] < 0:
                    return False
                if new.pop() != "c":
                    return False
        for key in dict_par:
            if dict_par[key] != 0:
                return False
        return True
 
# method 2       
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        result = []
        for char in s:
            if char == "(":
                result.append("a")
            elif char == ")":
                if result:
                    if result.pop() != "a":
                        return False
                else:
                    return False
            elif char == "[":
                result.append("b")
            elif char == "]":
                if result:
                    if result.pop() != "b":
                        return False
                else:
                    return False
            elif char == "{":
                result.append ("c")
            elif char == "}":
                if result:
                    if result.pop() != "c":
                        return False
                else:
                    return False
        return len(result) == 0