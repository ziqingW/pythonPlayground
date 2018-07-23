def isPrime(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True
        
def Christian():
    x = 5
    a = 1
    while True:
        prime = x - 2 * a**2
        if prime > 0:
            if isPrime(prime):
                x += 2
            else:
                a += 1
        else:
            return x

print(Christian())