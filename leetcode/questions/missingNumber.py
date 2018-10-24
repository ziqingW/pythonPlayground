# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# Example 1:

# Input: [3,0,1]
# Output: 2
# Example 2:

# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        else:
            mini = maxi = total = nums[0]
            for i in range(1, len(nums)):
                mini = min(mini, nums[i])
                maxi = max(maxi, nums[i])
                total += nums[i]
            other = int((mini+maxi)*(maxi-mini+1)/2) -total
            if other == 0:
                if mini == 0: 
                    return maxi + 1
                return mini - 1
            return other