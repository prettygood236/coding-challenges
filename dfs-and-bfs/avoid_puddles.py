# ---
# title: Avoid Puddles
# tags: [CodingChallenges, Python, BFS]
# created: '2023-12-12'
# ---

# ## Problem Description

# Due to continuous heavy rain, some areas are flooded. You are trying to go to school through areas that are not submerged. The path from home to school can be represented as an m x n grid.

# For example, the picture below represents a case where m = 4 and n = 3.


# The top left corner (home) is represented by coordinates (1, 1), and the bottom right corner (school) is represented by coordinates (m, n).

# Given the size of the grid m, n and a 2D array puddles containing coordinates of flooded areas as parameters, write a solution function that returns the remainder of dividing by 1,000,000,007 the number of shortest paths you can only move right and down from home to school.

# ## Solution

# This problem can be solved using breadth-first search (BFS). The idea is to traverse the grid from the start point to the end point, only moving right and down, while avoiding puddles.

# Here's how this looks in Python:

# ```python
from collections import deque

def solution(m,n,puddles):
    answer = bfs(m,n,puddles)
    return answer

def bfs(m,n,puddles):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 'PUDDLE'
    for i in puddles:
        x,y = i
        dp[y-1][x-1] = 'PUDDLE'
    queue = deque()
    queue.append((1,1,0))
    # right down left up
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    result = 0
    while queue:
        print(queue)
        print(dp)
        x,y,d = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nd = d + 1
            if nx < 1 or nx > m or ny < 1 or ny > n:
                continue
            if dp[ny-1][nx-1] == 'PUDDLE':
                continue
            if dp[ny-1][nx-1] == 0:
                dp[ny-1][nx-1] = nd
            if dp[ny-1][nx-1] < nd:
                continue
            if nx == m and ny == n:
                result = (result%1000000007) + 1
            else:
                queue.append((nx,ny,nd))
    return result

# m = 4
# n = 3 
# puddles	= [[2, 2]]
# 4

# m = 100
# n = 100
# puddles	= [[2, 2],[13,14],[3,52],[6,77],[53,79],[99,99]]

m = 10
n = 10
puddles	= [[2, 2],[6,9],[9,9]]

print(solution(m,n,puddles))