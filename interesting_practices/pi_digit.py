import math

def digitpi():
  while True:
    try:
      n = int(raw_input("Please input a number for pi's accurency: "))
    except:
      print "Incorrect input, please give a number."
      continue
    else:
      break
  print round(math.pi, n)
  
digitpi()