# In a given integer array nums, there is always exactly one largest element.

# Find whether the largest element in the array is at least twice as much as every other number in the array.

# If it is, return the index of the largest element, otherwise return -1.


class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = nums.index(max(nums))
        new_nums = nums[:i] + nums[i+1:]
        if len(new_nums) > 0:
            newMax = max(new_nums)
            if newMax == 0:
                return i
            else:
                if max(nums)/newMax >= 2:
                    return i
                else:
                    return -1
        else:
            return i
            
