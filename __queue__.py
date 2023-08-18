
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




# #- <Integer Lists>
# import sys
# from collections import deque
# T = int(sys.stdin.readline())

# for _ in range(T):
#   p = sys.stdin.readline().strip()
#   n = int(sys.stdin.readline())
#   q = deque(sys.stdin.readline().strip('[]\n ').split(','))
#   flag = True
#   reverse = False

#   for i in p:
#     if i == 'R':
#       reverse = not reverse
#     if i == 'D':
#       if not q or q[0] == '':
#         flag = False
#         break
#       else:
#         if reverse:
#           q.pop()
#         else:
#           q.popleft()
  
#   if flag:
#     if reverse:
#       q.reverse()
#     print('['+','.join(q)+']')
#   else:
#     print('error')





#- <프로세스>
# 프로세스문제 설명
# 운영체제의 역할 중 하나는 컴퓨터 시스템의 자원을 효율적으로 관리하는 것입니다. 이 문제에서는 운영체제가 다음 규칙에 따라 프로세스를 관리할 경우 특정 프로세스가 몇 번째로 실행되는지 알아내면 됩니다.

# 1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
# 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
# 3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
#   3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.
# 예를 들어 프로세스 4개 [A, B, C, D]가 순서대로 실행 대기 큐에 들어있고, 우선순위가 [2, 1, 3, 2]라면 [C, D, A, B] 순으로 실행하게 됩니다.

# 현재 실행 대기 큐(Queue)에 있는 프로세스의 중요도가 순서대로 담긴 배열 priorities와, 몇 번째로 실행되는지 알고싶은 프로세스의 위치를 알려주는 location이 매개변수로 주어질 때, 해당 프로세스가 몇 번째로 실행되는지 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# priorities의 길이는 1 이상 100 이하입니다.
# priorities의 원소는 1 이상 9 이하의 정수입니다.
# priorities의 원소는 우선순위를 나타내며 숫자가 클 수록 우선순위가 높습니다.
# location은 0 이상 (대기 큐에 있는 프로세스 수 - 1) 이하의 값을 가집니다.
# priorities의 가장 앞에 있으면 0, 두 번째에 있으면 1 … 과 같이 표현합니다.
# 입출력 예
# priorities	location	return
# [2, 1, 3, 2]	2	1
# [1, 1, 9, 1, 1, 1]	0	5
# 입출력 예 설명
# 예제 #1

# 문제에 나온 예와 같습니다.

# 예제 #2

# 6개의 프로세스 [A, B, C, D, E, F]가 대기 큐에 있고 중요도가 [1, 1, 9, 1, 1, 1] 이므로 [C, D, E, F, A, B] 순으로 실행됩니다. 따라서 A는 5번째로 실행됩니다.


from collections import deque
def solution(priorities, location):
    answer = [0] * len(priorities)
    # breakpoint()
    q = deque([(priorities[i],i) for i,v in enumerate(priorities)])
    sort_q = deque(sorted(priorities,reverse=True))
    count = 1
    while True:
      if not q:
        break

      temp, index = q.popleft()
      if temp == sort_q[0]:
          if index == location:
             return count
          answer[index] = count
          count += 1
          sort_q.popleft()
      else:
          q.append([temp,index])

        

priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location)) #0
priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location)) #5
priorities = [1, 2, 3, 4, 5, 6]
location = 0
print(solution(priorities, location)) #6
