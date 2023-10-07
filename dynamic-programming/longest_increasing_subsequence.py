# ---
# title: Longest Increasing Subsequence (LIS)
# tags: [CodingChallenges, Python, DynamicProgramming]
# created: '2022-11-07'
# ---

# ## Problem Description

# The longest increasing subsequence problem is to find a subsequence of a given sequence in which the subsequence's elements are in sorted order, lowest to highest, and in which the subsequence is as long as possible. 
# This subsequence is not necessarily contiguous or unique.

# ## Solution

# There are two popular ways to solve this problem:

# 1. Using dynamic programming with time complexity O(N^2)
# 2. Using segment tree with time complexity O(NlogN) (we will cover this after learning segment trees)

# ### Dynamic Programming Approach

# In this approach, we create an array D where each index represents the length of the longest increasing subsequence ending at that index. 
# For each element at index i, we check all previous elements and update D[i] accordingly.


# ```python
N = int(input())
A = list(map(int,input().split()))
D = [0] * N

for i in range(N):
  D[i] = 1
  for j in range(i):
    if A[i] > A[j]:
      D[i] = max(D[i],D[j]+1)
    
print(max(D))
# ```


# ### Segment Tree Approach (To be continued...)

# ```python
# from itertools import chain
# n = int(input())
# a = list(map(int,input().split()))
# dp = [[0,0] for _ in range(n)]

# for i in range(n):
#   dp[i][0] = 1
#   dp[i][1] = 1
#   for j in range(i):
#     if a[i] > a[j]:
#       dp[i][0] = max(dp[i][0],dp[j][0]+1)
#     if a[j] > a[i]:
#       dp[i][1] = max(dp[i][1],dp[j][0]+1,dp[j][1]+1)

# print(max(list(chain(*dp)))) 
# ```

# In the segment tree approach, we will sort the array and apply dynamic programming on it using segment trees which will reduce our time complexity to O(NlogN). 
# However, understanding of segment trees is required before implementing this solution.

# ### Applying LIS on pairs

# This approach is an extension of LIS where instead of working on single numbers we work on pairs.
# Here first we sort our pairs based on first element then apply LIS on second element.

# ```python
# n = int(input())
# a = [list(map(int,input().split())) for _ in range(n)]
# a.sort()
# dp = [0] * n

# for i in range(n):
#   dp[i] = 1
#   for j in range(i):
#     if a[i][1] > a[j][1]:
#       dp[i] = max(dp[i],dp[j]+1)

# print(n-max(dp))
# ```