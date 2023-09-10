# # blackjack

# import sys

# N, M = map(int,sys.stdin.readline().strip().split())
# L = list(map(int, sys.stdin.readline().strip().split()))
# R = []
# result = 0

# for i in L[:-2]:
#   for j in L[L.index(i)+1:-1]:
#     for k in L[L.index(j)+1:]:
#       # R.append(str(i)+str(j)+str(k))
#       a = i+j+k 
#       R.append(a)
#       if a <= M :
#         result = max(result, a)

# # print(R)
# print(result)




# # decomposition

# import sys

# N = int(sys.stdin.readline().strip())
# d = 0

# for i in range(N):
#   if i+sum(map(int,str(i))) == N:  # 정수 각 자리수 더하기
#     d = 1
#     print(i)
#     break

# if d == 0:
#   print(0)



# build ranking

# import sys
# N = int(sys.stdin.readline().strip())
# L = []
# # R = [1] * N

# for _ in range(N):
#   L.append(list(map(int, sys.stdin.readline().strip().split())))

# for i in L:
#   rank = 1
#   for j in L:
#     if i[0] < j[0] and i[1] < j[1]:
#       # R[L.index(i)] += 1
#       rank += 1
#   print(rank, end= ' ')

# print(*R)  #? 이거 왜 안되는 것인가??




# repaint the chessboard

# 가장 왼쪽 위가 B거나 W인 완전한 8X8 보드판과 잘라낸 모든 8X8 보드판의 다른 개수를 비교 -> 최소값 출력.

# import sys

# N,M = map(int,sys.stdin.readline().split())
# chess_L = []
# # counter_W = 0
# # counter_B = 0

# for _ in range(N):
#   temp_L = list(sys.stdin.readline().strip())
#   # temp_L = sys.stdin.readline().strip() #. string도 iterable이기 때문에 굳이 2차원 리스트를 만들며 저장할 필요가 없이 array[i][j]로 접근가능 하다.
#   # counter_B += temp_L.count('B')
#   # counter_W += temp_L.count('W')
#   chess_L.append(temp_L)


# def make_chessboard(N,M):
#   chessboard_lefttop_is_B = []
#   chessboard_lefttop_is_W = []
#   for i in range(N):
#     temp_B = []
#     temp_W = []
#     for j in range(M):
#       if i % 2 == 0:
#         if j % 2 == 0:
#           temp_B.append('B')
#           temp_W.append('W')
#         else :
#           temp_B.append('W')
#           temp_W.append('B')
      
#       else:
#         if j % 2 == 0:
#           temp_B.append('W')
#           temp_W.append('B')
#         else :
#           temp_B.append('B')
#           temp_W.append('W')

#     chessboard_lefttop_is_B.append(temp_B)
#     chessboard_lefttop_is_W.append(temp_W)

#   return chessboard_lefttop_is_B, chessboard_lefttop_is_W

# exe_chessboard_lefttop_is_B, exe_chessboard_lefttop_is_W = make_chessboard(8,8)

# count_a = []
# count_b = []

# for i in range(N-8 + 1):
#   for j in range(M-8 + 1):
#     temp_a = 0
#     temp_b = 0
#     for k in range(8):
#       for l in range(8):
#         if exe_chessboard_lefttop_is_B[k][l] != chess_L[i+k][j+l]:
#           temp_a += 1
#         if exe_chessboard_lefttop_is_W[k][l] != chess_L[i+k][j+l]:
#           temp_b += 1
#     count_a.append(temp_a)
#     count_b.append(temp_b)

# print(min(min(count_a), min(count_b)))





# brute force니까 그냥 1부터 쭉 무식하게 찾아보자 

# import sys
# N = int(sys.stdin.readline())
# result = 1

# while True:
#   result += 1
#   if '666' in str(result):
#     N -= 1
#   if N == 0:
#     print(result)
#     break




# #- BAEKJOON 19532. <The math class is conducted online>
# a,b,c,d,e,f = map(int,input().split())
# for x in range(-999,1000):
#   for y in range(-999,1000):
#     if a*x+b*y==c and d*x+e*y==f:
#       print(x,y)
#       exit()




