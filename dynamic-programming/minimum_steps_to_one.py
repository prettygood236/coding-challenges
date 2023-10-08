# ---
# title: Minimum Steps to One
# tags: [CodingChallenges, Python, DynamicProgramming]
# created: '2022-11-07'
# ---

# ## Problem Description

# Given a number 'n', find the minimum number of steps that take 'n' to 1. You can perform any one of the following 3 steps:

# 1. Subtract 1 from it. (n = n - 1)
# 2. If its divisible by 2, divide by 2.( if n % 2 == 0 , then n = n / 2 )
# 3. If its divisible by 3, divide by 3.( if n % 3 == 0 , then n = n / 3 )

# ## Solution

# The solution uses dynamic programming to calculate the minimum steps required to reduce each value from `2` to `n` down to `1`. 
# The step count is minimized based on whether the current value is divisible by `2` or `3`, or needs to be reduced by subtracting `1`.

# ```python
n = int(input())
l = [0] * (n+1)

for i in range(2,n+1):
    l[i] = l[i-1]+1

    if i % 2 == 0:
        l[i] = min(l[i//2]+1,l[i])

    if i % 3 == 0:
        l[i] = min(l[i//3]+1,l[i])

print(l[n])
