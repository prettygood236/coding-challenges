# ---
# title: Maximum Sum in Staircase with No Consecutive Steps
# tags: [CodingChallenges, Python, DynamicProgramming]
# created: '2022-11-07'
# ---

# ## Problem Description

# Given a staircase with 'n' steps and an array of 'n' numbers where each number represents the score that can be gained by stepping on that step. You may climb 1 or 2 steps at a time but cannot take two consecutive steps. The goal is to find the maximum score you can achieve.

# ## Solution

# The solution uses dynamic programming to calculate the maximum score for each step considering whether we take this step or not and if we do, whether we took previous step or skipped it. 

# Here's how this looks in Python:

# ```python
n = int(input())
l = [[] for _ in range(n)] 

for i in range(n):
    t = int(input())
    if i == 0 :
        l[0].append(t)
    if i == 1:
        l[1].append(l[0][0])
        l[1].append(t)
        l[1].append(l[0][0]+t)
    if i >= 2:
        l[i].append(max(l[i-1]))
        l[i].append(max(l[i-2])+t)
        l[i].append(l[i-1][1]+t)

print(max(l[-1]))
