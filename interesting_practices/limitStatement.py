from __future__ import division
from math import *
import re

def limiteval():
  while True:
    expr = raw_input("Enter the function(in terms of x):")
    if re.search("[^0-9\+\-\*/x]", expr):
      print "Wrong format, check again."
    else:
      break
  while True:
    try:
      x = int(raw_input("Enter the limit value of x:"))
    except:
      print "Number only, please."
    else:
      break
  try:
    result = eval(expr)
  except ZeroDivisionError:
    print "The limit statement value is infinity."
  else:
    print "The limit statement value is %r." % result
limiteval()