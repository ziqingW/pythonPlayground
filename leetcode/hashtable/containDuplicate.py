class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash = set()
        for num in nums:
            if num not in hash:
                hash.add(num)
            else:
                return True
        return False