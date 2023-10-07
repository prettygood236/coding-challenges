# ---
# title: Prim's Algorithm
# tags: [CodingChallenges, Python, GraphTheory, MinimumCostSpanningTree, PrimsAlgorithm]
# created: '2023-10-05'
# ---

# ## Problem Description

# Given an integer `n` representing number of vertices and list `costs` where each element in costs represent [vertex1, vertex2, edge_cost] between vertex1 and vertex2. You need to return minimum cost required to connect all vertices such that no cycle forms.

# Constraints:
# - The number of people trapped on an uninhabited island ranges from at least one up to 50,000.
# - Each individual's bodyweight ranges from at least 40 kg up to 240 kg.
# - The load capacity (weight limit) for each boat ranges from at least 40 kg up to 240 kg.
# - The load capacity for each boat will always be given larger than maximum individual bodyweight hence it will always be possible for everyone get rescued.


# ## Solution

# #* Graph: A mathematical structure consisting of a set of (1)nodes (or vertices) and a set of (2)edges that connect these nodes.
# #* Tree: A (1)connected graph (2)without cycles, in which all nodes are interconnected and there is exactly one path between any two nodes.
# #* Spanning Tree: A (1)subgraph of a given graph that includes all the nodes of the original graph and satisfies tree properties ((2)no cycles).
# #* Minimum Cost Spanning Tree: Among possible spanning trees, it refers to the spanning tree where the sum of edge (3)weights is minimal.

# # A Spanning Tree is a graph that connects all nodes while satisfying the properties of a tree. In other words, a spanning tree should include all nodes from the original graph and have no cycles.
# # Among these, the "minimum" spanning tree refers to the spanning tree where the sum of edge weights is minimal. In other words, it finds the smallest possible sum of edge weights among all possible spanning trees within a given graph.
# # To find an MST, Kruskal's algorithm or Prim's algorithm are typically used.

# # Prim's Algorithm: Prim's algorithm can produce different results depending on its starting point. 
# # This method starts from any arbitrary point and selects minimum-cost edges connected to that point to create an MST.

# # The basic principle shared by both algorithms is minimizing 'total cost' during 'edge search and selection' process while including 'all nodes' without forming any 'cycles'.
# # Minimum Spanning Trees are utilized in various fields such as network design, pathfinding, clustering, etc.

# #! Prim's algorithm
# #. 1. Select an arbitrary vertex and add it to the minimum spanning tree, then add all edges connected to that vertex into a priority queue.
# #. 2. Select the edge with the smallest cost from the priority queue.
# #. 3. If that edge connects two vertices already included in the minimum spanning tree, do nothing and move on. If that edge connects a vertex u included in the minimum spanning tree and a vertex V not included in it, then add that edge and vertex V to the minimum spanning tree. Afterwards, add all edges connecting vertex V and vertices not yet included in the minimum spanning tree to the priority queue.
# #. 4. Repeat steps 2 and 3 until V-1 edges are added to the minimum spanning tree.

# ```python
import heapq

def solution(n, costs):
    # Create an empty adjacency list
    graph = {i: {} for i in range(n)}

    # Fill the adjacency list with data from costs
    for frm, to, cost in costs:
        graph[frm][to] = cost
        graph[to][frm] = cost

    # Initialize an empty list to store the minimum spanning tree
    min_span_tree = []
    
    # Choose an arbitrary vertex (we'll choose the first one)
    start_vertex = 0
    
    # Create a priority queue and add all edges connected to the starting vertex
    edges = [(cost, start_vertex, to) for to, cost in graph[start_vertex].items()]
    
    heapq.heapify(edges)

    # Create a set to track visited vertices and add the starting vertex
    visited = set([start_vertex])

    while edges:
        # Select the edge with smallest cost from priority queue 
        cost, frm, to = heapq.heappop(edges)
         
        if to not in visited:
            visited.add(to)
            min_span_tree.append((frm,to,cost))
             
            for next_node,cost2 in graph[to].items():
                if next_node not in visited:
                    heapq.heappush(edges,(cost2,to,next_node))

    return sum(cost for frm,to,cost in min_span_tree)


# Test cases   
n = 4	
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	
print(solution(n, costs)) #4

