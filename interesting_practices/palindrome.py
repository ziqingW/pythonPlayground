for n in [x * y for x in range(1000, 99, -1) for y in range(1000, 99, -1)]:
  if str(n)[::-1] == str(n):
    print(n)
    break