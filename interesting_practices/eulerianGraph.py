def eulerian(graph):
  degrees = []
  for vertices in graph.values():
      degrees.append(len(vertices))
  even = 0
  odd = 0
  for degree in degrees:
    if degree % 2 == 0 and degree != 0:
      even += 1
    elif degree % 2 != 0 and degree != 0:
      odd += 1
  print "There are %d even degrees in the graph." % even
  print "There are %d odd degrees in the graph." % odd
  if odd > 0:
    print "There is no Euler Circuit for this graph."
    if odd > 2:
      print "There is no Euler Path for this graph."
    elif (not 0 in degrees) and odd == 2:
      print "There is at least one Euler Path for this graph."
  else:
    print "There is at least one Euler Circuit for this graph."
  
eulerian({ "a" : ["c",'d'],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c",'a'],
          "e" : ["c", "b"],
          "f" : ['a','c']
        })