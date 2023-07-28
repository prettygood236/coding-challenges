def solution(n):
    if n % 2 == 1:
        return 0
    dp = [0] * (n+1)
    dp[0], dp[2] = 1, 3
    
    mod = 1000000007

    for i in range(4, n+1, 2):
        dp[i] = dp[i-2] * dp[2]
        for j in range(i-4, -1, -2):
            dp[i] += dp[j] * 2
        dp[i] %= mod

    return dp[n]
