# ---
# title: Counting Stair Numbers
# tags: [CodingChallenges, Python, DynamicProgramming]
# created: '2022-11-07'
# ---

# ## Problem Description

# A stair number is a number that consists of digits where each digit has a difference of 1 with its adjacent digits. For example, `123`, `321`, `454` are stair numbers while `145`, `332` are not. Given an integer 'n', calculate how many stair numbers of length 'n' exist.

# ## Solution

# The solution uses dynamic programming to count the number of stair numbers for each length from 2 to n. For each digit from 0 to 9 at every step, we calculate the count considering previous and next digit (as they differ by one). 

# Here's how this looks in Python:

# ```python
n = int(input())

dp = [[0]*10 for _ in range(n+1)]
dp[0] = []
for i in range(1,10):
    dp[1][i] = 1

mod = 1000000000

for i in range(2,n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n])%mod)
