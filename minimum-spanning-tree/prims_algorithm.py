
#* A Minimum Spanning Tree (MST) is one of the key concepts in graph theory. 
#* It refers to a tree in a weighted undirected graph where the sum of weights of all edges is minimized while connecting all nodes.

# A Spanning Tree is a graph that connects all nodes while satisfying the properties of a tree. In other words, a spanning tree should include all nodes from the original graph and have no cycles.

# Among these, the "minimum" spanning tree refers to the spanning tree where the sum of edge weights is minimal. In other words, it finds the smallest possible sum of edge weights among all possible spanning trees within a given graph.

# To find an MST, Kruskal's algorithm or Prim's algorithm are typically used.

#* Prim's Algorithm: Prim's algorithm can produce different results depending on its starting point. 
#* This method starts from any arbitrary point and selects minimum-cost edges connected to that point to create an MST.

# The basic principle shared by both algorithms is minimizing 'total cost' during 'edge search and selection' process while including 'all nodes' without forming any 'cycles'.

# Minimum Spanning Trees are utilized in various fields such as network design, pathfinding, clustering, etc.
import heapq  # Importing the heapq module for priority queue operations

def solution(n, costs):
    adj = [[] for _ in range(n)]  # Initializing an adjacency list to store connections between nodes
    
    # Building the adjacency list
    for c in costs:
        a, b, cost = c  # Unpacking the node-node-cost triplet
        adj[a].append((cost, b))  # Adding an edge from 'a' to 'b' with weight 'cost'
        adj[b].append((cost, a))  # Adding an edge from 'b' to 'a' with weight 'cost'
    
    # Initializing Prim's algorithm
    connected_nodes = [0]  # Starting from node 0 (or any arbitrary node)
    candidate_edge_list = adj[0]  # All edges connected to node 0 are potential candidates for MST
    heapq.heapify(candidate_edge_list)  # Turning candidate_edge_list into a heap structure (priority queue)
    
    total_cost = 0   # This will hold the total cost of MST
    
    while candidate_edge_list:   # While there are still edges that might be added to MST 
        cost, b = heapq.heappop(candidate_edge_list)   # Pop and retrieve the edge with smallest cost
        
        if b not in connected_nodes:   # If this edge leads to a node not yet included in MST 
            connected_nodes.append(b)   # Add this new node into our MST nodes set 
            total_cost += cost          # Increase total_cost by adding current smallest cost
            
            for edge in adj[b]:         ## Check all edges starting from our newly added node 
                if edge[1] not in connected_nodes:   
                    heapq.heappush(candidate_edge_list, edge)  
                    ## If those edges lead to nodes that are not yet included,
                    ## add them as candidates into our heap.

    return total_cost     ## When no more nodes left outside of our tree,
                          ## return the final calculated minimum spanning tree's weight.
