def primefactor():
  def calculate():
    while True:
      try:
        n = int(raw_input("PLease input a number to see its prime factors: >"))
        global n
      except:
        print "Sorry, that's incorrect. Please input again."
        continue
      else:
        break
    if n == 2:
      return [n]
    else:
      list = [num for num in range(2, n/2 + 1) if n % num == 0]
      if list == []:
        return [n]
      else:
        for x in list:
          tempolist = list[:]
          tempolist.remove(x)
          for y in tempolist:
            if y % x == 0:
              list.remove(y)
        return list
  
  result = calculate()
  print "The prime factors of number %d is: " % n
  for num in result:
    print num

primefactor()