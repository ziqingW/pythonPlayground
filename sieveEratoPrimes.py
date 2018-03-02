def sieve(num):
# generate the sieve block
  primeList = [i for i in range(2, num + 1)]
# stepping starts
  step = 0
# calculate till step**2 > num is enough
# mark un-primes with false
# delete those marked number 
  while step ** 2 <= num:
    for j in range(step + 1, len(primeList)):
      if primeList[j] % primeList[step] == 0:
        primeList[j] = False
    primeList = filter(lambda x: x!= False, primeList)
    step += 1
  return primeList  

print sieve(123)
  