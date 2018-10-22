# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

# Example 1:

# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    # first use recursive method
        # if len(nums) == 0:
        #     return 0
        # elif len(nums) == 1:
        #     return nums[0]
        # else:
        #     n = len(nums) - 1
        #     return max(rob(nums[:n-1])+nums[n], rob(nums[:n]))
    
    # then use memo to run the recursive
        # memo = [-1]*(len(nums)+1)
        # return dp(nums)
            
        #     def dp(nums):
        #         if len(nums) == 0:
        #             return 0
        #         elif len(nums) == 1:
        #             return nums[0]
        #         else:
        #             for i in range(2, len(nums)+1):
        #                 if memo[i] >= 0:
        #                     return memo[i]
        #                 result = max(dp(nums[:i-1])+nums[i], dp(nums[:i]))
        #                 memo[i] = result
        #                 return result
        
        
        
        
    # DP method, with memo,
    #   if len(nums) == 0:
    #       return 0
    #   memo = [-1] * (len(nums)+1)
    #   memo[0] = 0
    #   memo[1] = nums[0]
    #   for i in range(2, len(nums)+1):
    #      best = max(memo[i-2]+nums[i-1], memo[i-1])
    #      memo[i] = best
    #   return memo[len(nums)]
    
    # it looks like the fibronacci number, so we can use variables to replace the memo
        if len(nums) == 0: return 0
        a = b = 0
        for num in nums:
            a, b = b, max(num + a, b)
        return b
