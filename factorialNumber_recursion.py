def facto(num):
  if num == 1:
    return num
  elif num == 0:
    return 1
  else:
    return num * facto(num - 1)

while True:
  try:
    n = int(raw_input("Please input a positive integer. >>"))
  except:
    print "Wrong format, input again."
  else:
    if n < 0:
      print "The number must be greater than zero."
    else:
      break
print "The factorial number of %d is %d." % (n, facto(n))