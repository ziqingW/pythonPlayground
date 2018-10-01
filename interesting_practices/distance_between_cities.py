import re

def address(x):
  city = raw_input("What's the name of the %s city? >>" % x)
  while True:
    coor = raw_input("What's the coordination of the %s city? >>" % x)
    if re.search("^\([0-9]", coor) and re.search("\)$", coor):
      addr = tuple(float(s) for s in coor[1:-1].split(","))
      break
    else:
      print "Wrong format for coordination, try again."
      continue
  print "The coordination of %s is %r." % (city, addr)
  return addr
  
def distance():
  x1, y1 = address("first")
  x2, y2 = address("second")
  distance = float((abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** 0.5)
  print "The distance between these two cities is %.2f." % distance
  
distance()

      