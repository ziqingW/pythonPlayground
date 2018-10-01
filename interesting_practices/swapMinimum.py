# find out the minimum times of swap to sort a unordered array of numbers to ascendent ordered
def minimumSwaps(arr):
  result = 0
  sortedArr = sorted(arr)
  arrTable = {elem:i for (i ,elem) in enumerate(arr)}
  for i in range(len(arr)):
    testValue = arr[i]
    endValue = sortedArr[i]
    if testValue != endValue:
      swapPosition = arrTable[endValue]  
      arr[swapPosition] = testValue
      arr[i] = endValue
      arrTable[testValue] = swapPosition
      arrTable[endValue] = i
      result += 1
  print(result)

minimumSwaps([1,3,5,2,4,6,8])