# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        results = ""
        if len(strs) > 0:
            strs = sorted(strs, key=lambda x: len(x))
            for i in range(len(strs[0])):
                if len(set(text[:i+1] for text in strs)) == 1:
                    results = strs[0][:i+1]
        return results
        
        # optimized method: without sort
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lcp = ""
        if strs:
            for i in range(len(strs[0])):
                try:
                    group = set([string[i] for string in strs])
                except:
                    return lcp
                else:
                    if len(group) == 1:
                        lcp += strs[0][i]
                    else:
                        return lcp
        return lcp
            
            