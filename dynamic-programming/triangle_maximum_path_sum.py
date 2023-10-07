# ---
# title: Triangle Maximum Path Sum
# tags: [CodingChallenges, Python, DynamicProgramming]
# created: '2022-11-07'
# ---

# ## Problem Description

# Given a triangle array, return the maximum path sum from top to bottom. For each step, you may move to an adjacent number of the row below.

# ## Solution

# This problem can be solved by using dynamic programming with time complexity O(n^2) where n is number of rows in the triangle.


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
