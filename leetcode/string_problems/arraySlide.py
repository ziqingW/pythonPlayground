# Given an array of n positive integers and a positive integer s, 
# find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.
def arrSlide(s, nums):
    total = 0
    left = 0
    result = len(nums) + 1
    for right, num in enumerate(nums):
        total += num
        while total >= s:
            result = min(result, right - left + 1)
            total -= nums[left]
            left += 1
    return result if result <= len(nums) else 0
    
print(arrSlide(7, [2,3,4,2,5,6,4,3,1,6]))