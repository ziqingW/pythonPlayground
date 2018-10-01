def collatz():
  while True:
    try:
      n = int(raw_input("Enter a number to start:"))
    except:
      print "Number only, thanks."
    else:
      if n < 1:
        print "The number must be greater than 1."
      else:
        break
  steps = 0
  origin = n
  while n != 1:
    if n % 2 == 0:
      n /= 2
      steps += 1
    else:
      n = n * 3 + 1
      steps += 1
  print "It takes %d steps for %d to reach one." % (steps, origin)
  
collatz()