def mortCalculate():
  while True:
    try:
      r = float(raw_input("How much is your mortgage's rate? >>"))
    except:
      print "Incorrect format, input once again please."
    else:
      break
    
  while True:
    try:
      p = int(raw_input("How much is your total principal? >>"))
    except:
      print "Incorrect format, input once again please."
    else:
      break 

  option = ""
  while not (option == "m" or option == "w" or option == "d"):
    option = raw_input("How do you plan to pay your mortgage, monthly, weekly or daily? Choose from m, w or d. >>")
  while True:
    try:
      n = int(raw_input("How many years does your mortgage last? >>"))
    except:
      print "Incorrect format, input once again please."
    else:
      break
  if option == "m":
    n = n * 12
    r = r/ 12 / 100
  elif option == "w":
    n = n * 365 / 7
    r = r/ (365/7) / 100
  else:
    r = r/ 365 / 100
    n = n * 365
  if r == 0:
    c = p / (n * 1.0)
  else:
    c = r * p / (1 - (1+ r) ** (-n))
  
  print "Your each payment would be $%.2f/%s." % (c, option)
  
mortCalculate()