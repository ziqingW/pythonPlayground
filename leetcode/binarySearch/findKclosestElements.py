# Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

# Example 1:
# Input: [1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]
# Example 2:
# Input: [1,2,3,4,5], k=4, x=-1
# Output: [1,2,3,4]
import bisect   # use bisect to simplify the search 
class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        left = right = bisect.bisect_left(arr, x)   # use bisect module to find out the insert point
        while right - left < k: 
            if left == 0:                   # if the insertion is at the leftend, return arr[:k]
                return arr[:k]
            elif right == len(arr):         # if the insertion is at the rightend, or when the right reaches the right end, return arr[-k:]
                return arr[-k:]
            elif x - arr[left-1] <= arr[right] - x:  # else, if the left difference is smaller than the right difference, go left
                left -= 1
            right += 1          # or go right
        return arr[left, right]