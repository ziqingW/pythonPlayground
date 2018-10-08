class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        len1 = len(set1)
        len2 = len(set2)
        if len2 < len1:
            set1, set2 = set2, set1
        return [num for num in set1 if num in set2]
                