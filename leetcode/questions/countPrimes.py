# Count the number of prime numbers less than a non-negative number, n.

# Example:

# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

import math
class Solution:
    # a straightforward method but TLE
#     def isPrime(self, n):
#         if n <= 1:
#             return False
#         elif n % 2 == 0:
#             return False
#         for i in range(3, int(n**0.5)+1, 2):
#             if n % i == 0:
#                 return False
#         return True
        
#     def countPrimes(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """ 
#         if n < 3:
#             return 0
#         count = 0
#         for num in range(2, n):
#             if self.isPrime(num):
#                 count += 1
#         return count

# sieve method also TLE
    # def countPrimes(self, n):
    #     if n <= 2:
    #         return 0
    #     else:
    #         sieves = [1] * n
    #         sieves[0] = sieves[1] = 0
    #         for i in range(2, int(math.sqrt(n))+1):
    #             pointer = 2 * i
    #             while pointer < n:
    #                 sieves[pointer] = 0
    #                 pointer += i
    #         return sum(sieves)

# another method without TLE
    def countPrimes(self, n):
        notPrime = [False] * n
        count = 0
        for i in range(2, n):
            if not notPrime[i]:
                count += 1
                for j in range(2, math.ceil(n/i)):
                    notPrime[i*j] = True
        return count
# all the previous methods are slow,
# here is a fast method
    def countPrimes(self, n):
        if n <= 2:
            return 0
        primes = [1] * n
        primes[0] = primes[1] = 0
        for i in range(2, int(n**0.5)+1):
            if primes[i] == 1:
                primes[i*i:n:i] = [0]*len(primes[i*i:n:i])
        return sum(primes)
        