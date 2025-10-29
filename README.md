Name: Jordan Fasolt-Holmes

# Project Overview: <br />
This program is meant to visualize the order that graph traversals run in. This version is an update to v1.0 which gave the order for Depth-First Search and Depth-First Search. Version 2.0 analyzes the Dijkstra, Greedy Best-First Search, and A* algorithm. It reads in sample data from graph_v2.txt and vertices_v1.txt. It then performs the graph traversal algorithms on the sample data starting at a user provided vertex and ending at a second user provided vertex. The program then returns the path, total distance, vertices explored, edges evaluated, and runtime of the algorithm the user selects to analyze.

## Instructions to run: 
Ensure haversine package is installed:
pip install haversine

Run program.py and enter a valid algorithm, start vertex, and end vertex to analyze.

## Output Generation:

### ***1. Short Distance(Portland->Salem):***
    Dijkstra - 
        Running Dijkstra's Algorithm...
        Path: Portland -> Salem
        Total Distance: 47.0
        Vertices Explored: 2
        Edges Evaluated: 
        Time taken: 0.000083 seconds
        
    GBFS - 
        Running Greedy Best-First Search...
        Path: Portland -> Salem
        Total Distance: 47.0
        Vertices Explored: 2
        Edges Evaluated: 4
        Time taken: 0.000123 seconds
        
    A* - 
        Running A* Search Algorithm...
        Path: Portland -> Salem
        Total Distance: 47.0
        Vertices Explored: 2
        Edges Evaluated: 4
        Time taken: 0.000126 seconds

### ***2. Medium Distance(Portland->Eugene):***
    Dijkstra - 
        Running Dijkstra's Algorithm...
        Path: Portland -> Salem -> Eugene
        Total Distance: 111.0
        Vertices Explored: 7
        Edges Evaluated: 17
        Time taken: 0.000089 seconds
        
    GBFS - 
        Running Greedy Best-First Search...
        Path: Portland -> Salem -> Eugene
        Total Distance: 111.0
        Vertices Explored: 3
        Edges Evaluated: 7
        Time taken: 0.000122 seconds
        
    A* - 
        Running A* Search Algorithm...
        Path: Portland -> Salem -> Eugene
        Total Distance: 111.0
        Vertices Explored: 3
        Edges Evaluated: 7
        Time taken: 0.000148 seconds

### ***3. Long Distance(Portland->Ashland):***
    Dijkstra - 
        Running Dijkstra's Algorithm...
        Path: Portland -> Salem -> Eugene -> Roseburg -> Medford -> Ashland
        Total Distance: 283.0
        Vertices Explored: 21
        Edges Evaluated: 51
        Time taken: 0.000127 seconds
        
    GBFS - 
        Running Greedy Best-First Search...
        Path: Portland -> Newport -> Florence -> Coos_Bay -> Roseburg -> Medford -> Ashland
        Total Distance: 412.0
        Vertices Explored: 7
        Edges Evaluated: 18
        Time taken: 0.000146 seconds
        
    A* - 
        Running A* Search Algorithm...
        Path: Portland -> Salem -> Eugene -> Roseburg -> Medford -> Ashland
        Total Distance: 283.0
        Vertices Explored: 8
        Edges Evaluated: 23
        Time taken: 0.000179 seconds

### ***4. Diagonal Route(Portland->Burns):***
    Dijkstra -
        Running Dijkstra's Algorithm...
        Path: Portland -> Hood_River -> The_Dalles -> Madras -> Redmond -> Bend -> Burns
        Total Distance: 351.0
        Vertices Explored: 23
        Edges Evaluated: 53
        Time taken: 0.000145 seconds
        
    GBFS - 
        Running Greedy Best-First Search...
        Path: Portland -> Hood_River -> The_Dalles -> Madras -> Redmond -> Bend -> Burns
        Total Distance: 351.0
        Vertices Explored: 7
        Edges Evaluated: 16
        Time taken: 0.000147 seconds
        
    A* - 
        Running A* Search Algorithm...
        Path: Portland -> Hood_River -> The_Dalles -> Madras -> Redmond -> Bend -> Burns
        Total Distance: 351.0
        Vertices Explored: 10
        Edges Evaluated: 27
        Time taken: 0.000197 seconds

