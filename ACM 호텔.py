import sys

T = int(sys.stdin.readline())
for _ in range(T):
  H,W,N = map(int,sys.stdin.readline().split()) 
  a = (N//H)+1
  b = N%H
  if b == 0 :
    a = N//H
    b = H
  print(f'{b}{a:02d}')
