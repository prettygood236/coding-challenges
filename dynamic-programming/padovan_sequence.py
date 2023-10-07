# ---
# title: Padovan Sequence
# tags: [CodingChallenges, Python, DynamicProgramming]
# created: '2022-11-05'
# ---

# ## Problem Description
# Given an integer N, find the Nth number in Padovan sequence. The Padovan sequence is defined as P(n) = P(n-2) + P(n-3) for n > 4 and initial values are P(1)=P(2)=P(3)=1, P(4)=2.

# ## Constraints
# The input consists of an integer T which represents the number of test cases (1 ≤ T ≤ 1000), followed by T lines each containing an integer N (1 ≤ N ≤ 100).

# ##Solution
# We use dynamic programming to solve this problem. We define dp[i] as the ith number in Padovan sequence. Then we have dp[i] = dp[i-2] + dp[i-3].

# ```python
T = int(input())
for _ in range(T):
    N = int(input())
    dp = [0] * 101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    
    for i in range(5, N+1):
        dp[i] = dp[i-2] + dp[i-3]
    
    print(dp[N])
