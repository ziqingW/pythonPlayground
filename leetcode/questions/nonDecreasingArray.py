# Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums1 = nums[:]
        nums2 = nums[:]
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums1[i] = nums[i+1]
                nums2[i+1] = nums[i]
                break
        return sorted(nums1) == nums1 or sorted(nums2) == nums2
                    
                    