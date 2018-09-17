# start by picking up a median number from "median of three"- the midian value among the first, last and the middle numbers
def quickSort(arr):
    less = []
    more = []
    pivots = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = sorted([arr[0], arr[-1], arr[len(arr)//2]])[1]
        for num in arr:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                more.append(num)
            else:
                pivots.append(num)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivots + more
    
print(quickSort([2,5,33,32,10,6,9,43,103,54,74]))