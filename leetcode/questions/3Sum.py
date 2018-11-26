# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        results = {}
        for i in range(len(nums)-2):
            a = nums[i]
            start = i + 1
            end = len(nums)-1
            while start < end:
                b, c = nums[start], nums[end]
                if a + b + c == 0:
                    if (a,b,c) not in results:
                        results[(a,b,c)] = True
                        start += 1
                        end -= 1
                elif a + b + c > 0:
                    end -= 1
                else:
                    start += 1
        return [list(result) for result in results]