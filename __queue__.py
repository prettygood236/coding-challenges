
#- <Queue 2>
# import sys
# from collections import deque
# n = int(sys.stdin.readline())

# queue = deque([])
# for _ in range(n):
#   s = sys.stdin.readline().strip()
#   if s[:4] == 'push':
#     s,i = s.split()
#     queue.append(int(i))
#   if s == 'pop':
#     if queue:
#       print(queue.popleft())
#     else :
#       print(-1)
#   if s == 'size':
#     print(len(queue))
#   if s == 'empty':
#     if queue:
#       print(0)
#     else:
#       print(1)
#   if s == 'front':
#     if queue:
#       print(queue[0])
#     else :
#       print(-1)
#   if s == 'back':
#     if queue:
#       print(queue[-1])
#     else :
#       print(-1)



#- <Card 2>
import sys
from collections import deque 

n = int(sys.stdin.readline())
queue = deque([i+1 for i in range(n)])

while len(queue) > 1:
  queue.popleft()
  queue.append(queue.popleft())

print(queue[0])
  
  