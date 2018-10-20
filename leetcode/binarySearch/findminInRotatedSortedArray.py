# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# You may assume no duplicate exists in the array.

# Example 1:

# Input: [3,4,5,1,2] 
# Output: 1
# Example 2:

# Input: [4,5,6,7,0,1,2]
# Output: 0

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1 # left should be the minimum if there's not a pivot point
        while left < right:
            m = (left+right) // 2
            if nums[m] > nums[right]: # there's a pivot point at the left half, and the minimum is at the right half
                left = m + 1
            else:           # there may be a pivot point at the left half, however, the minimum is at the left half
                right = m
        return nums[left]
                