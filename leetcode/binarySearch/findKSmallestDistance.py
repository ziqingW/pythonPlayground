# Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.

# Example 1:
# Input:
# nums = [1,3,1]
# k = 1
# Output: 0 
# Explanation:
# Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1st smallest distance pair is (1,1), and its distance is 0.

#  Must remember this and review it time by time !!!!!
class Solution:
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        low, hi = 0, nums[-1]-nums[0]
        while low <= hi:
            mid = (low+hi)//2
            count = 0
            j = 0
            for i in range(len(nums)):
                while j < len(nums) and nums[j] - nums[i] <= mid:
                    j += 1
                count += j - i - 1
            if count < k:
                low = mid + 1
            else:
                hi = mid - 1
        return low