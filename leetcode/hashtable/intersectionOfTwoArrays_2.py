# Given two arrays, write a function to compute their intersection.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]

from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        len1 = len(nums1)
        len2 = len(nums2)
        if len2 < len1:
            nums1, nums2 = nums2, nums1
        cnt1 = Counter()
        cnt2 = Counter()
        for num in nums1:
            cnt1[num] += 1
        for num in nums2:
            cnt2[num] += 1
        result = []
        for k in cnt1:
            if k in cnt2:
                result += [k]*min([cnt1[k], cnt2[k]])
        return result
                
        
            