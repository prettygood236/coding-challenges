# n = int(input())
# recur_count = 0
# dp_count = 0

# def recur_fib(n):
#   global recur_count
#   if n == 1 or n == 2 :
#     recur_count += 1
#     return 1
#   else :
#     return recur_fib(n-1) + recur_fib(n-2)

# dp = [0] * 41
# def dp_fib(n):
#   global dp_count
#   dp[1] = 1
#   dp[2] = 1
#   k = 3
#   while k <= n:
#     dp[k] = dp[k-1] + dp[k-2]
#     k += 1
#     dp_count += 1

# recur_fib(n)
# dp_fib(n)

# print(recur_count, dp_count)






# #! DP - Memoization!

# dp = [[[0]*21 for _ in range(21)] for _ in range(21)]

# def w(a,b,c):
#   #. Exit condition 
#   if a<=0 or b<=0 or c<=0:
#     return 1
#   if a>20 or b>20 or c>20:
#     return w(20,20,20)

#   #. If the problem has already been calculated, return it as is.
#   if dp[a][b][c]:
#     return dp[a][b][c]

#   if a<b<c :
#     dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
#     return dp[a][b][c]
#   dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
#   return dp[a][b][c]
  

# while True:
#   a,b,c = map(int,input().split())
#   if a==-1 and b==-1 and c==-1:
#     exit()
#   w(a,b,c)
#   print(f'w({a}, {b}, {c}) = {w(a,b,c)}')





# N = int(input())
# dp = [0] * 1000001
# dp[1] = 1
# dp[2] = 2
# k = 3

# while k <= N:
#   #. 메모리 최적화를 위해 나머지를 저장한다. (나머지 정리에 의해 합의 나머지는 나머지의 합과 같다)
#   dp[k] = (dp[k-1] + dp[k-2])%15746
#   k += 1

# print(dp[N])





# T = int(input())
# for _ in range(T):
#   N = int(input())
#   dp = [0] * 101
#   dp[1] = 1
#   dp[2] = 1
#   dp[3] = 1
#   dp[4] = 2
#   k = 5
#   while k <= N:
#     dp[k] = dp[k-2] + dp[k-3]
#     k += 1

#   print(dp[N])






# n = int(input())
# l = list(map(int,input().split()))

# for i in range(1,len(l)):
#   l[i] = max(l[i],l[i-1]+l[i])

# print(max(l))






#. 일반항을 구해내라!.

# N = int(input())
# L = [list(map(int,input().split())) for _ in range(N)]

# for i in range(1,len(L)):
#   for j in range(3):
#     L[i][j] += min(L[i-1][j-1],L[i-1][j-2])

# print(min(L[-1]))






# n = int(input())
# l = [list(map(int,input().split())) for _ in range(n)]

# for i in range(1,len(l)):
#   for j in range(len(l[i])):
#     if j == 0:
#       l[i][j] += l[i-1][j]
#     elif j == len(l[i])-1:
#       l[i][j] += l[i-1][len(l[i-1])-1]
#     else:
#       l[i][j] += max(l[i-1][j-1],l[i-1][j])

# print(max(l[-1]))







# n = int(input())
# l = []

# for i in range(n):
#   num = int(input())
#   if i == 0:
#     l.append([num])
#   if i == 1:
#     l.append([l[0][0]+num])
#     l[i].append(num)
#   if i >= 2:
#     l.append([num+l[i-1][1]])
#     l[i].append(num+max(l[i-2]))
    
# print(max(l[-1]))






# n = int(input())
# l = [0] * (n+1)

# for i in range(2,n+1):
#   l[i] = l[i-1]+1

#   if i % 2 == 0:
#     l[i] = min(l[i//2]+1,l[i])

#   if i % 3 == 0:
#     l[i] = min(l[i//3]+1,l[i])

# print(l[n])







# n = int(input())

# dp = [[0]*10 for _ in range(n+1)]
# dp[0] = []
# for i in range(1,10):
#   dp[1][i] = 1

# mod = 1000000000

# for i in range(2,n+1):
#   for j in range(10):
#     if j == 0:
#       dp[i][j] = dp[i-1][1]
#     elif j == 9:
#       dp[i][j] = dp[i-1][8]
#     else:
#       dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

# print(sum(dp[n])%mod)






# n = int(input())
# l = [[] for _ in range(n)] 

# for i in range(n):
#   t = int(input())
#   if i == 0 :
#     l[0].append(t)
#   if i == 1:
#     l[1].append(l[0][0])
#     l[1].append(t)
#     l[1].append(l[0][0]+t)
#   if i >= 2:
#     l[i].append(max(l[i-1]))
#     l[i].append(max(l[i-2])+t)
#     l[i].append(l[i-1][1]+t)

# print(max(l[-1]))






#* LIS (Longest Increasing Subsequence) 가장 긴 증가하는 부분수열


#. 시간복잡도 O(N^2)의 해결법
# N = int(input())
# A = list(map(int,input().split()))
# D = [0] * N

# for i in range(N):
#   D[i] = 1
#   for j in range(i):
#     if A[i] > A[j]:
#       D[i] = max(D[i],D[j]+1)
    
# print(max(D))


#. 시간복잡도 O(NlogN)의 해결법

# 세그먼트 트리 배우고 다시 해보도록 하겠다.





# from itertools import chain
# n = int(input())
# a = list(map(int,input().split()))
# dp = [[0,0] for _ in range(n)]

# for i in range(n):
#   dp[i][0] = 1
#   dp[i][1] = 1
#   for j in range(i):
#     if a[i] > a[j]:
#       dp[i][0] = max(dp[i][0],dp[j][0]+1)
#     if a[j] > a[i]:
#       dp[i][1] = max(dp[i][1],dp[j][0]+1,dp[j][1]+1)

# print(max(list(chain(*dp)))) 





# n = int(input())
# a = [list(map(int,input().split())) for _ in range(n)]
# a.sort()
# dp = [0] * n

# for i in range(n):
#   dp[i] = 1
#   for j in range(i):
#     if a[i][1] > a[j][1]:
#       dp[i] = max(dp[i],dp[j]+1)

# print(n-max(dp))





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





#* Napsack Problem

n, k = map(int,input().split())
wt = []
v = []
for _ in range(n):
  a,b = map(int,input().split())
  wt.append(a)
  v.append(b)

def knapSack(W, wt, v, n):
    dp = [0 for _ in range(W+1)] 
    for i in range(1, n+1): 
      for w in range(W, 0, -1): 
        if wt[i-1] <= w:
          dp[w] = max(dp[w], dp[w-wt[i-1]]+v[i-1])
 
    return dp[W]  


print(knapSack(k, wt, v, n))