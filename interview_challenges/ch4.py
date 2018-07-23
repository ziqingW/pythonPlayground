def prime(n):
  primes = [2]
  for x in range(3, n+1):
    for i in range(len(primes)):
      if x % primes[i] == 0:
        break
      else:
        if i == len(primes) -1:
          primes.append(x)
  return primes
      
      
    
    
print(prime(600851475143)[-1])
    
