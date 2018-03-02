import math

def digite():
  while True:
    try:
      n = int(raw_input("Please input a number for e's accurency: "))
    except:
      print "Incorrect input, please give a number."
      continue
    else:
      break
  print round(math.e, n)
  
digite()
