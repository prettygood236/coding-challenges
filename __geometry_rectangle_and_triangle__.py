
#. <Rectangle>
# a = int(input())
# b = int(input())
# print(a*b)


#. <Escape from the rectangle>
# import sys

# x,y,w,h = map(int,sys.stdin.readline().split())

# print(min(w-x,h-y,x,y))


#. <CETVRTA>
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



#. <Math is a physical education subject>
# print(int(input())*4)


#. BAEKJOON 9063. <Ground>
# import sys
# n = int(sys.stdin.readline())
# min_x, min_y = 10000,10000
# max_x, max_y = -10000,-10000
# for _ in range(n):
#   x,y = map(int,sys.stdin.readline().split())
#   min_x = min(min_x,x)
#   min_y = min(min_y,y)
#   max_x = max(max_x,x)
#   max_y = max(max_y,y)

# w = abs(max_x - min_x)
# h = abs(max_y - min_y)
# result = w*h

# print(w*h)



#. BAEKJOON 9063. <Triangle Times>
# a = int(input())
# b = int(input())
# c = int(input())
# if a==60 and a==b and b==c:
#   print('Equilateral')
# elif a+b+c==180 and (a==b or b==c or a==c):
#   print('Isosceles')
# elif a+b+c==180 and (a!=b and b!=c and a!=c):
#   print('Scalene')
# elif a+b+c!=180:
#   print('Error')




#. BAEKJOON 5073. <Triangles>
# while True:
#   l = list(map(int,input().split()))
#   l.sort()
#   a = l[2]
#   b = l[1]
#   c = l[0]
#   if a==0 and b==0 and c==0:
#     break
#   if a==b and b==c:
#     print('Equilateral')
#     continue
#   if a >= b+c:
#     print('Invalid')
#     continue
#   if a==b or b==c or a==c:
#     print('Isosceles')
#     continue
#   if a!=b and b!=c and a!=c:
#     print('Scalene')  




#. BAEKJOON 14215. <Three bars>
l = list(map(int,input().split()))
l.sort()
a = l[2]
b = l[1]
c = l[0]
if a >= b+c:
  a = b+c -1

print(a+b+c)