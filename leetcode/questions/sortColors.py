# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note: You are not suppose to use the library's sort function for this problem.
#
# Example:
#
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = {
            0: 0,
            1: 0,
            2: 0
        }
        for num in nums:
            counter[num] += 1
        nums[:counter[0]] = [0] * counter[0]
        nums[counter[0]:counter[0]+counter[1]] = [1] * counter[1]
        nums[counter[0]+counter[1]:] = [2] * counter[2]
