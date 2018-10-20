# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mean = (left+right)//2
            if nums[mean] == target:
                return mean
            elif nums[left] <= nums[mean]: # left is sorted, no pivot point 
                if nums[left] <= target <= nums[mean]: # check if target in left part
                    right = mean - 1 # if yes, continue check the left half
                else:
                    left = mean + 1 # else, check the right part
            else: # there is a pivot point at the left half, then 
                if nums[mean] <= target <= nums[right]: # the right half is sorted without pivot point
                    left = mean + 1 # check if target in right part
                else:
                    right = mean - 1 # or, check the left half
        return -1
        