# import sys

# x,y,w,h = map(int,sys.stdin.readline().split())

# print(min(w-x,h-y,x,y))




# import sys
# cnt_x = dict()
# cnt_y = dict()

# for _ in range(3):
#   x,y = map(int,sys.stdin.readline().split())
#   if x in cnt_x:
#     cnt_x[x] += 1
#   else:
#     cnt_x[x] = 1

#   if y in cnt_y:
#     cnt_y[y] += 1
#   else:
#     cnt_y[y] = 1
  
# print(min(cnt_x,key=cnt_x.get),min(cnt_y,key=cnt_y.get))



# import sys

# while True:
#   [x,y,z] = sorted(list(map(int,sys.stdin.readline().split())))
#   if x == 0 and y == 0 and z == 0:
#     break

#   if x**2 + y**2 == z**2:
#     print('right')
#   else:
    # print('wrong') 




# 가로, 세로를 따로 저장하고 -> 가장 큰 가로 x 가장 큰 세로 - 가장 큰 가로와 바로 이어져있지않은 세로 x 가장 큰 세로와 바로 이어져있지 않은 가로

# import sys
# K = int(sys.stdin.readline())
# W = []
# H = []

# for _ in range(6):
#   a,b = map(int,sys.stdin.readline().split())
#   if a == 1 or a == 2:
#     W.append(b)
#     H.append(0)
#   if a == 3 or a == 4:
#     W.append(0)
#     H.append(b)

# result = max(W)*max(H) - (W[H.index(max(H))-3]*H[W.index(max(W))-3])
# print(result*K)




# import sys
# import math

# R = int(sys.stdin.readline())

# print(format(round(R*R*math.pi,6),'.6f'))
# print(format(round(2*R*R,6),'.6f'))



# # * 수학적 지식이 부족해서 어려웠다.
# import sys
# T = int(sys.stdin.readline())

# for _ in range(T):
#   xo,yo,ro,xt,yt,rt = map(int,sys.stdin.readline().split())
#   # 두 원 중심 사이의 거리
#   distance = (abs(xo-xt)**2 + abs(yo-yt)**2) ** 0.5
#   # 두 원이 완전히 포개어 지는 경우. (교점이 무한대)
#   if xo == xt and yo == yt and ro == rt:
#     print(-1)
#   # 두 원이 두 점에서 만나는 경우.
#   elif abs(ro - rt) < distance < ro + rt :
#     print(2)
#   # 두 원이 내접하거나 외접하는 경우. (교점이 하나)
#   elif abs(ro - rt) == distance or ro + rt == distance:
#     print(1)
#   # 두 원의 교점이 없는 경우. 
#   elif distance < abs(ro - rt) or ro + rt < distance :
#     print(0)




# 출발점 도착점을 포함하고 있는 원의 개수를 구하면 됨.
# * 원의 방정식 -> (x-a)**2 + (y-b)**2 = r**2 
# * 따라서 (X'-a)**2 + (Y'-b)**2 <= r**2 를 만족시키는 (X',Y')는 원의 경계 또는 원 안에 포함된다!. 
# import sys 
# T = int(sys.stdin.readline())
# L = []

# for _ in range(T):
#   c = 0
#   x1, y1, x2, y2 = map(int,sys.stdin.readline().split())
#   n = int(sys.stdin.readline())
#   for _ in range(n):
#     cx, cy, r = map(int,sys.stdin.readline().split()) 
#     start = (x1-cx)**2 + (y1-cy)**2
#     end = (x2-cx)**2 + (y2-cy)**2
#     if(start <= r**2 and end > r**2) or (start > r**2 and end <= r**2): 
#       c += 1
#   L.append(c)

# print(*L,sep='\n')





# 세 구역으로 나눠서 생각해보자 
# 직사각형 구역. (X <= x and Y <= y) and (X+W >= x and Y+H >= y) 이면 링크 안 또는 경계에 있다.
# 왼쪽 반원 구역.  R = H/2 , (X-x)**2 + ((Y+R)-y)**2  <= R**2  
# 오른쪽 반원 구역.  R = H/2 , ((X+W)-x)**2 + ((Y+R)-y)**2  <= R**2  
import sys
W,H,X,Y,P = map(int,sys.stdin.readline().split())
R = H/2
count = 0

for _ in range(P):
  x,y = map(int,sys.stdin.readline().split())
  if (X <= x and Y <= y) and (X+W >= x and Y+H >= y):
    count += 1
    continue
  if ((X-x)**2 + ((Y+R)-y)**2  <= R**2):
    count += 1
    continue
  if (((X+W)-x)**2 + ((Y+R)-y)**2  <= R**2):
    count += 1
    continue

print(count)