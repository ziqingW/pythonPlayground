# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:

# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
# Example:

# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

# Output: [1,2,2,3,5,6]

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if n != 0:
            for i in range(len(nums1) - m):
                nums1.pop()
            for num in nums2:
                nums1.append(num)
            nums1.sort()
            
#  another method, faster than the previous one
        copy = nums1[:m]
        i = j = k = 0
        while i < m and j < n:
            if copy[i] < nums2[j]:
                nums1[k] = copy[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        if i == m and j != n:
            for x in range(j, n):
                nums1[k] = nums2[x]
                k += 1
        if j == n and i != m:
            for y in range(i, m):
                nums1[k] = copy[y]
                k += 1