#- <Minimum Rectangle>
#. 'Always think simply first!'
# 문제 설명
# 명함 지갑을 만드는 회사에서 지갑의 크기를 정하려고 합니다. 다양한 모양과 크기의 명함들을 모두 수납할 수 있으면서, 작아서 들고 다니기 편한 지갑을 만들어야 합니다. 이러한 요건을 만족하는 지갑을 만들기 위해 디자인팀은 모든 명함의 가로 길이와 세로 길이를 조사했습니다.

# 아래 표는 4가지 명함의 가로 길이와 세로 길이를 나타냅니다.

# 명함 번호	가로 길이	세로 길이
# 1	60	50
# 2	30	70
# 3	60	30
# 4	80	40
# 가장 긴 가로 길이와 세로 길이가 각각 80, 70이기 때문에 80(가로) x 70(세로) 크기의 지갑을 만들면 모든 명함들을 수납할 수 있습니다. 하지만 2번 명함을 가로로 눕혀 수납한다면 80(가로) x 50(세로) 크기의 지갑으로 모든 명함들을 수납할 수 있습니다. 이때의 지갑 크기는 4000(=80 x 50)입니다.

# 모든 명함의 가로 길이와 세로 길이를 나타내는 2차원 배열 sizes가 매개변수로 주어집니다. 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# sizes의 길이는 1 이상 10,000 이하입니다.
# sizes의 원소는 [w, h] 형식입니다.
# w는 명함의 가로 길이를 나타냅니다.
# h는 명함의 세로 길이를 나타냅니다.
# w와 h는 1 이상 1,000 이하인 자연수입니다.
# 입출력 예
# sizes	result
# [[60, 50], [30, 70], [60, 30], [80, 40]]	4000
# [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]	120
# [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]	133
# 입출력 예 설명
# 입출력 예 #1
# 문제 예시와 같습니다.

# 입출력 예 #2
# 명함들을 적절히 회전시켜 겹쳤을 때, 3번째 명함(가로: 8, 세로: 15)이 다른 모든 명함보다 크기가 큽니다. 따라서 지갑의 크기는 3번째 명함의 크기와 같으며, 120(=8 x 15)을 return 합니다.

# 입출력 예 #3
# 명함들을 적절히 회전시켜 겹쳤을 때, 모든 명함을 포함하는 가장 작은 지갑의 크기는 133(=19 x 7)입니다.


# def solution(sizes):
#     big,small = 0,0
#     for size in sizes:
#         if max(size) > big:
#             big = max(size)
#         if min(size) > small:
#             small = min(size)
#     return big*small

# sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]	
# print(solution(sizes)) #4000
# sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]	
# print(solution(sizes)) #120
# sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]	
# print(solution(sizes)) #133




#- <Mock exam>
#. 'Learned about 1. List comprehension, 2. method of using enumerate'
# 문제 설명
# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한 조건
# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
# 입출력 예
# answers	return
# [1,2,3,4,5]	[1]
# [1,3,2,4,2]	[1,2,3]
# 입출력 예 설명
# 입출력 예 #1

# 수포자 1은 모든 문제를 맞혔습니다.
# 수포자 2는 모든 문제를 틀렸습니다.
# 수포자 3은 모든 문제를 틀렸습니다.
# 따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.

# 입출력 예 #2

# 모든 사람이 2문제씩을 맞췄습니다.

# def solution(answers):
#     math_dropout = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
#     result = [0]*3
#     for i in range(len(answers)):
#         for j in range(3):
#             if answers[i] == math_dropout[j][i%len(math_dropout[j])]:
#                 result[j] += 1      
#     return [i+1 for i,v in enumerate(result) if v == max(result)]

# answers = [1,2,3,4,5]
# print(solution(answers)) #[1]
# answers = [1,3,2,4,2]	
# print(solution(answers)) #[1,2,3]



