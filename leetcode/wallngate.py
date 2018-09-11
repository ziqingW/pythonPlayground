def wallAndGates(rooms):
  # find out 0 first
  q = [(i,j) for i, rows in enumerate(rooms) for j, room in enumerate(rows) if not room]
  for i,j in q:
    for I, J in (i+1, j), (i-1,j), (i,j+1), (i,j-1):
      if 0<=I<len(rooms) and 0<=J<len(rooms[0]) and rooms[I][J] > 2**30:
        rooms[I][J] = rooms[i][j] + 1
        q += (I,J),
  print(rooms)

INF = 2**31-1  
wallAndGates([[INF,  -1,  0,  INF],[INF, INF, INF,  -1],[INF,  -1, INF,  -1],[0,  -1, INF, INF]])