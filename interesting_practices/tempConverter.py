from __future__ import division

def tempF(num):
  f = (num * 9/5) + 32
  return f
  
def tempC(num):
  c = (num - 32) * 5/9
  return c

def converter():
  answer = ""
  while not (answer == "f" or answer == "c"):
    answer = raw_input("Which unit of temperature you have? \nChoose f or c. >>")
  if answer == "f":
    while True:
      try:
        n = int(raw_input("What's the temperature? >>"))
      except:
        print "Wrong format, please input again."
      else:
        print "It's %dF. And it equals to %dC." % (n, tempC(n))
        break
  else:
    while True:
      try:
        n = int(raw_input("What's the temperature? >>"))
      except:
        print "Wrong format, please input again."
      else:
        print "It's %dC. And it equals to %dF." % (n, tempF(n))
        break
  converter()

converter()