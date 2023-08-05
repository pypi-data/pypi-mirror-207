import heapq
from pygraphia.core.Graph import Graph
from pygraphia.core.Vertex import Vertex
from pygraphia.core.Edge import Edge
from typing import Tuple


def get_mst(graph: Graph, start_vertex: Vertex = None) -> Tuple[list[Edge], float]:
    """Finds the MST of a given graph.

    Args:
        graph (Graph): The graph to find MST out of.
        start_vertex (Vertex, optional): The starting vertex. Defaults to Starting Vertex.

    Returns:
        Tuple[list[Edge], float]: list of edges comprising the MST and the total cost of the MST.
    """
    #     Inspired by William Fiset's Java implementation of Prim's algorithm: https://github.com/williamfiset/Algorithms
    if start_vertex == None:
        start_vertex = graph.vertex_list[0]
    total_mst_edge_count = len(graph.vertex_list) - 1
    mst_cost: float = 0
    mst_edges: list[Edge] = []
    visited: list[Vertex] = []
    temp_edge_list = start_vertex.edges
    heapq.heapify(temp_edge_list)
    while (len(temp_edge_list) and len(mst_edges) != total_mst_edge_count):
        edge = heapq.heappop(temp_edge_list)
        next_vertex = edge.dest
        visited.append(edge.src)
        if next_vertex in visited:
            continue
        else:
            mst_edges.append(edge)
            mst_cost += edge.weight
            for each_edge in next_vertex.edges:
                temp_edge_list.append(each_edge)
            heapq.heapify(temp_edge_list)
    if len(mst_edges) == total_mst_edge_count:
        return mst_edges, mst_cost
    else:
        return [], 0
