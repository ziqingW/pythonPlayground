def nextPrime():
  
  def query():
    answer = ""
    while not (answer == "y" or answer == "n"):
      answer = raw_input("Do you want to see the next Prime Number? y or n >>")
    if answer == "y":
      print "The next Prime Number is", next(g)
      query()
    else:
      print "Goodbye, see you next time!"

  def find():
    n = 3
    while True:
      list = [num for num in range(2, n/2 + 1) if n % num == 0]
      if list != []:
        n += 1
      else:
        p = n
        n += 1
        yield p
      

  g = find()
  print "The first Prime Number is 2."
  query()
  
nextPrime()