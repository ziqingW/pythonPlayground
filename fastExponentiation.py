def fast_exponent():
  a = int(raw_input("Enter a number for power:"))
  b = int(raw_input("Enter a number as power:"))
  c = int(raw_input("Enter a number to modulo:"))
  x = pow(a,b,c)
  print "%d to the power of %d modulos %d equals to %d." % (a, b, c, x)
  
fast_exponent()