# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# The array may contain duplicates.


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left,right = 0, len(nums)-1
        while left < right:
            mid = (left+right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] == nums[right]:
                if nums[left] == nums[mid]:
                    if len(set(nums[left:mid+1])) == 1:
                        left = mid + 1
                    elif len(set(nums[mid+1: right+1])) == 1:
                        right = mid
                else:
                    right = mid
            else:
                right = mid
        return nums[left]
        # return min(nums)
                    
                