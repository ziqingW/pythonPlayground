def fibonacci():
    list = [1, 1]
    while True:
        x = list[-1] + list[-2]
        list.append(x)
        if x > 4000000:
            break
    print(sum(list))
        
fibonacci()