

n = int(input())
l = list(map(int,input().split()))

for i in range(1,len(l)):
  l[i] = max(l[i],l[i-1]+l[i])

print(max(l))






일반항을 구해내라!.

N = int(input())
L = [list(map(int,input().split())) for _ in range(N)]

for i in range(1,len(L)):
  for j in range(3):
    L[i][j] += min(L[i-1][j-1],L[i-1][j-2])

print(min(L[-1]))






n = int(input())
l = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,len(l)):
  for j in range(len(l[i])):
    if j == 0:
      l[i][j] += l[i-1][j]
    elif j == len(l[i])-1:
      l[i][j] += l[i-1][len(l[i-1])-1]
    else:
      l[i][j] += max(l[i-1][j-1],l[i-1][j])

print(max(l[-1]))







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






n = int(input())
l = [0] * (n+1)

for i in range(2,n+1):
  l[i] = l[i-1]+1

  if i % 2 == 0:
    l[i] = min(l[i//2]+1,l[i])

  if i % 3 == 0:
    l[i] = min(l[i//3]+1,l[i])

print(l[n])







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






