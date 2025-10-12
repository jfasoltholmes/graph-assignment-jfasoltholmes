from typing import Optional
from graph_interfaces import IGraph, IVertex
from graph_impl import Graph, Vertex, Edge
from collections import deque
import csv

def read_graph(file_path: str) -> IGraph:  
    """Read the graph from the file and return the graph object"""
    # Create the empty graph
    graph = Graph()
    # Read the file and populate the graph
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        # Skip the header row
        next(reader)
        for row in reader:
            source_name, dest_name, highway_name, distance_str = row
            # Convert distance to integer
            distance = int(distance_str)

            # Create or get the source/destination vertex
            source_vertex = next((v for v in graph.get_vertices() if v.get_name() == source_name), None)
            if source_vertex is None:
                source_vertex = Vertex(source_name)
                graph.add_vertex(source_vertex)

            destination_vertex = next((v for v in graph.get_vertices() if v.get_name() == dest_name), None)
            if destination_vertex is None:
                destination_vertex = Vertex(dest_name)
                graph.add_vertex(destination_vertex)

            # Add the edge to the graph
            edge_name = f"{source_name}-{dest_name}-{highway_name}"
            edge = Edge(edge_name, destination_vertex, distance)
            graph.add_edge(edge)
            
    return graph

def print_dfs(graph: IGraph, start_vertex: IVertex) -> None: 
    """Print the DFS traversal of the graph starting from the start vertex"""
    def dfs(vertex: IVertex) -> None:
        # Mark the vertex as visited
        vertex.set_visited(True)
        print(vertex.get_name())
        # Recur for all the adjacent vertices
        for edge in vertex.get_edges():
            neighbor = edge.get_destination()
            if not neighbor.is_visited():
                dfs(neighbor)

    dfs(start_vertex)

def print_bfs(graph: IGraph, start_vertex: IVertex) -> None: 
    """Print the BFS traversal of the graph starting from the start vertex"""
    queue = deque([start_vertex])
    start_vertex.set_visited(True)

    while queue:
        vertex = queue.popleft()
        print(vertex.get_name())
        for edge in vertex.get_edges():
            neighbor = edge.get_destination()
            if not neighbor.is_visited():
                neighbor.set_visited(True)
                queue.append(neighbor) 


def main() -> None:
    graph: IGraph = read_graph("graph.txt")
    start_vertex_name: str  = input("Enter the start vertex name: ")

    # Find the start vertex object
    start_vertex: Optional[IVertex]= next((v for v in graph.get_vertices() if v.get_name() == start_vertex_name), None)

    if start_vertex is None:
        print("Start vertex not found")
        return
    
    print("\nDepth-First Search order:")
    print_dfs(graph, start_vertex)

    # Reset vertices
    for vertex in graph.get_vertices():
        vertex.set_visited(False)

    print("\nBreadth-First Search order:")
    print_bfs(graph, start_vertex)


if __name__ == "__main__":
    main()