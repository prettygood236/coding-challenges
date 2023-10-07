# ---
# title: Function w with Memoization
# tags: [CodingChallenges, Python, DynamicProgramming, Memoization]
# created: '2023-10-05'
# ---

# ## Problem Description

# In this problem, we are implementing a function `w(a,b,c)` defined as follows:

# w(a, b, c) = 1 if a<=0 or b<=0 or c<=0
# w(a, b, c) = w(20, 20, 20) if a>20 or b>20 or c>20
# w(a, b ,c) = w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c) if a<b<c
# w(a,b,c)= w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c - 1)-w(a-1,b-1,c-2) otherwise.


# The goal is to implement the function using dynamic programming with memoization to avoid redundant calculations.

# ## Constraints

# The input consists of three integers `a`, `b`, and `c` (-50 ≤ a,b,c ≤ 50).

# ## Solution

# We use memoization technique where we store the results of expensive function calls and reuse them when same inputs occur again. This is done by creating a three-dimensional list `dp` that stores the results of each call to `w`.

# ```python
dp = [[[0]*21 for _ in range(21)] for _ in range(21)]

def w(a,b,c):
  #. Exit condition 
  if a<=0 or b<=0 or c<=0:
    return 1
  if a>20 or b>20 or c>20:
    return w(20,20,20)

  #. If the problem has already been calculated, return it as is.
  if dp[a][b][c]:
    return dp[a][b][c]

  if a<b<c :
    dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    return dp[a][b][c]
  dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
  return dp[a][b][c]
  

while True:
  a,b,c = map(int,input().split())
  if a==-1 and b==-1 and c==-1:
    exit()
  w(a,b,c)
  print(f'w({a}, {b}, {c}) = {w(a,b,c)}')
