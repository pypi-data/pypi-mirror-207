from .Vertex import Vertex
from .Edge import Edge
from .Path import Path
# Helpful for graph theory jargon: https://en.wikipedia.org/wiki/Glossary_of_graph_theory


class Graph:
    """Main Graph class containing the necessary data structure, properties and methods.

    Note: This class contains immutable private variables that can only be accessed via properties.

    Properties
    ___________

    directed: bool
        Whether the graph is directed or not

    is_regular: bool
        Whether the graph is regular or not. 

    is_tree: bool
        Whether the graph is tree or not.

    is_eulerian: bool
        Whether the graphWhether the graph is eulerian or not.

    is_connected: bool
        Whether the graph is connected ot not.

    is_complete: bool
        Whether the graph is complete or not.

    is_cylclic: bool
        Whether the graph is cyclic or not.

    is_cycle: bool
        Whether the graph is a cycle or not.

    vertex_list: list[Vertex]
        List of vertices of the graph.

    """

    def __init__(self,
                 vertex_list: list[Vertex] = [], /, *,
                 directed: bool = False):
        self.__adj_list: dict[Vertex, list[Vertex]] = {}
        self.__out_adj_list: dict[Vertex, list[Vertex]] = {}  # for digraphs
        self.__directed = directed
        for each_vertex in vertex_list:
            if isinstance(each_vertex, Vertex):
                each_vertex.__directed = directed
                if each_vertex not in self.__adj_list.keys():
                    self.__adj_list.update({
                        each_vertex: []
                    })
            else:
                raise TypeError("Added vertices should be of the type Vertex")

    def __getitem__(self, vertex: Vertex):
        return self.__adj_list[vertex]

    # methods

    def add_vertex(self, vertex_list: list[Vertex]):
        """Add vertex/vertices to the graph.

        Args:
            vertex_list (list[Vertex]): list of vertex/vertices to be added.

        Raises:
            TypeError: Contents of list must be of the type Vertex.
        """
        for each_vertex in vertex_list:
            if each_vertex is Vertex:
                if each_vertex not in self.__adj_list.keys():
                    each_vertex.__directed = self.__directed
                    self.__adj_list.update({
                        each_vertex: []
                    })
            else:
                raise TypeError("Added vertices should be of the type Vertex")

    def add_edge(self,
                 src: Vertex,
                 dest: Vertex,
                 label: str = '',
                 weight: float = 0):
        """Add edge between two existing vertices

        Args:
            src (Vertex): The source vertex
            dest (Vertex): The destination vertex
            label (str, optional): Label of the edge. Defaults to ''.
            weight (float, optional): Weight/cost of associated with the edge. Defaults to 0.
        """
        # our adj list for digraph only stores vertices
        # that are connected by outwards going edges

        # exceptions
        # if not isinstance(src, Vertex):
        #     raise TypeError("src should be of the type Vertex")
        # if not isinstance(dest, Vertex):
        #     raise TypeError("dest should be of the type Vertex")
        # if not isinstance(label, str):
        #     raise TypeError("label should be of the type str")

        outgoing_edge = Edge(src, dest, label, weight, self.__directed)
        if self.__directed:
            for vertex in self.__adj_list:
                if vertex is src:
                    vertex.outgoing_edges.append(outgoing_edge)
                    vertex.neighbors.append(dest)
                    break
            dest.incoming_edges.append(outgoing_edge)
            self.__out_adj_list[src].append(dest)
        else:
            incoming_edge = Edge(dest, src, label, weight, self.__directed)
            for vertex in self.__adj_list:
                if vertex is src:
                    vertex.neighbors.append(dest)
                    vertex.outgoing_edges.append(outgoing_edge)
                    vertex.incoming_edges.append(incoming_edge)
                    break
            dest.neighbors.append(src)
            dest.incoming_edges.append(outgoing_edge)
            dest.outgoing_edges.append(incoming_edge)
        self.__adj_list[src].append(dest)
        self.__adj_list[dest].append(src)

    def components_count(self) -> int:
        """Counts the components of the graph.

        Returns:
            int:The number of components.
        """
        from pygraphia.algorithms.dfs import dfs
        start_vertex = next(iter(self.__adj_list))
        temp_vertices = [start_vertex]
        list_of_vertices = set(self.__adj_list.keys())
        for each_vertex in temp_vertices:
            visited: list[Vertex] = []
            dfs(self, each_vertex, visited)
            left_out_vertices = [
                x for x in list_of_vertices if x not in visited]
            if len(left_out_vertices) > 0:
                temp_vertices.append(next(iter(left_out_vertices)))
        return len(temp_vertices)

    def get_shortest_path(self, src: Vertex, dest: Vertex) -> Path:
        """Uses BFS to find the shortest path between two vertices.

        Args:
            src (Vertex): The source vertex.
            dest (Vertex): The destination vertex.

        Returns:
            Path: The shortest path. 
        """
        # todo: add option for floyd warshall https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
        from collections import deque
        visited = set()
        explore_queue = deque([(src, Path(src))])
        while len(explore_queue):
            vertex, path = explore_queue.popleft()
            if vertex == dest:
                path.add(vertex)
                return path
            else:
                visited.add(vertex)
                for neighbor in vertex.neighbors:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        path.add(vertex)
                        explore_queue.append((neighbor, path))
        return Path(None)

    # properties

    @property
    def directed(self) -> bool:
        return self.__directed

    @property
    def vertex_list(self) -> list[Vertex]:
        return list(self.__adj_list)

    @property
    def is_complete(self) -> bool:
        total_vertices = len(self.vertex_list)
        total_edges = sum(len(self.__adj_list[x]) for x in self.__adj_list)
        if self.directed:
            return total_edges == total_vertices*(total_vertices - 1)/2
        else:
            return total_edges/2 == total_vertices*(total_vertices - 1)/2

    @property
    def is_connected(self) -> bool:
        from pygraphia.algorithms.dfs import dfs
        visited: list[Vertex] = []
        dfs(self, next(iter(self.vertex_list)), visited)
        return set(visited) == set(self.vertex_list)

    @property
    def is_regular(self) -> bool:
        return all(list(x.degree == next(iter(self.vertex_list)).degree for x in self.vertex_list))

    # this is different from a cyclic graph
    # a cycle is a connected 2-regular graph
    @property
    def is_cycle(self) -> bool:
        return self.is_connected and self.is_regular and all(list(x.degree == 2 for x in self.vertex_list))

    @property
    def is_cyclic(self) -> bool:
        visited = []
        parent: Vertex
        explore_list = [self.vertex_list[0]]
        while len(explore_list):
            vertex = explore_list.pop()
            if vertex not in visited:
                visited.append(vertex)
                for each_neighbor in vertex.neighbors:
                    if each_neighbor not in visited:
                        parent = vertex
                        explore_list.append(each_neighbor)
                    elif (each_neighbor in visited) and each_neighbor != parent:
                        return True
        return False

    @property
    def is_tree(self) -> bool:
        return self.is_connected and not self.is_cyclic

    @property
    def is_eulerian(self) -> bool:
        return self.is_connected and all(list(x.degree // 2 == 0 for x in self.vertex_list))

    def __str__(self):
        return str(self.__adj_list)
