# ---
# title: Minimum Cost Painting Houses
# tags: [CodingChallenges, Python, DynamicProgramming]
# created: '2022-11-07'
# ---

# ## Problem Description

# There are a row of `N` houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color. The cost of painting each house with a certain color is represented by an `N x 3` matrix.

# ## Solution

# This problem can be solved by using dynamic programming with time complexity O(n) where n is number of houses.

# ```python
N = int(input())
L = [list(map(int,input().split())) for _ in range(N)]

for i in range(1,len(L)):
  for j in range(3):
    L[i][j] += min(L[i-1][(j+1)%3],L[i-1][(j+2)%3])

print(min(L[-1]))
