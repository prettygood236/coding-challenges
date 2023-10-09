# ---
# title: Cantor Set
# tags: [CodingChallenges, Python, Recursion]
# created: '2022-09-10'
# ---

# ## Problem Description

# The Cantor set is a fractal described as the intersection of an infinite sequence of closed sets. It is created by repeatedly deleting the open middle third of a set of line segments.

# Write a function that generates `N`th iteration of Cantor set.

# ## Solution

# This problem can be solved using recursion. The idea is to generate `N`th iteration by concatenating `(N-1)`th iteration, middle third spaces and `(N-1)`th iteration again.


# ```python
def cantor(str,N):
  if N == 0:
    return '-'
  else:
    return cantor(str,N-1)+' '*(3**(N-1))+cantor(str,N-1)

while True:
  try:
    N = int(input())
    print(cantor('',N))
  except EOFError:
    break
