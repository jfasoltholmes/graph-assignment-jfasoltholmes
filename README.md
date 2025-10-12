Name: Jordan Fasolt-Holmes

Project Overview: This program is meant to visualize the order that Depth-First Search and Breadth-First Search run in. It reads in sample data from sample.txt and performs the graph traversal algorithms on the sample data starting at a user provided vertex.

Instructions to run: Run program.py and enter a valid start vertex.

Output Generation("Portland" as input):
Depth-First Search order:
Portland
Salem
Eugene
Corvallis
Newport
Tillamook
Seaside
Astoria
Florence
Coos_Bay
Roseburg
Medford
Ashland
Crater_Lake
Bend
Redmond
Madras
The_Dalles
Hood_River
Pendleton
Ontario
Burns

Breadth-First Search order:
Portland
Salem
Astoria
Newport
Seaside
The_Dalles
Tillamook
Florence
Bend
Crater_Lake
Roseburg
Pendleton
Madras
Coos_Bay
Redmond
Burns
Medford
Ontario
Ashland

Design Decisions:
- Graph, Vertex, and Edge were implemented inside graph_impl.py in accordance to graph_interfaces.py.
- DFS is implemented in its recursive form.
- BFS is implemented using a deque from the python package, collections.
- Between running DFS and BFS, all vertices are marked as unvisited.
