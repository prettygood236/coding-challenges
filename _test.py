import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
s = 0

for _ in range(b):
  c,d = map(int,sys.stdin.readline().split())
  s+=c*d

if a == s:
  print('Yes')
else :
  print('No')
