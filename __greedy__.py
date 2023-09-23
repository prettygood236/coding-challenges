
#* Greedy: When part of the answer is THE answer!

# def solution(s):
#     # breakpoint()
#     i = 0
#     new_s = ''
#     #. We just need to iterate over the index i according to the condition. So let's use a while loop!
#     while i < len(s): 
#         try:
#             if int(s[i]):
#                 new_s += s[i]
#                 i += 1
#                 continue
#         except:
#             if s[i:i+3] == 'one':
#                 new_s += '1'
#                 i += 3
#                 continue
#             elif s[i:i+3] == 'two':
#                 new_s += '2'
#                 i += 3
#                 continue
#             elif s[i:i+3] == 'six':
#                 new_s += '6'
#                 i += 3
#                 continue
#             elif s[i:i+4] == 'zero':
#                 new_s += '0'
#                 i += 4
#                 continue
#             elif s[i:i+4] == 'four':
#                 new_s += '4'
#                 i += 4
#                 continue
#             if s[i:i+4] == 'five':
#                 new_s += '5'
#                 i += 4
#                 continue
#             if s[i:i+4] == 'nine':
#                 new_s += '9'
#                 i += 4
#                 continue
#             if s[i:i+5] == 'three':
#                 new_s += '3'
#                 i += 5
#                 continue
#             if s[i:i+5] == 'seven':
#                 new_s += '7'
#                 i += 5
#                 continue
#             if s[i:i+5] == 'eight':
#                 new_s += '8'
#                 i += 5
#                 continue

#     return new_s

def solution(s):
    d = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    for x in d:
        s = s.replace(x,d[x])
    return s

# s = '8zerotwo8'
# print(solution(s))


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

# def solution(name):
#     l = [min(ord(x)-ord('A'),ord('Z')-ord(x)+1) for x in name]
#     s = sum(l)
#     if s == 0:
#         return 0

#     # When the name is lined up like a circle, you can use the longest continuous A's as a reference point. 
#     # You need to find the start and end indices of the longest continuous A's. 
#     dp = [0] * len(name)
#     dp[0] = 0 if name[0] != 'A' else 1
#     for i in range(1,len(name)):
#         if name[i] == 'A':
#             dp[i] = 1
#             dp[i] += dp[i-1]
#     end = dp.index(max(dp))
#     start = end - max(dp) + 1


#     # You just need to reach from start to end. 
#     # There are two methods: min(going straight (passing through A), even if you turn around, avoiding A).

#     # Case 1: Going straight (passing through A).
#     # However, even if you go straight, if there are A's at the end, you can stop in front of them.
#     case_1 = 0
#     last = 0
#     i = -1
#     while True:
#         if name[i] == 'A':
#             last += 1
#             i -= 1
#         else:
#             break
#     case_1 = len(name)-1 - last

#     # Case 2: Even if you turn around, avoid A."
#     left = (len(dp)-1) - end
#     right = start - 1 if start != 0 else 0
#     case_2 = min(left,right)*2 + max(left,right)

#     return s + min(case_1,case_2)


# def solution(name):
#     # Number of up and down operations
#     answer = sum([min(ord(x)-ord('A'),ord('Z')-ord(x)+1) for x in name])

#     n = len(name)
#     # Number of left and right operations
#     breakpoint()
#     move = n - 1 # 끝까지 쭉 갈때 조작 횟수
#     for idx in range(n):
#         next_idx = idx + 1
#         while (next_idx < n) and (name[next_idx] == 'A'):
#             next_idx += 1
#         distance = min(idx, n - next_idx)
#         move = min(move, idx + n - next_idx + distance)

#     answer += move
#     return answer



# name = 'ABA'
# print(solution(name)) #2
# name = 'AABA'
# print(solution(name)) #3
# name = 'BBBAAABBB'
# print(solution(name)) #13
# name = 'AAAAA'
# print(solution(name)) #0
# name = 'BBBBBBB'
# print(solution(name)) #13
# name = "JEROEN"	
# print(solution(name)) #56
# name = "JAN"	
# print(solution(name)) #23
# name = "JAAN"	
# print(solution(name)) #23
 