#- <Finding prime numbers>
#. 1. Sieve of Eratosthenes : A method to find prime numbers up to n. iterate up to the square root of n+1 and filter out its multiples.
#. 2. How to use permutations and combinations libraries.'                       
# 문제 설명
# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# numbers는 길이 1 이상 7 이하인 문자열입니다.
# numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
# 입출력 예
# numbers	return
# "17"	3
# "011"	2
# 입출력 예 설명
# 예제 #1
# [1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

# 예제 #2
# [0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.

# 11과 011은 같은 숫자로 취급합니다.

#- 1. 에라토스테네스 체 짜서 2~numbers까지 소수들 구하고,
#- 2. numbers로 만들 수 있는 모든 조합을 짜서 소수가 맞는지 확인해서 출력. 
# import itertools

# def solution(numbers):
#     permutation = set([int(''.join(n)) for i in range(1,len(numbers)+1) for n in itertools.permutations(numbers, i)])
#     primes = prime_list(max(permutation))
#     return len([n for n in permutation if n in primes])

# #- 2 ~ num 까지 소수 리스트 반환
# def prime_list(num):
#     m = int((num+1)**0.5)
#     sieve = [True] * (num+1)
#     for i in range(2,m+1):
#         if sieve[i] == True:
#             for j in range(i+i,num+1,i):
#                 sieve[j] = False
#     return [i for i, v in enumerate(sieve) if v and i > 1]

# numbers = "17"
# print(solution(numbers)) #3
# numbers = "011"
# print(solution(numbers)) #2


#- <Carpet>
#. If we check the range of variables and it does not exceed the time complexity, a brute force search can be advantageous.
#. (In fact, this problem can be solved by setting up two equations for length and area and finding the solution to the quadratic equation.)
# 문제 설명
# Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

# carpet.png

# Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

# Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
# 노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
# 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.
# 입출력 예
# brown	yellow	return
# 10	2	[4, 3]
# 8	1	[3, 3]
# 24	24	[8, 6]
# 출처

# def solution(brown, yellow):
#     temp = 2
#     while True:
#         # breakpoint()
#         expected_w = (brown - temp) // 2
#         expected_h = (temp//2) + 2
#         if brown + yellow == expected_w*expected_h:
#             return [expected_w,expected_h]
#         temp += 2

# brown = 10
# yellow = 2
# print(solution(brown, yellow)) #[4,3]
# brown = 8
# yellow = 1
# print(solution(brown, yellow)) #[3,3]
# brown = 24
# yellow = 24
# print(solution(brown, yellow)) #[8,6]




#- <Fatigue>
#. Calculate the time complexity first. 
#. The total number of cases is O(n! * n) : 40320*8. Isn't this within the time complexity?
# 문제 설명
# XX게임에는 피로도 시스템(0 이상의 정수로 표현합니다)이 있으며, 일정 피로도를 사용해서 던전을 탐험할 수 있습니다. 이때, 각 던전마다 탐험을 시작하기 위해 필요한 "최소 필요 피로도"와 던전 탐험을 마쳤을 때 소모되는 "소모 피로도"가 있습니다. "최소 필요 피로도"는 해당 던전을 탐험하기 위해 가지고 있어야 하는 최소한의 피로도를 나타내며, "소모 피로도"는 던전을 탐험한 후 소모되는 피로도를 나타냅니다. 예를 들어 "최소 필요 피로도"가 80, "소모 피로도"가 20인 던전을 탐험하기 위해서는 유저의 현재 남은 피로도는 80 이상 이어야 하며, 던전을 탐험한 후에는 피로도 20이 소모됩니다.

