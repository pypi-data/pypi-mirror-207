from .Vertex import Vertex
from dataclasses import dataclass, field


@dataclass()
class Walk:
    """Class defining a walk.

    Attributes
    ___________
    vertex_list: list[Vertex]
        The list of verties in the walk.

    is_empty: bool
        Whether the walk is empty or not.

    """

    vertex_list: list[Vertex] = field(default_factory=list)
    is_empty: bool = False

    def __init__(self, vertex: Vertex | None):
        if isinstance(vertex, Vertex):
            self.vertex_list.append(vertex)
        else:
            self.is_empty = True

    def add(self, vertex: Vertex):
        """Add a vertex to the walk.

        Args:
            vertex (Vertex): The vertex to be added to the walk.
        """
        self.vertex_list.append(vertex)

    def __repr__(self) -> str:
        if not self.is_empty:
            return '--'.join(str(vertex) for vertex in self.vertex_list)
        else:
            return 'No Walk'

    def __str__(self) -> str:
        if not self.is_empty:
            return '--'.join(str(vertex) for vertex in self.vertex_list)
        else:
            return 'No Walk'
