from __future__ import division
import re

def bintodec(num):
  result = 0
  num = str(num)
  for i in range(len(num)):
    digit = int(num[i]) * 2 ** (len(num) - 1 - i)
    result += digit
  print "The binary number %s equal to decimal number %d." % (num, result)

def dectobin(num):
  result = ""
  l = 1
  n = num
  m = num
  while True:
    n = n / 2
    if n >= 1:
      l += 1
      continue
    else:
      break
  for i in range(l):
    x = num - 2 ** (l - 1 - i)
    if x >= 0:
      result = result + "1"
      num = x
    else:
      result = result + "0"
  print "The decimal number %d equal to binary number %s." % (m, result)
  
def converter():
  print ""
  answer = ""
  while not (answer == "1" or answer == "2"):
    answer = raw_input("Which convert do you want to use? \n1. Binary to decimal \n2. Decimal to binary \nChoose 1 or 2 >>>")
  if answer == "1":
    while True:
      try:
        number = int(raw_input("Please input the binary number >>>"))
        test = str(number)
      except:
        print "Incorrect format, input again."
      else:
        if re.search('[2-9]', test):
          print "Incorrect format, input again."
          continue
        else:
          break
    bintodec(number)
  else:
    while True:
      try:
        number = int(raw_input("Please input the decimal number >>>"))
      except:
        print "Incorrect format, input again."
      else:
        break
    dectobin(number)
  converter()
  
converter()
    