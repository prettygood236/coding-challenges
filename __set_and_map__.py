import sys

N = int(sys.stdin.readline())
Set_a = set(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
L = list(map(int,sys.stdin.readline().split()))
Set_b = set(L)

intersection = Set_a & Set_b

for i in range(M):
  if L[i] in intersection:
    print(1)
  else:
    print(0)