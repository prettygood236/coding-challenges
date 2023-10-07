# ---
# title: Maximum Subarray
# tags: [CodingChallenges, Python, DynamicProgramming, KadanesAlgorithm]
# created: '2022-11-07'
# ---

# ## Problem Description

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# ## Solution

# This problem can be solved by using dynamic programming with time complexity O(n) where n is size of input array. The approach used here is known as Kadane's algorithm.

# ### Kadane's Algorithm Approach

# ```python
n = int(input())
l = list(map(int,input().split()))

for i in range(1,len(l)):
  l[i] = max(l[i],l[i-1]+l[i])

print(max(l))
