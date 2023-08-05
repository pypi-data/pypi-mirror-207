from __future__ import annotations
from typing import TYPE_CHECKING
# turning this check off will result in import loop
if TYPE_CHECKING:
    from .Edge import Edge


class Vertex:
    """The Vertex class containing the necessary properties for defining a Vertex.

    Note: This class contains immutable private variables that can only be accessed via properties.

    label: str
        The label of the Vertex.

    directed: bool
        Whether the vertex is part of a directed graph or not.

    incoming_edges: list[Edge]
        Lists the incoming edges of the vertex.

    outgoing_edges: list[Edge]
        Lists the outgoing edges of the vertex.

    neighbors: list[Vertex]
        List of neighboring vertices.

    edges: list[Edge]
        List of all edges. For undirected graph, defaults to outgoing edges.

    indegree: int
        The indegree of the vertex.

    outdegree: int
        The outdegree of the vertex.

    degree: int
        The degree of the vertex= indegree + outdegree.



    """

    def __init__(self,
                 label: str = '',
                 directed: bool = False):
        self.__label = label
        self.__directed = directed
        self.__incoming_edges: list[Edge] = []
        self.__outgoing_edges: list[Edge] = []
        self.__neighbors: list[Vertex] = []

    @property
    def label(self) -> str:
        return self.__label

    @property
    def directed(self) -> bool:
        return self.__directed

    @property
    def incoming_edges(self) -> list[Edge]:
        return self.__incoming_edges

    @property
    def outgoing_edges(self) -> list[Edge]:
        return self.__outgoing_edges

    @property
    def neighbors(self) -> list:
        return self.__neighbors

    @property
    def edges(self) -> list[Edge]:
        if self.directed:
            return self.incoming_edges + self.outgoing_edges
        else:
            return self.outgoing_edges

    @property
    def indegree(self) -> int:
        return len(self.incoming_edges)

    @property
    def outdegree(self) -> int:
        return len(self.outgoing_edges)

    @property
    def degree(self) -> int:
        if self.directed:
            return self.indegree + self.outdegree
        else:
            return int(
                (self.outdegree + self.indegree)/2)

    def __repr__(self):
        return self.label

    def __str__(self):
        return self.label

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Vertex):
            if __value.label == self.label:
                return True
            else:
                return False
        else:
            return False

    def __hash__(self) -> int:
        return hash(self.label)
