import re
import copy

class Complex(object):
  def __init__(self, num):
    self.a, self.b = num
    
  def showComplex(self):
    if self.b >= 0:
      return "%.2f+%.2fi" % (self.a, self.b)
    else:
      return "%.2f-%.2fi" % (self.a, abs(self.b))
  
  def negation(self):
    self.a = self.a * (-1)
    self.b = self.b * (-1)
  
  def inversion(self):
    m = (self.a) ** 2 + (self.b) ** 2
    self.a = self.a * 1.0/ m
    self.b = self.b * (-1.0) / m

def complexAlgebra():
  def complexAdd(num1, num2):
    x = num1.a + num2.a
    y = num1.b + num2.b
    z = Complex((x,y))
    return z
  
  def complexMulti(num1, num2):
    x = num1.a * num2.a - num1.b * num2.b
    y = num1.b * num2.a + num1.a * num2.b
    z = Complex((x,y))
    return z

  regex = "\([0-9.]+,[0-9.]+\)"
  while True:
    n1 = raw_input("What is the first complex number? In tuple format: >>")
    if not re.search(regex, n1):
      print "That's wrong format, input it as (x,y)."
      continue
    else:
      break
  c1 = tuple(float(s) for s in n1[1:-1].split(","))
  c1 = Complex(c1)
  print "The first complex number is %s." % c1.showComplex()
  
  while True:
    n2 = raw_input("What is the second complex number? In tuple format: >>")
    if not re.search(regex, n2):
      print "That's wrong format, input it as (x,y)."
      continue
    else:
      break
  c2 = tuple(float(s) for s in n2[1:-1].split(","))
  c2 = Complex(c2)
  print "The second complex number is %s." % c2.showComplex()
  c2Copy = copy.copy(c2)
  
  answer = ""
  while not (answer == "1" or answer == "2" or answer == "3" or answer == "4"):
    answer = raw_input("Which operation do you want to do?\n\t1.Add\n\t2.Subtraction\n\t3.Multiplication\n\t4.Division\nChoose 1~4. >>")
  if answer == "1":
    complexAdd(c1, c2)
    print "The addition result of {0} and {1} is {2}.".format(c1.showComplex(), c2.showComplex(), complexAdd(c1, c2).showComplex())
  elif answer == "2":
    c2.negation()
    complexAdd(c1, c2)
    print "The subtraction result of {0} from {1} is {2}.".format(c2Copy.showComplex(), c1.showComplex(), complexAdd(c1, c2).showComplex())
  elif answer == "3":
    complexMulti(c1, c2)
    print "The multiplication result of {0} and {1} is {2}.".format(c1.showComplex(), c2.showComplex(), complexMulti(c1, c2).showComplex())
  else:
    c2.inversion()
    complexMulti(c1, c2)
    print "The division result of {0} from {1} is {2}.".format(c2Copy.showComplex(), c1.showComplex(), complexMulti(c1, c2).showComplex())

complexAlgebra()