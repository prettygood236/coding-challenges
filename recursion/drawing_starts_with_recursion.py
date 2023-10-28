# ---
# title: Drawing Stars with Recursion
# tags: [CodingChallenges, Python, Recursion]
# created: '2023-09-08'
# ---

# ## Problem Description

# You are given a number N (N is a power of 3), and you are required to draw a star pattern of size N x N. The pattern should be such that a smaller star of size N/3 x N/3 is removed from the middle of the bigger star.

# ## Solution

# This problem can be solved using recursion in Python. The base case of the recursion is when N is 1, in which case we just return a single star. For larger N, we construct the pattern using three copies of the pattern for N/3, with spaces added in the middle for the second copy.


# ```python
def star_marking(N):
  if N == 1:
    return ['*']
  Star = star_marking(N//3)
  L = []

  for i in Star:
    L.append(i*3)
  for i in Star:
    L.append(i+' '*(N//3)+i)
  for i in Star:
    L.append(i*3)
  return L

import sys
N = int(sys.stdin.readline().strip())
print('\n'.join(star_marking(N)))
