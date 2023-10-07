# ---
# title: Tiling
# tags: [CodingChallenges, Python, DynamicProgramming]
# created: '2022-11-05'
# ---

# ## Problem Description
# Given a 2 x N rectangle and tiles of size 2 x 1, count the number of ways to tile the given rectangle using these tiles.

# ## Constraints
# - The input consists of an integer N (1 ≤ N ≤ 1000000).

# ## Solution
# We use dynamic programming to solve this problem. We define dp[i] as the number of ways to fill a grid of size i. Then we have dp[i] = dp[i-1] + dp[i-2].

# ```python
N = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    # Memory optimization by storing remainder (according to remainder theorem, the remainder of the sum is equal to the sum of the remainders)
    dp[i] = (dp[i-1] + dp[i-2])%15746

print(dp[N])

