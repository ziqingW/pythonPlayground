def tileCost():
  while True:
    try:
      w = int(raw_input("How wide is the floor plan? >>"))
      h = int(raw_input("What's length of the floor plan? >>"))
      n = float(raw_input("How much is the price for tile per sqft? >>"))
    except:
      print "Sorry, I cannot understand you. Please input again."
    else:
      print "The total cost for the floor plan is $%r." % (w*h*n)
      break
      

tileCost()