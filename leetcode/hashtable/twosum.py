# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        result = {}
        for i, num in enumerate(nums):
            if num not in result:
                result[num] = i
            else:
                if type(result[num]) == int:
                    result[num] = [result[num], i]    
                result[num].append(i)
            other = target - num
            if other in result:
                if type(result[other]) == list:
                    return [result[other][0], result[other][1]]
                else:
                    if result[other] != i:
                        return sorted([i, result[other]])