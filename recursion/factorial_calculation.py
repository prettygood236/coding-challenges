# ---
# title: Factorial Calculation
# tags: [CodingChallenges, Python, Recursion]
# created: '2022-09-08'
# ---

# ## Problem Description

# The factorial of a non-negative integer `N` is the product of all positive integers less than or equal to `N`. It is denoted by `N!`. Write a function that calculates factorial of given number.

# ## Solution

# This problem can be solved using recursion. The idea is to return factorial of `N` by multiplying `N` with factorial of `(N-1)`. Base case is when `N` is 0 or 1.


# ```python
def factorial(N):
  if N <= 1:
    return 1
  else:
    return N * factorial(N-1)
