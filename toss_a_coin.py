import random
def coin():
  head = 0
  tail = 0
  times = 0
  while True:
    answer = ""
    while not (answer == "y" or answer == "n"):
      answer = raw_input("Do you want to toss the coin? >> choose y or n.")
    if answer == "y":
      x = random.randint(0,1)
      if x == 0:
        head += 1
        print "You tossed the coin, it's %s!" % "head"
      else:
        tail += 1
        print "You tossed the coin, it's %s!" % "tail"
      times += 1
    else:
      break
  print "You have tossed %d times of coins, %d head and %d tail in total." % (times, head, tail)

coin() 