### ***5. Long Coastal vs. Inland(Portland->Medford):*** 
    Dijkstra - 
        Running Dijkstra's Algorithm...
        Path: Portland -> Salem -> Eugene -> Roseburg -> Medford
        Total Distance: 268.0
        Vertices Explored: 20
        Edges Evaluated: 48
        Time taken: 0.000118 seconds
    GBFS - 
        Running Greedy Best-First Search...
        Path: Portland -> Newport -> Florence -> Coos_Bay -> Roseburg -> Medford
        Total Distance: 397.0
        Vertices Explored: 6
        Edges Evaluated: 15
        Time taken: 0.000135 seconds
    A* - 
        Running A* Search Algorithm...
        Path: Portland -> Salem -> Eugene -> Roseburg -> Medford
        Total Distance: 268.0
        Vertices Explored: 6
        Edges Evaluated: 18
        Time taken: 0.000164 seconds

## Algorithm Analysis:
### ***Empirical Observations -***
The three algorithms(Dijkstra, GBFS, A*) being compared return similar results but arrive in different ways. When comparing over the 5 test results above, GBFS consistently returns the lowest amount of vertices explored and edges evaluated. Two specific cases I would like to examine are Portland to Ashland and Portland to Medford. The results were 7 vertices explored and 18 edges evaluated for Portland to Ashland as well as 6 vertices explored and 15 edges evaluated for Portland to Medford. At first glance this seems like GBFS performed optimally compared to Dijkstra and A* when examining the edges evaluated and vertices explored, however this is not the case. In the Portland to Ashland case, GBFS total distance was 412. In the Portland to Medford case, GBFS total distance was 397. This is nearly double the distance that A* and Dijkstra found. In both cases, GBFS actually took significantly longer paths compared to Dijkstra and A*. This is because the algorithm specifically focuses on the smallest heuristic estimate, leading to going down paths with significantly higher weights. Another important case to examine is Portland to Eugene. Dijkstra, GBFS, and A* all found the same path, however, Dijkstra explored 7 vertices and 17 edges while GBFS and A* both explored 3 vertices and 7 edges. This highlights the exhaustive nature of Dijkstra's algorithm.
### ***Use Case Analysis -***
Because Dijkstra's algorithm doesn't require a heuristic, this makes it excel in cases where you have a non-admissable heuristic. Although the algorithm was slower, it guaranteed accuracy among all test cases.
A* is a great middle ground between the exhaustiveness of Dijkstra's algorithm and the speed of GBFS, when the heuristic is admissable. For example, examining the Portland to Medford case, A* found the same optimal path as Dijkstra's algorithm but only by exploring 6 vertices and 18 edges versus Dijkstra's 20 vertices and 48 edges. GBFS can be very quick compared to both Dijkstra and A*, however, because prioritizes the heuristic and doesn't take into consideration the path weight, this can lead to much less optimal paths. For example, the Portland to Ashland case where GBFS originally seemed quicker with less vertices and edges explored than A*, however, it found a much less optimal path of 412 versus 283. All three have their use cases, Dijkstra excels when you need guranteed accuracy and aren't as worried about time, GBFS for when time and space is of the essence and the implementation doesn't require the most optimal path, and A* for a balance between Dijkstra and GBFS when an admissable heuristic is provided. 
### ***Runtime Complexity Analysis -***
All three algorithms share the same worst case time complexity and space complexity. Initializing the starts distance to 0 and all other nodes distances to infinity takes O(V) where V is the number of vertices. For the priority queue, each vertex is popped at most once and each edge may push once. Meaning that V + E is the total number of heap operations. Each of the push or pop operations take O(log n) where n is the size of the heap. In the worst case, the heap may contain E elements, meaning O(log E) for each operation. This gives an overall time complexity of O(V + E log E). For the space complexity, each dictionary and set stores up to O(V) the heap may contain up to E elements, therefore, O(V + E). The differences in average performance rely on what the algorithm prioritizes. Dijkstra's prioritizes path cost, GBFS's prioritizes the heuristic estimate, and A*'s prioritizes the combination of the two. Because the Oregon map size (|V| = 22, |E| = 52) is small, runtime performance between the three seems miniscule, however on sizes much larger such as the entire US highway system, the differences in exploration and runtime would be visualized much greater. For example, Dijkstra's algorithm will continue to be accurate but its exhaustive nature will cause it to take significantly more time large scale. Both GBFS and A* rely on an admissable heuristic. 
### ***Heuristic Discussion -***
To be admissable, the heuristic must not overestimate the actual distance of the path. The reason the haversine distance is admissable is because it is a straight line distance from one set of coordinates to another set of coordinates. By nature, roads will always either equal the straight line distance or take longer with detours. When the heuristic underestimates heavily, it can cause GBFS to explore paths that seem closer to the goal but end up needing significantly longer detours. I cannot imagine a more admissable heuristic than the haversine considering the haversine gurantees atleast an admissable heuristic, however, I believe that it would be interesting to explore other heuristic options.
    
