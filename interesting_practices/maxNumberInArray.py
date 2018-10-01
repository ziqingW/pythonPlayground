# In a given length array [n](len = n), do the following operations in array:[a, b , c]
# then the slot in array n start from ath to bth will be added value of c
# Give the output what the max value in slot in the array

def maxSlotinArray(n, queries):
    arr = [0] * (n+1)
    for query in queries:
        [start, end, addon] = query
        arr[start-1] += addon
        arr[end] -= addon
    maxNum = addNum = 0
    for num in arr:
        addNum += num
        if addNum > maxNum:
            maxNum = addNum
    return maxNum
    
# Big O is O(n)
    