# Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. 
# If target exists, then return its index, otherwise return -1.

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mean = (left + right)//2
            mean_val = nums[mean]
            if mean_val < target:
                left = mean + 1
            elif mean_val > target:
                right = mean - 1
            else:
                return mean
        return -1
            
        