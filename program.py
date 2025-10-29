from typing import Optional
from src.graph_interfaces import IGraph
from src.graph_utils import a_star, gbfs, read_graph, dijkstra
import time

def main() -> None:
    graph: IGraph = read_graph("graph_v2.txt")

    # While loop to allow user to enter a different vertex
    while True:
        start_vertex_name: str  = input("Enter the start vertex name: ")
        # Find the start vertex object
        start_vertex = graph.get_vertex(start_vertex_name)
        if start_vertex is None:
            print("\nStart vertex not found, please examine vertices in graph_v2.txt and try again.")
            continue

        end_vertex_name: str  = input("Enter the end vertex name: ")
        # Find the end vertex object
        end_vertex = graph.get_vertex(end_vertex_name)
        if end_vertex is None:
            print("\nEnd vertex not found, please examine vertices in graph_v2.txt and try again.")
            continue

        # Menu for algorithm selection
        print("\n\nChoose your algorithm: ")
        print("1. Dijkstra's Algorithm")
        print("2. Greedy Best-First Search")
        print("3. A* Search Algorithm")
        choice = input("Enter the number of your choice: ").strip()

        if choice == '1':
            print("\nRunning Dijkstra's Algorithm...")
            start_time = time.perf_counter()
            distance, path, vertices_explored, edges_evaluated = dijkstra(graph, start_vertex, end_vertex)
            end_time = time.perf_counter()

            # Print the results
            print(f"Path: {' -> '.join(path)}")
            print(f"Total Distance: {distance}")
            print(f"Vertices Explored: {vertices_explored}")
            print(f"Edges Evaluated: {edges_evaluated}")
            print(f"Time taken: {end_time - start_time:.6f} seconds")

        elif choice == '2':
            print("\nRunning Greedy Best-First Search...")
            start_time = time.perf_counter()
            distance, path, vertices_explored, edges_evaluated = gbfs(graph, start_vertex, end_vertex)
            end_time = time.perf_counter()

            # Print the results
            print(f"Path: {' -> '.join(path)}")
            print(f"Total Distance: {distance}")
            print(f"Vertices Explored: {vertices_explored}")
            print(f"Edges Evaluated: {edges_evaluated}")
            print(f"Time taken: {end_time - start_time:.6f} seconds")
            
        elif choice == '3':
            print("\nRunning A* Search Algorithm...")
            start_time = time.perf_counter()
            distance, path, vertices_explored, edges_evaluated = a_star(graph, start_vertex, end_vertex)
            end_time = time.perf_counter()

            # Print the results
            print(f"Path: {' -> '.join(path)}")
            print(f"Total Distance: {distance}")
            print(f"Vertices Explored: {vertices_explored}")
            print(f"Edges Evaluated: {edges_evaluated}")
            print(f"Time taken: {end_time - start_time:.6f} seconds")
        else:
            print("\nInvalid choice. Please select a valid algorithm number.")
            continue

        # Reset vertices
        for vertex in graph.get_vertices():
            vertex.set_visited(False)

        # Prompt to continue or exit
        cont = input("\nDo you want to search another route? (y/n): ").strip().lower()
        if cont != 'y':
            print("\nThank you for using the Oregon Pathfinder!\nGoodbye!\n\n")
            break


if __name__ == "__main__":
    main()