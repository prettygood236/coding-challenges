# 가장 개수가 적어야 한다 -> 5로 다 나누고 3을 끼워넣어본다. 딱 떨어질떄 까지 5를 빼간다. 

import sys

n = int(sys.stdin.readline()) # 18 4 6 9 11 

a = n//5 # 3 0 1 1 2 
b = n%5 # 3 4 1 4 1 

while True:
  c = b//3 # 1 1 0 1 0
  d = b%3 # 0 1 1 1 1  -> d가 0이 아니라면 5몫 하나 빼서 다시. d가 0이라면 print(a+c) 

  if d == 0:
    print(a+c)
    break
  if d != 0 and a == 0:
    print(-1)
    break

  a = a-1
  b = b+5