# 이 게임에는 하루에 한 번씩 탐험할 수 있는 던전이 여러개 있는데, 한 유저가 오늘 이 던전들을 최대한 많이 탐험하려 합니다. 유저의 현재 피로도 k와 각 던전별 "최소 필요 피로도", "소모 피로도"가 담긴 2차원 배열 dungeons 가 매개변수로 주어질 때, 유저가 탐험할수 있는 최대 던전 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# k는 1 이상 5,000 이하인 자연수입니다.
# dungeons의 세로(행) 길이(즉, 던전의 개수)는 1 이상 8 이하입니다.
# dungeons의 가로(열) 길이는 2 입니다.
# dungeons의 각 행은 각 던전의 ["최소 필요 피로도", "소모 피로도"] 입니다.
# "최소 필요 피로도"는 항상 "소모 피로도"보다 크거나 같습니다.
# "최소 필요 피로도"와 "소모 피로도"는 1 이상 1,000 이하인 자연수입니다.
# 서로 다른 던전의 ["최소 필요 피로도", "소모 피로도"]가 서로 같을 수 있습니다.
# 입출력 예
# k	dungeons	result
# 80	[[80,20],[50,40],[30,10]]	3
# 입출력 예 설명
# 현재 피로도는 80입니다.

# 만약, 첫 번째 → 두 번째 → 세 번째 던전 순서로 탐험한다면

# 현재 피로도는 80이며, 첫 번째 던전을 돌기위해 필요한 "최소 필요 피로도" 또한 80이므로, 첫 번째 던전을 탐험할 수 있습니다. 첫 번째 던전의 "소모 피로도"는 20이므로, 던전을 탐험한 후 남은 피로도는 60입니다.
# 남은 피로도는 60이며, 두 번째 던전을 돌기위해 필요한 "최소 필요 피로도"는 50이므로, 두 번째 던전을 탐험할 수 있습니다. 두 번째 던전의 "소모 피로도"는 40이므로, 던전을 탐험한 후 남은 피로도는 20입니다.
# 남은 피로도는 20이며, 세 번째 던전을 돌기위해 필요한 "최소 필요 피로도"는 30입니다. 따라서 세 번째 던전은 탐험할 수 없습니다.
# 만약, 첫 번째 → 세 번째 → 두 번째 던전 순서로 탐험한다면

# 현재 피로도는 80이며, 첫 번째 던전을 돌기위해 필요한 "최소 필요 피로도" 또한 80이므로, 첫 번째 던전을 탐험할 수 있습니다. 첫 번째 던전의 "소모 피로도"는 20이므로, 던전을 탐험한 후 남은 피로도는 60입니다.
# 남은 피로도는 60이며, 세 번째 던전을 돌기위해 필요한 "최소 필요 피로도"는 30이므로, 세 번째 던전을 탐험할 수 있습니다. 세 번째 던전의 "소모 피로도"는 10이므로, 던전을 탐험한 후 남은 피로도는 50입니다.
# 남은 피로도는 50이며, 두 번째 던전을 돌기위해 필요한 "최소 필요 피로도"는 50이므로, 두 번째 던전을 탐험할 수 있습니다. 두 번째 던전의 "소모 피로도"는 40이므로, 던전을 탐험한 후 남은 피로도는 10입니다.
# 따라서 이 경우 세 던전을 모두 탐험할 수 있으며, 유저가 탐험할 수 있는 최대 던전 수는 3입니다.

from itertools import permutations

def solution(k, dungeons):
    dungeons_permutations = list(permutations(dungeons,len(dungeons)))
    answer = [0]*len(dungeons_permutations)
    # breakpoint()
    for i,v in enumerate(dungeons_permutations):
        temp = k
        for m,u in v:
            if temp < m:
                break
            else:
                answer[i] += 1
                temp -= u
    return max(answer)

#. Using DFS
# answer = 0
# N = 0
# visited = []

# def dfs(k, cnt, dungeons):
#     global answer
#     if cnt > answer:
#         answer = cnt

#     for j in range(N):
#         if k >= dungeons[j][0] and not visited[j]:
#             visited[j] = 1
#             dfs(k - dungeons[j][1], cnt + 1, dungeons)
#             visited[j] = 0

# def solution(k, dungeons):
#     global N, visited
#     N = len(dungeons)
#     visited = [0] * N
#     dfs(k, 0, dungeons)
#     return answer

#? Using recursion
# solution = lambda k, d: max([solution(k - u, d[:i] + d[i+1:]) + 1 for i, (m, u) in enumerate(d) if k >= m] or [0])


k = 80	
dungeons = [[80,20],[50,40],[30,10]]	
print(solution(k,dungeons)) #3 