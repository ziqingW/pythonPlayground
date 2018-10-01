def factorial():
  facto = 1
  while True:
    try:
      num = int(raw_input("Please input a positive integer. >>"))
    except:
      print "Incorrect format, input again."
    else:
      if num < 0:
        print "The number must be greater than zero."
      else:
        break
  if num == 0:
    return facto
  else:
    facto = 1
    for i in range(1, num + 1):
      facto *= i
    return facto
    
print "The factorial number is %d." % factorial()