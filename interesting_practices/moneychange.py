from __future__ import division
import math

def moneyChange():
  while True:
    try:
      cost = float(raw_input("How much is the cost? >>"))
    except:
      print "That's not a correct number, try again."
    else:
      break
  while True:
    try:
      pay = float(raw_input("How much will you pay for it? >>"))
    except:
      print "That's not a correct number, try again."
    else:
      break
  
  change = pay - cost
  diff = abs(change)
  dollar = int(math.floor(diff))
  diff = int(round((diff - dollar) * 100))
  quarter = math.floor(diff / 25)
  dime = math.floor((diff % 25) / 10)
  nickel = diff - 25 * quarter - 10 * dime

  
  if change < 0:
    print "That's not enough, you owe the seller %d dollar, %d quarter, %d dime and %d nickels." % (dollar, quarter, dime, nickel)
  if change == 0:
    print "Exact money, thank you!"
  if change > 0:
    print "Here's the change: %d dollar, %d quarter, %d dime and %d nickels. Thank you." % (dollar, quarter, dime, nickel)
    
moneyChange()