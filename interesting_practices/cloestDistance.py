def closestPath(l):
# calculate distance between two points  
  def distanceBetween(a,b):
    x1,y1 = a
    x2,y2 = b
    distance = ((x1-x2) ** 2 + (y1-y2) ** 2) ** 0.5
    return distance

  mindistance = 0
  pointsList = []
  result = []
  for i in range(len(l)-1):
    for j in range(i+1, len(l)):
      pointsList.append([l[i],l[j]])
  mindistance = distanceBetween(pointsList[0][0],pointsList[0][1])
  result = pointsList[0]
  for x in range(1, len(pointsList)):
    distance = distanceBetween(pointsList[x][0],pointsList[x][1])
    if distance < mindistance:
      mindistance = distance
      result = pointsList[x]
  return distance, result

print closestPath([(1,3),(4,5),(7,8),(9,10)])