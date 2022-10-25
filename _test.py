N = int(input())
R = [[0 for _ in range(101)] for _ in range(101)]
count = 0

for _ in range(N):
  a,b = map(int, input().split())

  for i in range(a,a+10):
    for j in range(b,b+10):
      if R[i][j] == 0:
        R[i][j] = 1
        count += 1

print(count)
    