def makeGraph(linklist):
  verticeSet = set(link[0] for link in linklist)
  graph = {}
  for vertice in verticeSet:
    graph[vertice] = [link[1] for link in linklist if link[0] == vertice]
  return graph

print makeGraph([('a', 'c'), ('c', 'a'), ('c', 'b'), ('c', 'd'), ('c', 'e'), ('b', 'c'), ('b', 'e'), ('e', 'c'), ('e', 'b'), ('d', 'c')])