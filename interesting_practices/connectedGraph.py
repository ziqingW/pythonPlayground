def connected(graph):
  
  def path(vertice, nodes = None):
# for the ease of recursive use, set up the default value of nodes ae None; when recursive, nodes can be inherited from the previous result
    if nodes == None:
      nodes = []
    connected = graph[vertice]
# if the connected points are not repeated yet in nodes, add it
# until all of the nodes are checked by the loop that no non-repeat one, return the result nodes
    for point in connected:
      if point not in set(nodes):
        nodes += point
        path(point, nodes)
    return nodes
  
  allvertex = list(graph.keys())
  for vertice in allvertex:
    if set(path(vertice)) != set(allvertex):
      return False
  return True

if connected({ "a" : ["f", "b"],
       "b" : ["c","b"],
       "c" : ["b", "c", "d", "e"],
       "d" : ["a", "c"],
       "e" : ["c"],
       "f" : ["a"]
}):
  print "This graph is connected."
else:
  print "This is not a connected graph."