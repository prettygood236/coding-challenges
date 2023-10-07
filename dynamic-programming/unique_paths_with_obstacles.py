# ---
# title: Unique Paths with Obstacles
# tags: [CodingChallenges, Python, DynamicProgramming]
# created: '2022-11-08'
# ---

# ## Problem Description

# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path. However, there are obstacles in the form of puddles represented by their coordinates. You cannot pass through an obstacle.

# ## Solution

# This problem can be solved by using dynamic programming with time complexity O(m*n) where m is number of rows and n is number of columns.

# ### Dynamic Programming Approach

# ```python
def solution(m, n, puddles):
    dp = [[0]*m for _ in range(n)]

    for puddle in puddles:
        a,b = puddle
        dp[b-1][a-1] = -1

    dp[0][0] = 1
    mod = 1_000_000_007

    for i in range(n):
        for j in range(m):
            if (i==0 and j==0) or dp[i][j] == -1:
                continue
            if dp[i-1][j] != -1:
                dp[i][j] += dp[i-1][j]
            if dp[i][j-1] != -1:
                dp[i][j] += dp[i][j-1]
            dp[i][j] %= mod

    return dp[n-1][m-1]

m = 4
n = 3
puddles = [[2,2]]
print(solution(m,n,puddles)) # Expected output: 4

m = 100
n = 100
puddles = [[2,2]]
print(solution(m,n,puddles))
