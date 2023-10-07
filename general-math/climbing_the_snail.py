# ---
# title: Climbing the Snail
# tags: [CodingChallenges, Python, Math]
# created: '2022-07-04'
# ---

# # Climbing the Snail

# ## Problem Description

# In this problem, a snail wants to climb up a tree of height V meters. During the day, the snail can climb A meters and at night while it sleeps, it slips down B meters. However, during the last day when it reaches or surpasses V meters, it does not slip down. Your task is to find out how many days does it take for the snail to reach or surpass V meters.

# ## Constraints

# - The input consists of three integers A,B,V (1 ≤ B < A ≤ V ≤ 1,000,000,000).

# ## Solution

# We use simple math to solve this problem. We first calculate how much distance d is left after climbing on first day which is (V-A). Then we calculate how many days are required to cover this distance which is d/(A-B). Since number of days should be an integer we take ceil value of this calculation and add 1 for first day.

# ```python
import math

A,B,V = map(int,input().split())
d = (V-A)/(A-B)

print(math.ceil(d)+1)
