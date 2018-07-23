sum = 0
for n in range(1, 1001):
    if n % 15 == 0:
        sum += n
    elif n % 3 == 0:
        sum += n
    elif n % 5 == 0:
        sum += n
print(sum)        
