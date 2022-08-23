import sys 

l = int(sys.stdin.readline())

for _ in range(l):
  k = int(sys.stdin.readline())
  n = int(sys.stdin.readline())
  f = list(range(1,15))
  for _ in range(k):
    s = 0
    for i in range(len(f)):
      s += f[i]
      f[i] = s
  print(f[n-1])