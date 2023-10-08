# ---
# title: Maximum Path Sum in Triangle
# tags: [CodingChallenges, Python, DynamicProgramming]
# created: '2023-10-08'
# ---

# ## Problem Description

# Given a triangle array of integers, find the maximum path sum from top to bottom. At each step, you may move to an adjacent number on the row below.

# ## Solution

# The solution uses dynamic programming to calculate the maximum path sum for each position. Starting from top, for each number in a row we calculate maximum possible sum by taking maximum of sums with two possible numbers above it (one directly above and one just previous) and adding current number.

# Here's how this looks in Python:

# ```python
def solution(triangle):
    dp = [[0]*len(x) for x in triangle]
    dp[0][0] = triangle[0][0]
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i-1])):
            dp[i][j] = max(dp[i][j],dp[i-1][j]+triangle[i][j])
            dp[i][j+1] = max(dp[i][j+1],dp[i-1][j]+triangle[i][j+1])
    return max(dp[-1])

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6 ,5]]	
print(solution(triangle)) # 30
# ```

# ```python
n = int(input())
l = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,len(l)):
  for j in range(len(l[i])):
    if j == 0:
      l[i][j] += l[i-1][j]
    elif j == len(l[i])-1:
      l[i][j] += l[i-1][len(l[i-1])-1]
    else:
      l[i][j] += max(l[i-1][j-1],l[i-1][j])

print(max(l[-1]))
