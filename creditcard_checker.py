import re

def luhnAlgo(num):
  num = num[::-1]
  checksum = 0
  for i in num[::2]:
    checksum += int(i)
  for i in num[1::2]:
    digit = int(i) * 2
    if digit > 9:
      digit = digit - 9
    checksum += digit
  if checksum % 10 == 0:
    return True
  else:
    return False

  
def creditCheck():
  while True:
    card = raw_input("What's your credit card number? >>")
    if re.search("[^0-9]", card):
      print "That's not legit credit card number, please check it if right."
      continue
    else:
      break
  if luhnAlgo(card):
    print "It's a valid credit card, thank you!"
  else:
    print "Sorry, it's not a valid card, please change another card."
    
creditCheck()

    