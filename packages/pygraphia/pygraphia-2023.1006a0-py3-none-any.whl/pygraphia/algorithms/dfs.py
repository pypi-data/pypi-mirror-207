from pygraphia.core.Graph import Graph
from pygraphia.core.Vertex import Vertex


def dfs(graph: Graph, start_vertex: Vertex, visited: list):
    """"Traverses the graph with DFS from the starting vertex. 
    Must be provided with an empty list to capture the visited vertices.

    Args:
        graph (Graph): The graph to perform DFS on.
        start_vertex (Vertex): The starting vertex.
        visited (list): The list of visited vertices.
    """
    visited.append(start_vertex)
    for each_neighbor in start_vertex.neighbors:
        if each_neighbor not in visited:
            dfs(graph, each_neighbor, visited)
