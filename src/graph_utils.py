from src.graph_interfaces import IGraph, IVertex
from src.graph_impl import Graph, Vertex, Edge
from collections import deque
from haversine import haversine, Unit
import csv
import heapq
from typing import List, Optional, Tuple, Dict

def read_vertices(file_path: str, graph: IGraph) -> None:
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        # Skip the header row
        next(reader)
        for row in reader:
            name, lat_str, lon_str = row
            latitude = float(lat_str)
            longitude = float(lon_str)
            vertex = next((v for v in graph.get_vertices() if v.get_name() == name), None)
            if vertex is None: 
                vertex = Vertex(name, latitude, longitude)
                graph.add_vertex(vertex)
            else:
                vertex.set_coordinates(latitude, longitude)

def read_graph(file_path: str) -> IGraph:  
    """Read the graph from the file and return the graph object"""
    # Create the empty graph, and read vertices
    graph = Graph()
    read_vertices("vertices_v1.txt", graph)
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

            # Create the edge and add it to the graph
            edge_name = f"{source_name}|{dest_name}|{highway_name}"
            edge = Edge(edge_name, source_vertex, destination_vertex, distance)
            source_vertex.add_edge(edge)
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

def heuristic(vertex1: IVertex, vertex2: IVertex) -> float:
    # Calculate the heuristic between the two vertices
    coords1 = vertex1.get_coordinates()
    coords2 = vertex2.get_coordinates()
    return haversine(coords1, coords2, unit=Unit.MILES)

def dijkstra(graph: IGraph, start_vertex: IVertex, end_vertex: IVertex) -> Dict[str, float]:
    # Initialize dictionary to hold names of vertices and their distances
    distances: Dict[str, float] = {v.get_name(): float('inf') for v in graph.get_vertices()}
    # Set distance to start vertex to 0
    distances[start_vertex.get_name()] = 0.0
    # Initialize dictionary for vertices
    vertex_map: Dict[str, IVertex] = {v.get_name(): v for v in graph.get_vertices()}
    # Initialize dictionary for tracking predecessors
    predecessors: Dict[str, str] = {}

    # Initialize priority queue
    priority_queue = [(0.0, start_vertex.get_name())]
    visited = set()

    # Counters
    vertices_explored = 0
    edges_evaluated = 0

    # Main Loop
    while priority_queue:
        current_distance, current_name = heapq.heappop(priority_queue)
        vertices_explored += 1

        if current_name in visited:
            continue
        visited.add(current_name)

        # Check if end vertex has been reached
        if current_name == end_vertex.get_name():
            break

        current_vertex = vertex_map[current_name]

        for edge in current_vertex.get_edges():
            edges_evaluated += 1
            neighbor = edge.get_destination()
            weight = edge.get_weight() or 0.0

            new_distance = current_distance + weight

            if new_distance < distances[neighbor.get_name()]:
                distances[neighbor.get_name()] = new_distance
                predecessors[neighbor.get_name()] = current_name
                heapq.heappush(priority_queue, (new_distance, neighbor.get_name()))

    path = []
    current = end_vertex.get_name()
    while current in predecessors:
        path.append(current)
        current = predecessors[current]
    if path:
        path.append(start_vertex.get_name())
        path.reverse()
    else:
        path = [start_vertex.get_name()]

    return distances[end_vertex.get_name()], path, vertices_explored, edges_evaluated

def gbfs(graph: IGraph, start_vertex: IVertex, end_vertex: IVertex) -> Dict[str, float]:
    # Initialize the priority queue
    priority_queue = [(heuristic(start_vertex, end_vertex), start_vertex.get_name(), 0.0)]
    visited = set()
    predecessors: Dict[str, str] = {}

    # For tracking total distances
    distances: Dict[str, float] = {v.get_name(): float('inf') for v in graph.get_vertices()}
    distances[start_vertex.get_name()] = 0.0

    # Map vertex names to vertex objects
    vertex_map: Dict[str, IVertex] = {v.get_name(): v for v in graph.get_vertices()}

    # Counters
    vertices_explored = 0
    edges_evaluated = 0

    while priority_queue:
        current_heuristic, current_name, current_distance = heapq.heappop(priority_queue)
        vertices_explored += 1

        if current_name in visited:
            continue
        visited.add(current_name)

        # Check if end vertex has been reached
        if current_name == end_vertex.get_name():
            total_distance = current_distance
            break

        current_vertex = vertex_map[current_name]

        for edge in current_vertex.get_edges():
            edges_evaluated += 1

            neighbor = edge.get_destination()
            neighbor_name = neighbor.get_name()
            weight = edge.get_weight() or 0.0

            new_distance = current_distance + weight

            if neighbor_name not in visited:
                predecessors[neighbor_name] = current_name
                heuristic_value = heuristic(neighbor, end_vertex)
                heapq.heappush(priority_queue, (heuristic_value, neighbor_name, new_distance))
                distances[neighbor_name] = new_distance
    
    path = []
    current = end_vertex.get_name()
    while current in predecessors:
        path.append(current)
        current = predecessors[current]
    if path:
        path.append(start_vertex.get_name())
        path.reverse()
    else:
        path = [start_vertex.get_name()]

    return total_distance, path, vertices_explored, edges_evaluated

def a_star(graph: IGraph, start_vertex: IVertex, end_vertex: IVertex) -> Dict[str, float]:
    g_scores: Dict[str, float] = {v.get_name(): float('inf') for v in graph.get_vertices()}
    g_scores[start_vertex.get_name()] = 0.0

    f_scores: Dict[str, float] = {v.get_name(): float('inf') for v in graph.get_vertices()}
    f_scores[start_vertex.get_name()] = heuristic(start_vertex, end_vertex)

    vertex_map: Dict[str, IVertex] = {v.get_name(): v for v in graph.get_vertices()}

    priority_queue = [(f_scores[start_vertex.get_name()], start_vertex.get_name())]
    visited = set()
    predecessors: Dict[str, str] = {}

    vertices_explored = 0
    edges_evaluated = 0

    while priority_queue:
        current_f_score, current_name = heapq.heappop(priority_queue)
        vertices_explored += 1

        if current_name in visited:
            continue
        visited.add(current_name)

        if current_name == end_vertex.get_name():
            break

        current_vertex = vertex_map[current_name]

        for edge in current_vertex.get_edges():
            edges_evaluated += 1
            neighbor = edge.get_destination()
            weight = edge.get_weight() or 0.0

            tentative_g_score = g_scores[current_name] + weight

            if tentative_g_score < g_scores[neighbor.get_name()]:
                predecessors[neighbor.get_name()] = current_name
                g_scores[neighbor.get_name()] = tentative_g_score
                f_scores[neighbor.get_name()] = tentative_g_score + heuristic(neighbor, end_vertex)
                heapq.heappush(priority_queue, (f_scores[neighbor.get_name()], neighbor.get_name()))
    
    path = []
    current = end_vertex.get_name()
    while current in predecessors:
        path.append(current)
        current = predecessors[current]
    if path:
        path.append(start_vertex.get_name())
        path.reverse()
    else:
        path = [start_vertex.get_name()]

    return g_scores[end_vertex.get_name()], path, vertices_explored, edges_evaluated

