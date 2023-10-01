
#* Kruskal's Algorithm: Kruskal's algorithm works regardless of starting point. 
#* This method sorts edges in ascending order and repeatedly searches and selects minimum-cost edges that do not form cycles to create an MST.

# Importing necessary modules
from operator import itemgetter

def kruskal(n, costs):
    # Sort the edges in ascending order of their weights (costs)
    costs.sort(key=itemgetter(2))
    
    # Initialize the parent list. At the start, each node is its own parent.
    parent = [i for i in range(n)]
    
    # This function returns the root of the given node.
    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]
    
    # This function joins two subsets into a single set by linking roots.
    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        
        if root1 != root2:
            parent[root2] = root1
    
    # Initialize total cost to zero
    total_cost = 0
    
    for cost in costs:
        u, v, w = cost
        
        # If u and v are not already in same set then add it to result and perform union
        if find(u) != find(v):
            union(u,v)
            total_cost += w
            
     return total_cost  # Return final minimum spanning tree's weight.

