
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


# from collections import deque
# def solution(priorities, location):
#     answer = [0] * len(priorities)
#     # breakpoint()
#     q = deque([(priorities[i],i) for i,v in enumerate(priorities)])
#     sort_q = deque(sorted(priorities,reverse=True))
#     count = 1
#     while True:
#       if not q:
#         break

#       temp, index = q.popleft()
#       if temp == sort_q[0]:
#           if index == location:
#              return count
#           answer[index] = count
#           count += 1
#           sort_q.popleft()
#       else:
#           q.append([temp,index])

        

# priorities = [2, 1, 3, 2]
# location = 2
# print(solution(priorities, location)) #0
# priorities = [1, 1, 9, 1, 1, 1]
# location = 0
# print(solution(priorities, location)) #5
# priorities = [1, 2, 3, 4, 5, 6]
# location = 0
# print(solution(priorities, location)) #6




#- <다리를 지나는 트럭>
# 문제 설명
# 트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

# 예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

# 경과 시간	다리를 지난 트럭	다리를 건너는 트럭	대기 트럭
# 0	[]	[]	[7,4,5,6]
# 1~2	[]	[7]	[4,5,6]
# 3	[7]	[4]	[5,6]
# 4	[7]	[4,5]	[6]
# 5	[7,4]	[5]	[6]
# 6~7	[7,4,5]	[6]	[]
# 8	[7,4,5,6]	[]	[]
# 따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

# solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

# 제한 조건
# bridge_length는 1 이상 10,000 이하입니다.
# weight는 1 이상 10,000 이하입니다.
# truck_weights의 길이는 1 이상 10,000 이하입니다.
# 모든 트럭의 무게는 1 이상 weight 이하입니다.
# 입출력 예
# bridge_length	weight	truck_weights	return
# 2	10	[7,4,5,6]	8
# 100	100	[10]	101
# 100	100	[10,10,10,10,10,10,10,10,10,10]	110

# from collections import deque
# def solution(bridge_length, weight, truck_weights):
#     truck_q = deque(truck_weights)
#     bridge = deque([0] * bridge_length)
#     time = 0
#     bridge_weight = 0
#     # breakpoint()
#     while truck_q or bridge_weight:
#         bridge_weight -= bridge.popleft()
#         if truck_q and (bridge_weight + truck_q[0] <= weight):
#             current_truck = truck_q.popleft()
#             bridge.append(current_truck)
#             bridge_weight += current_truck
#         else:
#             bridge.append(0)
#         time += 1
#     return time

# bridge_length	 = 2
# weight = 10
# truck_weights = [7,4,5,6]
# print(solution(bridge_length, weight, truck_weights)) #8
# bridge_length	 = 100
# weight = 100
# truck_weights = [10]
# print(solution(bridge_length, weight, truck_weights)) #101  
# bridge_length	 = 100
# weight = 100  
# truck_weights = [10,10,10,10,10,10,10,10,10,10]
# print(solution(bridge_length, weight, truck_weights)) #110



#- <Stock Price>
# 문제 설명
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

# 제한사항
# prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
# prices의 길이는 2 이상 100,000 이하입니다.
# 입출력 예
# prices	return
# [1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
# 입출력 예 설명
# 1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
# 2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
# 3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
# 4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
# 5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.

from collections import deque
def solution(prices):
    q = deque([prices[0]])
    answer = [0] * len(prices)
    time = 1
    for i in range(1,len(prices)):
        index = 1
        if q[-index] <= prices[i]:
            q.append(prices[i])
            
        else:
            answer[i-1] = time
            q.popleft()
            q.append(prices[i])


    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices)) #[4, 3, 1, 1, 0]