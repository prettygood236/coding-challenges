
#. <Making Quad-Tree>
# import sys

# n = int(sys.stdin.readline())
# l = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
# w = 0
# b = 0

# def solve(x,y,n):
#   global w,b
#   t = l[y][x]
#   for i in range(y,y+n):
#     for j in range(x,x+n):
#       if l[i][j] != t:
#         solve(x,y,n//2)
#         solve(x,y+n//2,n//2)
#         solve(x+n//2,y,n//2)
#         solve(x+n//2,y+n//2,n//2)
#         return
#   if t == 0:
#     w += 1
#   else:
#     b += 1  

# solve(0,0,n)
# print(w,b,sep='\n')




#. <Quad-Tree> 
#. 시작, 끝을 n, x,y를 이용해 정하기! n은 계속 1/2n으로 변화

# import sys

# n = int(sys.stdin.readline())
# l = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]
# result = ''

# def solve(x,y,n):
#   global result
#   t = l[y][x]
#   for i in range(y,y+n):
#     for j in range(x,x+n):
#       if l[i][j] != t:
#         result += '('
#         solve(x,y,n//2)
#         solve(x+n//2,y,n//2)
#         solve(x,y+n//2,n//2)
#         solve(x+n//2,y+n//2,n//2)
#         result += ')'
#         return
#   result += str(t)

# solve(0,0,n)
# print(result)





#. <Spatial-Tree>

# import sys

# n = int(sys.stdin.readline())
# l = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
# result = [0]*3

# def solve(x,y,n):
#   t = l[y][x]
#   for i in range(y,y+n):
#     for j in range(x,x+n):
#       if l[i][j] != t:
#         n = n//3
#         for k in range(3):
#           solve(x,y,n)
#           solve(x+n,y,n)
#           solve(x+(2*n),y,n)
#           y += n
#         return
#   if t == -1:
#     result[0] += 1
#   if t == 0:
#     result[1] += 1
#   if t == 1:
#     result[2] += 1
#   return

# solve(0,0,n)
# print(*result, sep='\n')





#. <Modulo Powers>
#. 모듈로 거듭제곱
#! A^B mod C = ( (A mod C)^B ) mod C


import sys

a,b,c = map(int,sys.stdin.readline().split())
result = a
count = 1

while True:
  a = a*a
  count += 1
  if a > sys.maxsize:
    a %= c
    break

r = b % count
b = b // count




print(sys.maxsize)