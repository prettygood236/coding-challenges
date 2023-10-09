# ---
# title: Print All Combinations (DFS)
# tags: [CodingChallenges, Python, DFS]
# created: '2022-08-21'
# ---

# # Print All Combinations (DFS)

# ## Problem Description

# Given two integers N and M, print all possible combinations of M numbers from 1 to N. 

# ## Constraints

# - 1 <= N <= 8
# - 1 <= M <= min(8,N)

# ## Solution

# This problem can be solved using depth-first search (DFS). The idea is to add each number from 1 to N into a list and recursively call the function until the list contains M numbers. If a number is already in the list, it is skipped.

# ```python
def solution(N,M):
    s = []

    def dfs():
      if len(s) == M:
        print(' '.join(map(str,s)))
        return

      for i in range(1,N+1):
        if i not in s:
          s.append(i)
          dfs()
          s.pop()

    dfs()
