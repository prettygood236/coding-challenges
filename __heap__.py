
#- BAEKJOON 11279. <Max Heap>
# import sys

# def push_heap(heap, value):
#   heap.append(value)
#   i = len(heap) - 1
#   while i > 0:
#     parent = (i - 1) // 2
#     if heap[parent] >= heap[i]:
#       break
#     heap[parent], heap[i] = heap[i], heap[parent]
#     i = parent

# def pop_heap(heap):
#   if not heap:
#     return 0

#   max_value = heap[0]
#   heap[0] = heap[-1]
#   heap.pop()

#   i = 0
#   while True:
#     left_child = 2 * i + 1
#     right_child = 2 * i + 2
#     max_child = left_child

#     if right_child < len(heap) and heap[right_child] > heap[left_child]:
#       max_child = right_child

#     if max_child >= len(heap) or heap[i] >= heap[max_child]:
#       break

#     heap[i], heap[max_child] = heap[max_child], heap[i]
#     i = max_child

#   return max_value

# N = int(sys.stdin.readline())
# heap = []

# for _ in range(N):
#   x = int(sys.stdin.readline())
#   if x == 0:
#     print(pop_heap(heap))
#   else:
#     push_heap(heap, x)



#- <Spicier>
# 문제 설명
# 매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
# Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# scoville의 길이는 2 이상 1,000,000 이하입니다.
# K는 0 이상 1,000,000,000 이하입니다.
# scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
# 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.
# 입출력 예
# scoville	K	return
# [1, 2, 3, 9, 10, 12]	7	2
# 입출력 예 설명
# 스코빌 지수가 1인 음식과 2인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
# 새로운 음식의 스코빌 지수 = 1 + (2 * 2) = 5
# 가진 음식의 스코빌 지수 = [5, 3, 9, 10, 12]

# 스코빌 지수가 3인 음식과 5인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
# 새로운 음식의 스코빌 지수 = 3 + (5 * 2) = 13
# 가진 음식의 스코빌 지수 = [13, 9, 10, 12]

# 모든 음식의 스코빌 지수가 7 이상이 되었고 이때 섞은 횟수는 2회입니다.


#* When should we use a heap?
#* When we need to frequently access the maximum or minimum element of a collection, but still want to insert and delete elements efficiently. 

# import heapq

# def solution(scoville, K):
#     answer = 0
#     heap_scoville = []
#     heapq.heapify(scoville)
#     while True:
#         if len(heap_scoville) == 1 and heap_scoville[0] < K:
#             return -1
#         if heap_scoville[0] < K:
#             first = heapq.heappop(heap_scoville)
#             second = heapq.heappop(heap_scoville)
#             new = first + (second*2)        
#             heapq.heappush(heap_scoville,new)
#             answer += 1
#         else:
#             return answer

# scoville = [1, 2, 3, 9, 10, 12]	
# K	= 7
# print(solution(scoville,K)) #2



#- <Disk Controller>
# 문제 설명
# 하드디스크는 한 번에 하나의 작업만 수행할 수 있습니다. 디스크 컨트롤러를 구현하는 방법은 여러 가지가 있습니다. 가장 일반적인 방법은 요청이 들어온 순서대로 처리하는 것입니다.

# 예를들어

# - 0ms 시점에 3ms가 소요되는 A작업 요청
# - 1ms 시점에 9ms가 소요되는 B작업 요청
# - 2ms 시점에 6ms가 소요되는 C작업 요청
# 와 같은 요청이 들어왔습니다. 이를 그림으로 표현하면 아래와 같습니다.
# Screen Shot 2018-09-13 at 6.34.58 PM.png

# 한 번에 하나의 요청만을 수행할 수 있기 때문에 각각의 작업을 요청받은 순서대로 처리하면 다음과 같이 처리 됩니다.
# Screen Shot 2018-09-13 at 6.38.52 PM.png

# - A: 3ms 시점에 작업 완료 (요청에서 종료까지 : 3ms)
# - B: 1ms부터 대기하다가, 3ms 시점에 작업을 시작해서 12ms 시점에 작업 완료(요청에서 종료까지 : 11ms)
# - C: 2ms부터 대기하다가, 12ms 시점에 작업을 시작해서 18ms 시점에 작업 완료(요청에서 종료까지 : 16ms)
# 이 때 각 작업의 요청부터 종료까지 걸린 시간의 평균은 10ms(= (3 + 11 + 16) / 3)가 됩니다.

# 하지만 A → C → B 순서대로 처리하면
# Screen Shot 2018-09-13 at 6.41.42 PM.png

# - A: 3ms 시점에 작업 완료(요청에서 종료까지 : 3ms)
# - C: 2ms부터 대기하다가, 3ms 시점에 작업을 시작해서 9ms 시점에 작업 완료(요청에서 종료까지 : 7ms)
# - B: 1ms부터 대기하다가, 9ms 시점에 작업을 시작해서 18ms 시점에 작업 완료(요청에서 종료까지 : 17ms)
# 이렇게 A → C → B의 순서로 처리하면 각 작업의 요청부터 종료까지 걸린 시간의 평균은 9ms(= (3 + 7 + 17) / 3)가 됩니다.

# 각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 배열 jobs가 매개변수로 주어질 때, 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가 되는지 return 하도록 solution 함수를 작성해주세요. (단, 소수점 이하의 수는 버립니다)

# 제한 사항
# jobs의 길이는 1 이상 500 이하입니다.
# jobs의 각 행은 하나의 작업에 대한 [작업이 요청되는 시점, 작업의 소요시간] 입니다.
# 각 작업에 대해 작업이 요청되는 시간은 0 이상 1,000 이하입니다.
# 각 작업에 대해 작업의 소요시간은 1 이상 1,000 이하입니다.
# 하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.
# 입출력 예
# jobs	return
# [[0, 3], [1, 9], [2, 6]]	9
# 입출력 예 설명
# 문제에 주어진 예와 같습니다.

# 0ms 시점에 3ms 걸리는 작업 요청이 들어옵니다.
# 1ms 시점에 9ms 걸리는 작업 요청이 들어옵니다.
# 2ms 시점에 6ms 걸리는 작업 요청이 들어옵니다.


def solution(jobs):
    answer = 0
    time = 0
    for x in jobs:
        time += x[1]
        if 
    # answer = //len


    return answer


jobs = [[0, 3], [1, 9], [2, 6]] 		
print(solution(jobs)) #9