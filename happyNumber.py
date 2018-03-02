from __future__ import division

def happyNumber(s0):

  def powerten(n):
    while n > 1:
      n /= 10
      if n == 1:
        return True
    return False

  scopy = s0
  slist = []
  happy = False
  while True:
    s1 = 0
    for i in str(s0):
      s2 = int(i) ** 2
      s1 += s2
    if s1 == 1 or powerten(s1):
      happy = True
      break
    else:
      if s1 in slist:
        break
      else:
        s0 = s1
        slist.append(s1)
        continue
  if happy == True:
    return True
  else:
    return False
  
def happygenerator():
  n = 1
  while True:
    if happyNumber(n):
      result = n
      n += 1
      yield result
    else:
      n += 1

happy = happygenerator()
for i in range(20):
  print next(happy)

