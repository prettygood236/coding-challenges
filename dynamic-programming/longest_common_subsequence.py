# ---
# title: Longest Common Subsequence (LCS)
# tags: [CodingChallenges, Python, DynamicProgramming]
# created: '2022-11-08'
# ---

# ## Problem Description

# The longest common subsequence (LCS) problem is the problem of finding the longest subsequence common to all sequences in a set of sequences (often just two sequences). 
# It differs from the longest common substring problem: unlike substrings, subsequences are not required to occupy consecutive positions within the original sequences.

# ## Solution

# This problem can be solved by using dynamic programming with time complexity O(N^2).

# ### Dynamic Programming Approach

# ```python
x = input()
y = input()
dp = [[0] * (len(y)+1) for _ in range(len(x)+1)]

for i in range(1,len(x)+1):
  for j in range(1,len(y)+1):
    if x[i-1] == y[j-1]:
      dp[i][j] = dp[i-1][j-1] + 1
    else :
      dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[-1][-1])

