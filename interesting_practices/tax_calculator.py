def taxCalcu():
  while True:
    try:
      cost = float(raw_input("How much is the cost? >>"))
    except:
      print "That's not right, input again."
    else:
      break
  while True:
    try:
      tax = float(raw_input("How much is the tax? >>"))
    except:
      print "That's not right, input again."
    else:
      break
  cost = cost * (100 + tax)/100
  print "The final cost is $%.2f. Thank you." % cost

taxCalcu()