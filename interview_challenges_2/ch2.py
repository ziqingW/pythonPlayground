def pythago(num):
    list_sq = [ n ** 2 for n in range(1, num)]
    for a in list_sq:
        for b in list_sq:
            c = a + b
            if c in list_sq and a ** 0.5 + b ** 0.5 + c ** 0.5 == num:
                return [a ** 0.5, b ** 0.5, c ** 0.5]
                    
print(pythago(1000))