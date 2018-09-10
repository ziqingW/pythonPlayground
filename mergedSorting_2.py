def mergeSorting(arr):
    if len(arr) <= 1:
        return arr
    median = len(arr) // 2
    left = arr[:median]
    right = arr[median:]
    dividedLeft = mergeSorting(left)
    dividedRight = mergeSorting(right)
    return sortTwo(dividedLeft, dividedRight)
        
def sortTwo(left, right):
    result = []
    leftIndex = rightIndex = 0
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] <= right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1
    if left:
        result.extend(left[leftIndex:])
    if right:
        result.extend(right[rightIndex:])
    return result