import sys

N,M = map(int,sys.stdin.readline().split())
L = []

for i in range(1,N+1):
  for j in range(1,N+1):
    if i != j:
      L.append([i,j])

print(L)