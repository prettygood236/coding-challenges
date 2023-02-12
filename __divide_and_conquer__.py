
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