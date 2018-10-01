words = raw_input('Input a string please: ')
a, e, i, o, u = 0, 0, 0, 0, 0
for chr in words:
  if chr == 'a':
    a += 1
  elif chr == 'e':
    e += 1
  elif chr == 'i':
    i += 1
  elif chr == 'o':
    o += 1
  elif chr == 'u':
    u += 1
print "There are %d vowels in the input string. And they are %d a, %d e, %d i, %d o, %d u." % (a+e+i+o+u, a, e, i, o, u)
