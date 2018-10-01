# generate a object of graph for the required operations
import sys
class Graph(object):
  def __init__(self,vertices):
    self.vertices = vertices
# Using a nested list to represent edges with their distance between each vertice     
    self.graph = [[0 for row in range(vertices)] for column in range(vertices)]

  def minDistance(self, dist, sptSet):
    # set up the min as infinite, 
    # try to find out the node among the unvisited nodes with the shortest distance so as to start with
    min = sys.maxint
    for v in range(self.vertices):
      if dist[v] < min and sptSet[v] == False:
        min = dist[v]
        min_index = v
    return min_index

# from the list of shortest paths, find out the steps from start to end 
  def combinePath(self, edges, start, end, result = None):
    if result == None:
      result = []
    for edge in edges:
      if edge.split("->")[-1] == str(end):
        result.insert(0, edge)
        if result[0].split("->")[0] != start:
          self.combinePath(edges, start, edge.split("->")[0], result)
    return result
    
# find out the shortest edges to connect all the nodes    
  def dijsktra(self, start, end):
# since when call the function, the start and end are the node numbers from 1, so here substract 1 from the start and end
    start -= 1
    end -= 1
    edgesMap = [sys.maxint] * self.vertices
    edgesMap[start] = 0
    visited = [False] * self.vertices
    path = [""] * self.vertices

# start with the given start point, check the start point everytime in the loop with minDistance function    
    for count in range(self.vertices):
      u = self.minDistance(edgesMap, visited)
# then mark the node as visited(True)
      visited[u] = True
#compare each node and its edges to find out the shortest edge
      for v in range(self.vertices):
        if self.graph[u][v] > 0 and visited[v] == False and edgesMap[v] > edgesMap[u] + self.graph[u][v]:
# add steps into the collection
          edgesMap[v] = edgesMap[u] + self.graph[u][v]
# creating string of steps
# add steps into an empty, it can be overlapped by the shortest one at same node
          endpoint = str(u+1) + "->" + str(v+1)
          path[v] = endpoint
    
    
    return self.combinePath(path, start+1, end+1)
    
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

print graph.dijsktra(1,6)
