# ---
# title: Network Count
# tags: [CodingChallenges, Python, DFS, Graphs]
# created: '2023-12-10'
# ---

# ## Problem Description

# A network refers to a configuration where computers are interconnected to exchange information. For example, if computer A and computer B are directly connected, and computer B and computer C are directly connected, then computer A and computer C are indirectly connected and can exchange information. Thus, computers A, B, and C can all be said to be in the same network.

# Given the number of computers `n` and a 2D array `computers` representing the connections, write a function `solution` to return the number of networks.

# ## Constraints

# - The number of computers `n` is a natural number between 1 and 200.
# - Each computer is represented as an integer from 0 to n-1.
# - If the i-th and j-th computers are connected, `computers[i][j]` is represented as 1.
# - `computer[i][i]` is always 1.

# ## Solution

# The solution uses Depth-First Search (DFS) to traverse each network. It uses a boolean array `visited` to track the visited nodes. For each unvisited node, it performs a DFS and increments the network count.

# ```python
def solution(n, computers):
    def dfs(i):
        visited[i] = True
        for j in range(n):
            if visited[j] != True and computers[i][j] == 1:
                dfs(j)
        return
    
    visited = [False] * n
    answer = 0
    for i in range(n):
        if visited[i] != True:
            dfs(i)
            answer += 1 
    return answer

n = 3	
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	
print(solution(n,computers)) # 2
n = 3	
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]	
print(solution(n,computers)) # 1
