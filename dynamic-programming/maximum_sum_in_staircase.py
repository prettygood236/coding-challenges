# ---
# title: Maximum Sum in Staircase
# tags: [CodingChallenges, Python, DynamicProgramming]
# created: '2022-11-07'
# ---

# ## Problem Description

# Given a staircase with 'n' steps and an array of 'n' numbers where each number represents the maximum possible score that can be gained by stepping on that step. You may climb 1 or 2 steps at a time. When you move to the step, you get the score of that step. The goal is to find the maximum score you can achieve.

# ## Solution

# ```python
n = int(input())
l = []

for i in range(n):
  num = int(input())
  if i == 0:
    l.append([num])
  if i == 1:
    l.append([l[0][0]+num])
    l[i].append(num)
  if i >= 2:
    l.append([num+l[i-1][1]])
    l[i].append(num+max(l[i-2]))

print(max(l[-1]))

