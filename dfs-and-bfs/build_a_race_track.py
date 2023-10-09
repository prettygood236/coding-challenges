# ---
# title: Build a Race Track
# tags: [CodingChallenges, Python, BFS]
# created: '2022-08-23'
# ---

# # Build a Race Track

# ## Problem Description

# Given a grid of size N x N where 0 represents an empty space and 1 represents an obstacle, find the minimum cost to build a race track from the top-left corner to the bottom-right corner. The race track can be built in four directions (up, down, left, right) and it costs 100 to build one unit of road in the same direction and 600 to change direction (including initial construction cost).

# ## Constraints

# - The grid size N is between 3 and 25.
# - Each cell in the grid is either 0 or 1.

# ## Solution

# #? I really don't know why it's taking so long. Life is so hard when I can't figure out why it's exceeding the time limit.
# #? (Addition) Maybe because it's a 25x25 BFS, you little rascal?

# ```python
# from collections import deque

# def solution(board):
#     def bfs(y,x):
#         n = len(board)
#         dp = [[[int(1e9)]*n for _ in range(n)] for _ in range(4)]
#         for i in range(4):
#             dp[i][0][0] = 0 
#         queue = deque()
#         dir = -1
#         cost = 0
#         queue.append((0,0,dir,cost))
#     # right down left up
#         dy = [0,1,0,-1]  
#         dx = [1,0,-1,0]
        
#         while queue:
#             y,x,_dir,cost = queue.popleft()
#             for i in range(4):
#                 ny = y + dy[i]
#                 nx = x + dx[i]

#                 if nx < 0 or nx >= n or ny < 0 or ny >= n:
#                     continue
#                 if board[ny][nx]:
#                     continue
                
#                 c = cost + (100 if _dir == i or _dir == -1 else 600)
                
#                 if dp[i][ny][nx] >= c:
#                     dp[i][ny][nx] = c
#                     queue.append((ny,nx,i,c))
#     answer = int(1e9)
#     for i in range(4):
#         answer = min(answer,dp[i][n-1][n-1])
#     return answer
# ```

# ```python
def solution(board):
    n = len(board)
    dp = [[[0]*n for _ in range(n)] for _ in range(4)]
    for i in range(n):
      for j in range(n):
          dfs(i,j,0,0,dp)
    # answer = min(dp[n-1][n-1])
    return 


def dfs(y,x,dir,cost,dp):
    n = len(board)
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return
    if board[y][x] == 1:
        return
    if dp[dir][y][x]:
        return
    print(dp)
    for i in range(4):
        if dir == i:
          cost += 100
        else:
          cost += 600
        dp[i][y][x] = cost
        dfs(y,x+1,i,cost,dp)
        dfs(y+1,x,i,cost,dp)
        dfs(y,x-1,i,cost,dp)
        dfs(y-1,x,i,cost,dp)
    return 

board = [[0,0,0],[0,0,0],[0,0,0]] #900
# board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]	#3800
# board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]	#2100
# board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]	#3200
solution(board)
