# ---
# title: Knapsack Problem
# tags: [CodingChallenges, Python, DynamicProgramming]
# created: '2022-11-08'
# ---

# ## Problem Description

# The knapsack problem is a problem in combinatorial optimization. Given a set of items, 
# each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

# ## Solution

# This problem can be solved by using dynamic programming with time complexity O(NW) where N is number of items and W is maximum weight.

# ### Dynamic Programming Approach

# ```python
n, k = map(int,input().split())
wt = []
v = []
for _ in range(n):
  a,b = map(int,input().split())
  wt.append(a)
  v.append(b)

def knapSack(W, wt, v, n):
    dp = [0 for _ in range(W+1)] 
    for i in range(1,n+1): 
      for w in range(W,0,-1): 
        if wt[i-1] <= w:
          dp[w] = max(dp[w], dp[w-wt[i-1]] + v[i-1])
    print(dp)
    return dp[W]  

print(knapSack(k, wt, v,n))
