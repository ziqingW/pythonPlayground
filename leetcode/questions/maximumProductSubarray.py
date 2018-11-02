# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

# Example 1:

# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum, mini, maxi = nums[0], nums[0], nums[0]
        for i in range(1,len(nums)):
            if nums[i] < 0:
                mini, maxi = maxi, mini
            maxi = max(maxi*nums[i], nums[i])
            mini = min(mini*nums[i], nums[i])
            maximum = max(maximum, maxi)
        return maximum
        