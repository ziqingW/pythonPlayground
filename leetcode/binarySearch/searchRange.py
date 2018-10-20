# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def search(left, right):
            if nums[left] == target == nums[right]: # if target is the whole range of left and right 
                return [left, right]        # return the range immediately
            elif nums[left] <= target <= nums[right]:  # if target is among the range, split the range and search half
                mid = (left+right) // 2
                l, r = search(left, mid), search(mid+1, right) 
                return max(l,r) if -1 in l+r else [l[0], r[1]]  # because the return value are only [-1,-1] or [a,b] which covers the target
            return [-1, -1]     # value completely, choose the list which is not [-1,-1]. Or if both of the results are not [-1,-1], combine them
        
        if len(nums) == 0:
            return [-1, -1]
        return search(0, len(nums)-1)