# Binary Search Based Solution

# Imagine we split an array into m different sub-arrays. There can be several ways to do this split. Let us assume we take one possible split.
# In this particular split, we take the sum of each subarray j and call it S(j) where j is from 1 to m. Then we figure out the sub-array which has the maximum sum from all of these m different sums and call it max_sum(array, m).
# What is the least possible value of max_sum(array, m)? Answer will be max(array) - this must be obvious. The max(array) value must be in one of the m sub-arrays. The least possible amongst all possible m different sub-arrays would be a sub-array with a single element as the max(array).
# What is the maximum possible value of max_sum(array, m)? Answer will be sum(array) - a subarray with all elements.
# So the range of max_sum(array, m) is max(array) to sum(array).
# We now have a search problem - we need to search within the range max(array) to sum(array) such that we find the minimum value in this range with which we can form at-most m sub-arrays such no sub-array has sum more than this value. To efficiently search a sorted range we use binary search.
# Imagine we pick a value mid and find that we could make more sub-arrays than m. This means we picked too small value (check the code to understand this). We should set low = mid + 1.
# Imagine we pick a value mid and find we could make less sub-arrays than m. Now we can easily split those sub-arrays to increase the count and still make sure that the maximum sum of those sub-arrays is less than mid (splitting will only decrease mid). In this case, we record a potential solution and make high = mid-1, hoping to get an even better solution later.
# Lets use an example: [7,2,5,10,8] and 2
# max_sum([7,2,5,10,8], 2) will be in the range [10, 32] - i.e. any split of the array into 2 sub-array will have sum of the sub-array between [10, 32].
# Now we want to find the minimum value in this range with which we can form 2 sub-arrays. Lets do this linearly. Can we use 10? Using 10, we can form [7, 2]; [5]; [10]; [8] - 4 subarrays. We clearly need to increase the minimum value so that we can reduce from 4 subarrays.
# What if we used binary search and started with mid = (10+32)/2 = 21. This gives us [7,2,5]; [10,8] - This is valid solution. Can we do better? We record 21 and reduce our range to [10, 20].
# This gives us mid as 15. [7,2,5]; [10]; [8] - Invalid! we got more than 2 sub-arrays. We need to increase low to mid+1 and search in the range [16, 20].
# [16, 20] gives us 18. [7,2,5]; [10,8] - This is a valid solution. Can we do better than 18? Let us search in the range [16,17]
# [16,17] gives mid as 16. [7,2,5]; [10]; [8]. This is invalid and we need to increase range. New range is [17,17]. This again gives [7,2,5]; [10]; [8] and we get the new range as [18,17].
# [18,17] breaks the while loop! We have recorded 18 as the last answer and return it.


class Solution(object):
    def is_valid(self, nums, m, mid):
        # assume mid is < max(nums)
        cuts, curr_sum  = 0, 0
        for x in nums:
            curr_sum += x
            if curr_sum > mid:
                cuts, curr_sum = cuts+1, x
        subs = cuts + 1
        return (subs <= m)
    
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        low, high, ans = max(nums), sum(nums), -1
        while low <= high:
            mid = (low+high)//2
            if self.is_valid(nums, m, mid): # can you make at-most m sub-arrays with maximum sum atmost mid 
                ans, high = mid, mid-1
            else:
                low = mid + 1
        return ans