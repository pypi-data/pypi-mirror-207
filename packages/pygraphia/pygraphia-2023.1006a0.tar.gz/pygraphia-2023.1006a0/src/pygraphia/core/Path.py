from .Vertex import Vertex
from .Walk import Walk
from dataclasses import dataclass, field


@dataclass(init=False)
class Path(Walk):
    """A subclass of Walk.
    """

    def add(self, vertex: Vertex):
        if vertex not in self.vertex_list:
            self.vertex_list.append(vertex)
        else:
            pass
