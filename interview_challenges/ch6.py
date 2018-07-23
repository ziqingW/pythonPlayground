def collatz(num):
    results = [num]
    while num != 1 :
        if num % 2 == 0 :
            num /= 2
        else:
            num = num * 3 + 1
        results.append(num)
    return results
    
for n in collatz(30):
    print(n)
        