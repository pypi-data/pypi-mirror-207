from pygraphia.core import (Graph, Vertex)

Graph = Graph.Graph
Vertex = Vertex.Vertex

v1 = Vertex('v1')
v2 = Vertex('v2')


test = Graph([v1, v2])
test.add_edge(v1, v2)

if test.is_complete:
    print("Graph is complete")
else:
    print("Graph is not complete")
