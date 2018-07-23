def prime(n):
  primes = [2]
  x = 3
  while True:
    for i in range(len(primes)):
      if x % primes[i] == 0:
        break
      else:
        if i == len(primes) -1:
          primes.append(x)
    x += 1
    if len(primes) == n:
      break
  return primes[n-1]
      
    
print(prime(10001))