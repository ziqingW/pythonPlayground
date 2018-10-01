import sys
class Graph(object):
  
  def __init__(self, vertices):
    self.vertices = vertices
    self.graph = [[0 for row in range(self.vertices)] for column in range(self.vertices)]
    
  def minDistance(self, dist, visited):
    minDis = sys.maxint
    for i in range(self.vertices):
      if dist[i] < minDis and visited[i] == False:
        minDis = dist[i]
        node = i
    return node
    
  def shortest(self):
    dist = [sys.maxint] * self.vertices
    dist[0] = 0
    visited = [False] * self.vertices
    edges = [0] * self.vertices
    path = [""] * self.vertices
    path[0] = 0
    for count in range(self.vertices):
      u = self.minDistance(dist, visited)
      visited[u] = True
      for v in range(self.vertices):
        if self.graph[u][v] > 0 and visited[v] == False and self.graph[u][v] + dist[u] < dist[v]:
          dist[v] = self.graph[u][v] + dist[u]
          path[v] = str(u) + "-" + str(v)
          edges[v] = self.graph[u][v]
    return (path, edges)
    
graph = Graph(9)
graph.graph = [[0, 8, 0, 0, 0, 0, 0, 7, 11],
           [8, 0, 7, 10, 5, 0, 0, 0, 0],
           [0, 7, 0, 2, 0, 0, 0, 0, 0],
           [0, 10, 2, 0, 4, 0, 0, 0, 0],
           [0, 5, 0, 4, 0, 2, 0, 0, 0],
           [0, 0, 0, 0, 2, 0, 9, 0, 0],
           [0, 0, 0, 0, 0, 9, 0, 3, 4],
           [7, 0, 0, 0, 0, 0, 3, 0, 0],
           [11, 0, 0, 0, 0, 0, 4, 0, 0]]
print graph.shortest()
