
  
def merge_sort(l):
# merge two sorted list to be a new sorted list using the augment of a tuple with two lists 
#Attentions! All the lists of the augment must be sorted already.
  def merge(targetList):
    m, n = targetList
    ml = len(m)
    nl = len(n)
    sortedList = []
    mIndex = 0
    nIndex = 0
# compare the numbers of two list one by one, put the smaller one into the newly defined list
    while mIndex < ml and nIndex < nl:
      if m[mIndex] < n[nIndex]:
        sortedList.append(m[mIndex])
        mIndex += 1
      else:
        sortedList.append(n[nIndex])
        nIndex += 1
# if one of the list is run out of the length, add the rest of the other list into the newly defined sorted list
    if mIndex == ml:
      sortedList += n[nIndex:]
    if nIndex == nl:
      sortedList += m[mIndex:]
    return sortedList

 
# split the rootlist to be a list with a series of dimer-list, plus the single sub-list if there is.
# Then merge these sub-lists to sort by call merge().
  def splitMerge(l):
    temporMergeList = []
    lengthSplitList = len(l)
    if lengthSplitList % 2 != 0:
      for j in range(0, lengthSplitList - 1, 2):
        temporMergeList.append(merge((l[j], l[j+1])))
      temporMergeList.append(l[-1])
    else:
      for j in range(0, lengthSplitList, 2):
        temporMergeList.append(merge((l[j], l[j+1])))
# if there is only one list in the result, return it, that's the final result;
# or, callback the recursive splitMerge() 
    if len(temporMergeList) > 1:
      return splitMerge(temporMergeList)
    else:
      return temporMergeList

# split the original list to be a list of list items concluding a single element.      
  rootSplitList = []
  for i in range(0, len(l)):
    rootSplitList.append([l[i]])
  result = splitMerge(rootSplitList)[0]
  return result

print merge_sort([7, 13, 1,313,5663,31,6,313,89,3,3213,31456,778,433,235,235,897,65,43,900,76,43])


  

  
  