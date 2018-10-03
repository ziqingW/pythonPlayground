# Given a binary array, find the maximum number of consecutive 1s in this array.

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        maximum = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                k += 1
                if maximum < k:
                    maximum = k
            else:
                k = 0
        return maximum