#- <Make a big number>
#. Strings are immutable. Therefore, you can't use 'sort', but you can use 'sorted'.
#. In Python, strings are indeed immutable. This means that once a string is created, it cannot be changed. However, you can reassign the variable to a new string. This doesn't change the original string but rather creates a new one. For example, if you have a string s = "Hello", and then do s = "World", you haven't changed "Hello" to "World". Instead, you've created a new string "World" and made s point to it.
#. Read the problem correctly.
# 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.
# 예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들수 있습니다. 이 중 가장 큰 숫자는 94 입니다.
# 문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

# 제한 조건
# number는 2자리 이상, 1,000,000자리 이하인 숫자입니다.
# k는 1 이상 number의 자릿수 미만인 자연수입니다.
# 입출력 예
# number	k	return
# "1924"	2	"94"
# "1231234"	3	"3234"
# "4177252841"	4	"775841"

# #. 앞에서부터 쭉 봐서 가장 작은 것들부터 k 개만큼 지우는 거 였다 젠장

# def solution(number, k):
#     breakpoint()
#     n = len(number)
#     #. In set, the time complexity of finding an element is also O(1) like a dictionary.
#     del_list = set()
#     temp = 0 
#     for i in range(1,n):
#         if not k:
#             break
#         # 제거할 수 있는 k만큼 뒤에 있는 숫자가 더 클때는 제거하는게 무조건 숫자가 커진다.
#         if k >= i-temp and number[i] > number[temp]:
#             for j in range(temp,i):
#                 del_list.add(j)
#                 k -= 1
#             temp += i-temp
#         # k만큼 지워도 뒤에 숫자가 더 작다면 그 앞 숫자들은 지우면 안된다!
#         elif i-temp >= k and number[i] <= number[temp]:
#             temp = i 
    
#     if k:
#         for i in range(k):
#             del_list.add(n-1-i)
            
#     return ''.join([v for i,v in enumerate(number) if i not in del_list])

# number = '98'
# k = 1
# print(solution(number, k)) #'9'
# number = '444456'
# k = 3
# print(solution(number, k)) #'454321'
# number = '1924'
# k = 2
# print(solution(number, k)) #'94'
# number = '1231234'
# k = 3
# print(solution(number, k)) #'3234'
# number = '4177252841'
# k = 4
# print(solution(number, k)) #'775841'
# number = '987654321'
# k = 4
# print(solution(number, k)) #'98765'


#- <Lifeboats>
#. The Two Pointers algorithm : A technique used in programming to solve problems by moving two pointers within a data structure. 
#. It's commonly used in linked lists and sorted arrays for tasks such as finding elements, detecting cycles, or locating subarrays with specific sums.
#. The two pointers move at different speeds, so a while loop is used to handle this.

# 무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.

# 예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.

# 구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.

# 사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
# 각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
# 구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
# 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.
# 입출력 예
# people	limit	return
# [70, 50, 80, 50]	100	3
# [70, 80, 50]	100	3
# ※ 2023년 07월 31일 테스트 케이스가 추가되었습니다. 기존에 제출한 코드가 통과하지 못할 수 있습니다.

def solution(people, limit):
    people.sort(reverse=True)
    answer = 0
    i = 0
    j = len(people) -1

    while i <= j:
        temp = limit
        temp -= people[i]
        i += 1
        # The condition i-1 != j is not necessary, but it can provide precision.
        if people[j] <= temp and i-1 != j :
            j -= 1
        answer += 1

    return answer

people = [70,60,50,30,27,3]
limit = 100
print(solution(people,limit)) #3
people = [70, 50, 80, 50]
limit = 100
print(solution(people,limit)) #3
people = [70, 80, 50]
limit = 100
print(solution(people,limit)) #3