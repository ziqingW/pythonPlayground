def bubble_sort(l):
  while True:
    sorted = 0
    for i in range(len(l) - 1):
      if l[i] > l[i+1]:
        large = l[i]
        small = l[i+1]
        l[i] = small
        l[i+1] = large
        sorted += 1
    #    print l
    if sorted == 0:
      break
    else:
      continue
  print l