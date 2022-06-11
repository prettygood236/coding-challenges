# baduk=[]
# for _ in range (19):
#   baduk.append(list(map(int,input().split())))
# n = int(input())

# for _ in range (n):
#   y,x = map(int,input().split())
  
#   for i in range (19):
#     baduk[y-1][i] = 1 if baduk[y-1][i]==0 else 0
#     for j in range (19):
#       baduk[i][x-1] = 1 if baduk[i][x-1]==0 else 0
  
# for i in range (19):
#   for j in range (19):
#     print(baduk[i][j],end=' ')
#   print()

# h, w = map(int, input().split())
# n = int(input())
# grid = [[0 for _ in range (w)] for _ in range (h)]

# for _ in range (n):
#   l,d,y,x = map(int,input().split())
#   if d == 0:
#     for i in range (l):
#       grid[y-1][x-1+i] = 1
#   else : 
#     for i in range (l):
#       grid[y-1+i][x-1] = 1
      
# for i in range (h):
#   for j in range (w):
#     print(grid[i][j], end=' ')
#   print()
  
maze=[]
for _ in range (10):
  maze.append(list(map(int,input().split())))

x = 1
y = 1

while True:
  if y>=9 or x>=9:
    break;
  
  if maze[y][x] == 2:
    maze[y][x] = 9
    break;
  
  if maze[y][x] == 0:
    maze[y][x] = 9
    x += 1
  
  if maze[y][x] == 1:
    x -= 1
    y += 1
    
  
for i in range (10):
  for j in range (10):
    print(maze[i][j], end=' ')
  print()