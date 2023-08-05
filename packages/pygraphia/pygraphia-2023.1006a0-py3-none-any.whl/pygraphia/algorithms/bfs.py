from pygraphia.core.Graph import Graph
from pygraphia.core.Vertex import Vertex
from collections import deque


def bfs(graph: Graph, start_vertex: Vertex, visited: list):
    """Traverses the graph with BFS from the starting vertex. 
    Must be provided with an empty list to capture the visited vertices.

    Args:
        graph (Graph): The graph to perform BFS on.
        start_vertex (Vertex): The starting vertex.
        visited (list): The list of visited vertices.
    """
    explore_queue = deque([start_vertex])
    while len(explore_queue):
        vertex = explore_queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            for neighbor_vertices in vertex.neighbors:
                if neighbor_vertices not in visited:
                    explore_queue.append(neighbor_vertices)
