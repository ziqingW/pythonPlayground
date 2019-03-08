# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
#

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        results = []
        if length > 0:
            nums = set(nums)
            for n in range(1, 1+length):
                if n not in nums:
                    results.append(n)
        return results
        
