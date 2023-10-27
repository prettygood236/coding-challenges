# ---
# title: Shortest Path Count in a Grid
# tags: [CodingChallenges, Python, DynamicProgramming]
# created: '2023-10-15'
# ---

# ## Problem Description

# Due to continuous heavy rain, some areas are flooded. You are trying to go to school through areas that are not submerged. The path from home to school can be represented as an m x n grid.

# For example, the picture below represents a case where m = 4 and n = 3.

# [Image]

# The top left corner (home) is represented by coordinates (1, 1), and the bottom right corner (school) is represented by coordinates (m, n).

# Given the size of the grid m, n and a 2D array puddles containing coordinates of flooded areas as parameters, write a solution function that returns the remainder of dividing by 1,000,000,007 the number of shortest paths you can only move right and down from home to school.

# ## Solution

# This problem can be solved using dynamic programming. The idea is to keep track of all possible paths from start point to each cell in grid while avoiding puddles.


# ```python
def solution(m, n, puddles):
    dp = [[float('inf')]*m for _ in range(n)]
    mod = 1000000007

    for x,y in puddles:
        dp[y-1][x-1] = 0

    flag = 1
    for i in range(m):
        if dp[0][i] == 0:
            flag = 0
        dp[0][i] = flag
    flag = 1
    for i in range(n):
        if dp[i][0] == 0:
            flag = 0
        dp[i][0] = flag

    for i in range(1,n):
        for j in range(1,m):
            if dp[i][j] == 0:
                continue
            else:
                dp[i][j] = min(dp[i][j], (dp[i][j-1]+dp[i-1][j])%mod)

    return dp[-1][-1]

m = 4; n = 3; puddles= [[1, 2], [2, 2]]
print(solution(m, n, puddles)) #3
# ```

# [[Avoid Puddles]]