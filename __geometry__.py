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



import sys

while True:
  [x,y,z] = sorted(list(map(int,sys.stdin.readline().split())))
  if x == 0 and y == 0 and z == 0:
    break

  if x**2 + y**2 == z**2:
    print('right')
  else:
    print('wrong') 
