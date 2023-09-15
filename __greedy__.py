
#* Greedy: When part of the answer is THE answer!

#- <Coin 0>
# import sys

# N, K = map(int, sys.stdin.readline().split())
# L = [int(sys.stdin.readline()) for _ in range(N)]
# L.reverse()
# result = 0

# for v in L:
#   if v > K:
#     continue
#   result += K // v
#   K = K % v
#   if K == 0:
#     break

# print(result)


#- <meeting room assignment>
# import sys
# n = int(sys.stdin.readline())
# l = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# l.sort(key=lambda x:(x[1],x[0]))

# result = 1
# temp = l[0][1] 
# for i in range(1,len(l)):
#   if temp <= l[i][0]:
#     temp = l[i][1] 
#     result += 1
  
# print(result)



#- <ATM>
# import sys
# n = int(sys.stdin.readline())
# l = list(map(int,sys.stdin.readline().split()))
# l.sort()

# for i in range(1,len(l)):
#   l[i] += l[i-1]

# print(sum(l))


#- <Missing Parenthesis>
# import sys
# e = list(sys.stdin.readline().strip().split('-'))

# for i in range(len(e)):
#   e[i] = sum(map(int,e[i].split('+')))

# for i in range(1,len(e)):
#   e[i] = int(e[i-1]) - int(e[i])

# print(e[-1])
  


#- <Gas Station>
# import sys
# n = int(sys.stdin.readline())
# distances = list(map(int,sys.stdin.readline().split()))
# costs = list(map(int,sys.stdin.readline().split()))

# value = costs[0]
# result = 0
# for i in range(n-1):
#   if costs[i] < value:
#     value = costs[i]
#   result += value * distances[i]

# print(result)



#- <Gym uniform>
#. We should pay attention to the exception conditions of the problem
# 문제 설명
# 점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 전체 학생의 수는 2명 이상 30명 이하입니다.
# 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
# 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
# 입출력 예
# n	lost	reserve	return
# 5	[2, 4]	[1, 3, 5]	5
# 5	[2, 4]	[3]	4
# 3	[3]	[1]	2
# 입출력 예 설명
# 예제 #1
# 1번 학생이 2번 학생에게 체육복을 빌려주고, 3번 학생이나 5번 학생이 4번 학생에게 체육복을 빌려주면 학생 5명이 체육수업을 들을 수 있습니다.

# 예제 #2
# 3번 학생이 2번 학생이나 4번 학생에게 체육복을 빌려주면 학생 4명이 체육수업을 들을 수 있습니다.


def solution(n, lost, reserve):
    d_l = {l:1 for l in lost}
    d_r = {r:1 for r in reserve}
    lost.sort()
    for l in lost: # Who lost but reserve
        if l in d_r:
            del d_l[l]
            del d_r[l]

    for l in lost:
        if l in d_l:
            if l-1 in d_r:
                del d_l[l]
                del d_r[l-1]
                continue
            if l+1 in d_r:
                del d_l[l]
                del d_r[l+1]
            
    return n-len(d_l)

n = 5	
lost = [2, 4]	
reserve = [1, 3, 5]	
print(solution(n, lost, reserve)) # 5
n = 5	
lost = [2, 4]	
reserve = [3]	
print(solution(n, lost, reserve)) # 4
n = 3	
lost = [3]	
reserve = [1]	
print(solution(n, lost, reserve)) # 2
n = 10
lost = [2, 4, 5, 6, 7, 9, 10]
reserve = [1, 3, 4, 8]
print(solution(n, lost, reserve)) # 6
