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




#. BAEKJOON 19532. <The math class is conducted online>
a,b,c,d,e,f = map(int,input().split())

for x in range(-999,1000):
  for y in range(-999,1000):
    if a*x+b*y==c and d*x+e*y==f:
      print(x,y)
      exit()