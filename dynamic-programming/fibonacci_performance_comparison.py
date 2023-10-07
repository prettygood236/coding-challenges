# ---
# title: Fibonacci Performance Comparison
# tags: [CodingChallenges, Python, Recursion, DynamicProgramming]
# created: '2022-11-05'
# ---

# ## Problem Description

# In this problem, we are comparing the performance of two methods for calculating the nth Fibonacci number: recursion and dynamic programming. The goal is to count how many operations each method takes to calculate the nth Fibonacci number.

# ## Constraints

# - The input is an integer n (1 ≤ n ≤ 40).

# ## Solution

# We implement both recursive and dynamic programming solutions for finding the nth Fibonacci number. 

# In `recur_fib(n)`, we use a simple recursive approach which follows directly from the definition of Fibonacci sequence. However this approach leads to a lot of repeated calculations which increases its time complexity exponentially.

# In `dp_fib(n)`, we use dynamic programming to store already calculated values in an array `dp`. This way when we need them again, instead of recalculating them we simply retrieve them from `dp` array.

# Finally, we compare operation counts for both methods by running them with same input and printing out their operation counts.

# ```python
n = int(input())
recur_count = 0
dp_count = 0

def recur_fib(n):
  global recur_count
  if n == 1 or n == 2 :
    recur_count += 1
    return 1
  else :
    return recur_fib(n-1) + recur_fib(n-2)

dp = [0] * (n+1)
def dp_fib(n):
  global dp_count
  dp[1] = dp[2] = 1 
   
  
  k =3 
  while k <= n:
      dp[k] = dp[k - 1] + dp[k -2]
      k +=1 
      dp_count +=1 


recur_fib(n)
dp_fib(n)

print(recur_count, dp_count)
