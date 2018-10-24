# Given an integer array, find three numbers whose product is maximum and output the maximum product.

# Example 1:
# Input: [1,2,3]
# Output: 6
# Example 2:
# Input: [1,2,3,4]
# Output: 24
# Note:
# The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
# Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.


class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1, max2, max3, min1, min2 = float("-Inf"),float("-Inf"),float("-Inf"),float("Inf"),float("Inf")
        for num in nums:
            if num >= max1:
                max1, max2, max3 = num, max1, max2
            elif num >= max2:
                max2, max3 = num, max2
            elif num >= max3:
                max3 = num
            if num <= min1:
                min1, min2 = num, min1
            elif num <= min2:
                min2 = num
        return max(max1*max2*max3, max1*min1*min2)
