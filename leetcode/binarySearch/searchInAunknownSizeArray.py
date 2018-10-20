# Given an integer array sorted in ascending order, write a function to search target in nums.  If target exists, then return its index, otherwise return -1. However, the array size is unknown to you. 
# You may only access the array using an ArrayReader interface, where ArrayReader.get(k) returns the element of the array at index k (0-indexed).

# You may assume all integers in the array are less than 10000, 
# and if you access the array out of bounds, ArrayReader.get will return 2147483647.
# You may assume that all elements in the array are unique.
# The value of each element in the array will be in the range [-9999, 9999].

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        left, right = 0, 19998
        while left <= right:
            mid = (left+right) // 2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) == 2147483647:
                right = mid - 1
            else:
                if reader.get(mid) < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1