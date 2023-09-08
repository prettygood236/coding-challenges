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




# #. BAEKJOON 19532. <The math class is conducted online>
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