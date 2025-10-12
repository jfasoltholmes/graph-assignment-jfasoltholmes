from graph_interfaces import IEdge, IGraph, IVertex
from typing import List, Optional, Dict

# Implementation definitions
# You should implement the bodies of the methods required by the interface protocols.

class Graph(IGraph):
    def __init__(self) -> None:
        self._vertices: List[IVertex] = []
        self._edges: List[IEdge] = []
    
    def get_vertices(self) -> List[IVertex]:
        return self._vertices

    def get_edges(self) -> List[IEdge]:
        return self._edges
    
    def add_vertex(self, vertex: IVertex) -> None:
        # Ensure no duplicate vertex names
        if any(v.get_name() == vertex.get_name() for v in self._vertices):
            raise Exception(f"Vertex with name {vertex.get_name()} already exists.")
        self._vertices.append(vertex)

    def remove_vertex(self, vertex_name: str) -> None:
        # Remove vertex and all associated edges
        self._vertices = [v for v in self._vertices if v.get_name() != vertex_name]
        self._edges = [e for e in self._edges if e.get_destination().get_name() != vertex_name]

    def add_edge(self, edge: IEdge) -> None:
        # Ensure no duplicate edge names
        if any(e.get_name() == edge.get_name() for e in self._edges):
            raise Exception(f"Edge with name {edge.get_name()} already exists.")
        self._edges.append(edge)
        
        # Also add the edge to the source vertex
        source_name = edge.get_name().split('-')[0]
        source_vertex = next((v for v in self._vertices if v.get_name() == source_name), None)
        if source_vertex is not None:
            source_vertex.add_edge(edge)

    def remove_edge(self, edge_name: str) -> None:
        # Remove edge from graph and from all vertices
        self._edges = [e for e in self._edges if e.get_name() != edge_name]
        for vertex in self._vertices:
            vertex.remove_edge(edge_name)

class Vertex(IVertex):
    def __init__(self, name: str) -> None:
        self._name: str = name
        self._edges: List[IEdge] = []
        self._visited: bool = False

    def get_name(self) -> str:
        return self._name
    
    def set_name(self, name: str) -> None:
        self._name = name

    def add_edge(self, edge: IEdge) -> None:
        self._edges.append(edge)

    def remove_edge(self, edge_name: str) -> None:
        # Remove edge by name
        self._edges = [e for e in self._edges if e.get_name() != edge_name]

    def get_edges(self) -> List[IEdge]:
        return self._edges

    def set_visited(self, visited: bool) -> None:
        self._visited = visited

    def is_visited(self) -> bool:
        return self._visited

class Edge(IEdge):
    def __init__(self, name: str, destination: IVertex, weight: Optional[float] = None) -> None:
        self._name: str = name
        self._destination: IVertex = destination
        self._weight: Optional[float] = weight
    
    def get_name(self) -> str:
        return self._name
    
    def set_name(self, name: str) -> None:
        self._name = name

    def get_destination(self) -> IVertex:
        return self._destination
    
    def get_weight(self) -> Optional[float]:
        return self._weight

    def set_weight(self, weight: float) -> None:
        self._weight = weight
