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






n = int(input())
l = [0]*1000001
val = 1
cal = 1
count = 0

while True:
  if n==1 or l[n]:
    # print('111111111111')
    print(l[n])
    break
  cal = val
  while cal < 1000000:
    # print('222222222222')
    l[cal] = count
    cal *= 2
    count += 1
  count = 0
  cal = val
  while cal < 1000000:
    # print('3333333333333')
    l[cal] = count
    l[cal_plus_1] = count_cal_plus_1
    cal *= 3
    count += 1
    cal_plus_1 = cal + 1
    count_cal_plus_1 = count + 1
  count = 0
  while l[val] != 0:
    # print('4444444444444')
    val += 1
  cal = val


  # if cal % 2 == 0:
  #   # print('5555555555')
  #   cal = cal // 2
  #   count += 1

  # if cal % 3 == 0:
  #   # print('666666666666')
  #   cal = cal // 2
  #   count += 1



