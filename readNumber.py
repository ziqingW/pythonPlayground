def numName():
 
  def readnum(n):
    minus = False
    if int(n) == 0:
      return "zero"
    elif int(n) < 0:
      minus = True
      n = n[1:]
    lent = len(n)
    ncopy = n[::-1]
    nlist = []
    for i in ncopy:
      if int(i) == 1:
        p = "one"
      elif int(i) == 2:
        p = "two"
      elif int(i) == 3:
        p = "three"
      elif int(i) == 4:
        p = "four"
      elif int(i) == 5:
        p = "five"
      elif int(i) == 6:
        p = "six"
      elif int(i) == 7:
        p = "seven"
      elif int(i) == 8:
        p = "eight"
      elif int(i) == 9:
        p = "nine"
      else:
        p = ""
      nlist.append(p)
    if lent >= 2:
      for i in range(1, lent, 3):
        if nlist[i] != "one" and nlist[i] != "":
          if nlist[i] == "two":
            nlist[i] = "twenty"
          elif nlist[i] == "three":
            nlist[i] = "thirty"
          elif nlist[i] == "four":
            nlist[i] = "fourty"
          elif nlist[i] == "five":
            nlist[i] = "fifty"
          elif nlist[i] == "six":
            nlist[i] = "sixty"
          elif nlist[i] == "seven":
            nlist[i] = "seventy"
          elif nlist[i] == "eight":
            nlist[i] = "eighty"
          elif nlist[i] == "nine":
            nlist[i] = "ninty"
          if nlist[i-1] != "":      
            nlist[i-1] = nlist[i] + "-" + nlist[i-1]
            nlist[i] = ""
        if nlist[i] == "one":
          nlist[i] = ""
          if nlist[i-1] == "":
            nlist[i-1] = "ten"
          elif nlist[i-1] == "one":
            nlist[i-1] = "eleven"
          elif nlist[i-1] == "two":
            nlist[i-1] = "twelve"
          elif nlist[i-1] == "three":
            nlist[i-1] = "thirteen"
          elif nlist[i-1] == "four":
            nlist[i-1] = "fourteen"
          elif nlist[i-1] == "five":
            nlist[i-1] = "fifteen"
          elif nlist[i-1] == "six":
            nlist[i-1] = "sixteen"
          elif nlist[i-1] == "seven":
            nlist[i-1] = "seventeen"
          elif nlist[i-1] == "eight":
            nlist[i-1] = "eighteen"
          else:
            nlist[i-1] = "nineteen"

    if lent >= 3:
      for i in range(2, lent, 3):
        if nlist[i] != "":
          nlist[i] = nlist[i] + " hundred"
  
    if lent >= 4:
      if nlist[3] != "":
        nlist[3] = nlist[3] + " thousand"
  
    if lent >=7:
      if nlist[6] != "":
        nlist[6] = nlist[6] + " million,"
  
    if lent >=10:
      if nlist[9] != "":
        nlist[9] = nlist[9] + " billion,"
  
    if lent >=13:
      if nlist[12] != "":
        nlist[12] = nlist[12] + " trillion,"
  
    nlist.reverse()
    nlist = filter(lambda x: x!="", nlist)
    answer = " and ".join(nlist)
    if minus:
      return "minus " + answer
    else:
      return answer
  
  while True:
    try:
      num = int(raw_input("What's the number you want to be read? >>"))
    except:
      print "Number only, please."
    else:
      break
    
  print "The number %d can be read as:\n %s." % (num, readnum(str(num)))
 
numName()