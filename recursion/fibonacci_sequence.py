# ---
# title: Fibonacci Sequence
# tags: [CodingChallenges, Python, Recursion]
# created: '2022-09-08'
# ---

# ## Problem Description

# The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. Write a function that calculates `N`th number in Fibonacci sequence.

# ## Solution

# This problem can be solved using recursion. The idea is to return `N`th Fibonacci number by adding `(N-1)`th and `(N-2)`th Fibonacci numbers. Base cases are when `N` is 0 or 1.


# ```python
def fibonacci(N):
  if N == 0:
    return 0
  if N == 1:
    return 1
  else :
    return fibonacci(N-1) + fibonacci(N-2)
