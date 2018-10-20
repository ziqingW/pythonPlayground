# A peak element is an element that is greater than its neighbors.

# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

# You may imagine that nums[-1] = nums[n] = -∞.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5 
# Explanation: Your function can return either index number 1 where the peak element is 2, 
#              or index number 5 where the peak element is 6.

class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) -1
        if len(nums) == 1: # if only one number, return 0
            return 0
        while left <= right:
            mid = (left+right)//2
            if mid == len(nums) - 1: # since nums[-1] = -inf, nums[0] > nums[-1] always True, so don't need to 
                return mid          # consider the edge issue for index 0. However, when the mid reach the last
            else:                   # number, return it as the peak
                if nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid]:
                    return mid      # if mid is larger than its flank numbers, return it
                elif nums[mid] < nums[mid+1]:
                    left = mid + 1  # if mid is in a ascending slope, go right
                elif nums[mid] < nums[mid-1]: # else if mid is in a descending slope, go left
                    right = mid - 1