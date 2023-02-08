def solution(a):
  dp = [[0] * 500000 for _ in range(500000)]
  answer = -1
  for i in range(len(a)):
    if a[i] 
  print(dp)
  return answer

a = [0] # 0
a = [5,2,3,3,5,3]	# 4
a = [0,3,3,0,7,2,0,2,2,0]	# 8

print(solution(a))





#* LCS (Longest Common Subsequence) 가장 긴 공통 부분 수열
# x = input()
# y = input()
# dp = [[0] * (len(y)+1) for _ in range(len(x)+1)]

# for i in range(1,len(x)+1):
#   for j in range(1,len(y)+1):
#     if x[i-1] == y[j-1]:
#       dp[i][j] = dp[i-1][j-1] + 1
#     else :
#       dp[i][j] = max(dp[i-1][j],dp[i][j-1])

# print(dp[-1][-1])