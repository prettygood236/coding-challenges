
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
# import sys
# from collections import deque 

# n = int(sys.stdin.readline())
# queue = deque([i+1 for i in range(n)])

# while len(queue) > 1:
#   queue.popleft()
#   queue.append(queue.popleft())

# print(queue[0])
  
  


#- <The Josephus Problem 0>
# import sys
# from collections import deque

# N,K = map(int,sys.stdin.readline().split())
# queue = deque([i+1 for i in range(N)])
# result = []
# t = -(K-1)

# for i in range(N):
#   queue.rotate(t)
#   result.append(queue.popleft())


# print('<',end='')
# for i in range(N):
#   if i == N-1:
#     print(result[i],end='')
#   else:
#     print(result[i],',',sep='',end=' ')
# print('>')




#- <Printer Queue>
# import sys
# from collections import deque 

# for _ in range(int(sys.stdin.readline())):
#   n,m = map(int,sys.stdin.readline().split())
#   l = list(map(int,sys.stdin.readline().split()))
#   for i in range(len(l)):
#     l[i] = [l[i],False]
#   l[m][1] = True
#   queue = deque(l)
#   count = 1
#   while True:
#     max_v = max(queue)[0]
#     if queue[0][1] and queue[0][0] == max_v:
#       break
#     elif queue[0][0] == max_v:
#       queue.popleft()
#       count += 1
#     else :
#       queue.rotate(-1)

#   print(count)



#- <Deque>
# import sys
# from collections import deque 
# dq = deque([])

# n = int(sys.stdin.readline())
# for _ in range(n):
#   t = sys.stdin.readline().rstrip()
#   if t[:4] == 'push':
#     f,b = t.split()
#     if f == 'push_back':
#       dq.append(int(b))
#     if f == 'push_front':
#       dq.appendleft(int(b))
#   if t == 'pop_front':
#     if dq:
#       print(dq.popleft())
#     else:
#       print(-1)
#   if t == 'pop_back':
#     if dq:
#       print(dq.pop())
#     else:
#       print(-1)
#   if t == 'size':
#     print(len(dq))
#   if t == 'empty':
#     if dq:
#       print(0)
#     else:
#       print(1)
#   if t == 'front':
#     if dq:
#       print(dq[0])
#     else:
#       print(-1)
#   if t == 'back':
#     if dq:
#       print(dq[-1])
#     else:
#       print(-1)
    



#- <Spinning Queue>
# import sys
# from collections import deque
# N,M = map(int,sys.stdin.readline().split())
# l = list(map(int,sys.stdin.readline().split()))
# queue = deque([i+1 for i in range(N)])
# result = 0

# for i in l:
#   temp = 0
#   while True:
#     if i == queue[0]:
#       result += min(temp, len(queue)-temp)
#       queue.popleft()
#       break
#     else:
#       queue.rotate(-1)
#       temp += 1

# print(result)




#- <Integer Lists>
import sys
from collections import deque
T = int(sys.stdin.readline())

for _ in range(T):
  p = sys.stdin.readline().strip()
  n = int(sys.stdin.readline())
  q = deque(sys.stdin.readline().strip('[]\n ').split(','))
  flag = True
  reverse = False

  for i in p:
    if i == 'R':
      reverse = not reverse
    if i == 'D':
      if not q or q[0] == '':
        flag = False
        break
      else:
        if reverse:
          q.pop()
        else:
          q.popleft()
  
  if flag:
    if reverse:
      q.reverse()
    print('['+','.join(q)+']')
  else:
    print('error')


