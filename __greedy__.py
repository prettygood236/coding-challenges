
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


# def solution(n, lost, reserve):
#     d_l = {l:1 for l in lost}
#     d_r = {r:1 for r in reserve}
#     lost.sort()
#     for l in lost: # Who lost but reserve
#         if l in d_r:
#             del d_l[l]
#             del d_r[l]

#     for l in lost:
#         if l in d_l:
#             if l-1 in d_r:
#                 del d_l[l]
#                 del d_r[l-1]
#                 continue
#             if l+1 in d_r:
#                 del d_l[l]
#                 del d_r[l+1]
            
#     return n-len(d_l)

# n = 5	
# lost = [2, 4]	
# reserve = [1, 3, 5]	
# print(solution(n, lost, reserve)) # 5
# n = 5	
# lost = [2, 4]	
# reserve = [3]	
# print(solution(n, lost, reserve)) # 4
# n = 3	
# lost = [3]	
# reserve = [1]	
# print(solution(n, lost, reserve)) # 2
# n = 10
# lost = [2, 4, 5, 6, 7, 9, 10]
# reserve = [1, 3, 4, 8]
# print(solution(n, lost, reserve)) # 6




#- <Joystick> 
#. To generalize, you need to create a wide variety of test cases.
#. Generalization must be broad enough to cover all cases! 
# 조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
# ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

# 조이스틱을 각 방향으로 움직이면 아래와 같습니다.

# ▲ - 다음 알파벳
# ▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
# ◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
# ▶ - 커서를 오른쪽으로 이동 (마지막 위치에서 오른쪽으로 이동하면 첫 번째 문자에 커서)
# 예를 들어 아래의 방법으로 "JAZ"를 만들 수 있습니다.

# - 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
# - 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
# - 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
# 따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
# 만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

# 제한 사항
# name은 알파벳 대문자로만 이루어져 있습니다.
# name의 길이는 1 이상 20 이하입니다.
# 입출력 예
# name	return
# "JEROEN"	56
# "JAN"	23

def solution(name):
    l = [min(ord(x)-ord('A'),ord('Z')-ord(x)+1) for x in name]
    s = sum(l)
    if s == 0:
        return 0

    # When the name is lined up like a circle, you can use the longest continuous A's as a reference point. 
    # You need to find the start and end indices of the longest continuous A's. 
    dp = [0] * len(name)
    dp[0] = 0 if name[0] != 'A' else 1
    for i in range(1,len(name)):
        if name[i] == 'A':
            dp[i] = 1
            dp[i] += dp[i-1]
    end = dp.index(max(dp))
    start = end - max(dp) + 1


    # You just need to reach from start to end. 
    # There are two methods: min(going straight (passing through A), even if you turn around, avoiding A).

    # Case 1: Going straight (passing through A).
    # However, even if you go straight, if there are A's at the end, you can stop in front of them.
    case_1 = 0
    last = 0
    i = -1
    while True:
        if name[i] == 'A':
            last += 1
            i -= 1
        else:
            break
    case_1 = len(name)-1 - last

    # Case 2: Even if you turn around, avoid A."
    left = (len(dp)-1) - end
    right = start - 1 if start != 0 else 0
    case_2 = min(left,right)*2 + max(left,right)

    return s + min(case_1,case_2)


def solution(name):
    # Number of up and down operations
    answer = sum([min(ord(x)-ord('A'),ord('Z')-ord(x)+1) for x in name])

    n = len(name)
    # Number of left and right operations
    breakpoint()
    move = n - 1 # 끝까지 쭉 갈때 조작 횟수
    for idx in range(n):
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, n - next_idx)
        move = min(move, idx + n - next_idx + distance)

    answer += move
    return answer



name = 'ABA'
print(solution(name)) #2
name = 'AABA'
print(solution(name)) #3
name = 'BBBAAABBB'
print(solution(name)) #13
name = 'AAAAA'
print(solution(name)) #0
name = 'BBBBBBB'
print(solution(name)) #13
name = "JEROEN"	
print(solution(name)) #56
name = "JAN"	
print(solution(name)) #23
name = "JAAN"	
print(solution(name)) #23
 
