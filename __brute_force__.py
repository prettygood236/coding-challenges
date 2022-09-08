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

import sys
N = int(sys.stdin.readline().strip())
L = []
# R = [1] * N

for _ in range(N):
  L.append(list(map(int, sys.stdin.readline().strip().split())))

for i in L:
  rank = 1
  for j in L:
    if i[0] < j[0] and i[1] < j[1]:
      # R[L.index(i)] += 1
      rank += 1
  print(rank, end= ' ')

# print(*R)  #? 이거 왜 안되는 것인가??