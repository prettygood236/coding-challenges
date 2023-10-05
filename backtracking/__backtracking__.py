import sys
N,M = map(int,sys.stdin.readline().split())
s = []

def dfs():
  if len(s) == M:
    print(' '.join(map(str,s)))
    return

  for i in range(1,N+1):
    if i not in s:
      s.append(i)
      dfs()
      s.pop()

dfs()




# N,M = map(int,input().split())
# s = []

# def dfs():
#   if len(s) == M:
#     print(' '.join(map(str,s)))
#     return

#   for i in range(1,N+1):
#     if i not in s:
#       if len(s) == 0 or s[-1] < i:
#         s.append(i)
#         dfs()
#         s.pop()

# dfs()





# N,M = map(int,input().split())
# s = []

# def dfs():
#   if len(s) == M:
#     print(' '.join(map(str,s)))
#     return
  
#   for i in range(1,N+1):
#     s.append(i)
#     dfs()
#     s.pop()   

# dfs()




# N,M = map(int,input().split())
# s = []

# def dfs():
#   if len(s) == M:
#     print(' '.join(map(str,s)))
#     return

#   for i in range(1,N+1):
#     if len(s) == 0 or s[-1] <= i:
#       s.append(i)
#       dfs()
#       s.pop()

# dfs() 




# N = int(input())
# col = [0] * N
# result = 0

# def n_queens(i):
#   global result
#   if i == N:
#     # print(col[:])
#     result += 1
#   else :
#     for j in range(N):
#       col[i] = j
#       if is_promising(i):
#         n_queens(i+1)

# def is_promising(i):
#   for x in range(i):
#     if col[i] == col[x] or abs(col[i]-col[x]) == i - x:
#       return False
#   return True

# n_queens(0)
# print(result)





# board = [list(map(int,input().split())) for _ in range(9)]
# blank = []

# for i in range(9):
#   for j in range(9):
#     if board[i][j] == 0:
#       blank.append([i,j])

# def sudoku(n):
#   if n == len(blank):
#     for i in board:
#       print(*i)
#     exit()
#   else:
#     x = blank[n][0]
#     y = blank[n][1]
#     for k in range(1,10):      
#       if is_promising(x,y,k):
#         board[x][y] = k
#         sudoku(n+1)
#       board[x][y] = 0 

# def is_promising(x,y,k):
#   # row_check
#   for i in range(9):
#     if k == board[x][i]:
#       return False

#   # column_check
#   for i in range(9):
#     if k == board[i][y]:
#       return False

#   # 이렇게 새 리스트를 만들면 시간초과가 나는구나!
#   # rotated = list(map(list,zip(*board))) 
#   # if k in rotated[y]:
#   #   return False

#   # block_check
#   nx = x // 3 * 3
#   ny = y // 3 * 3
#   for i in range(3):
#     for j in range(3):
#       if k == board[nx+i][ny+j]:
#         return False

#   return True

# sudoku(0)


# 0 0 5 3 0 0 0 0 0
# 8 0 0 0 0 0 0 2 0
# 0 7 0 0 1 0 5 0 0
# 4 0 0 0 0 5 3 0 0
# 0 1 0 0 7 0 0 0 6
# 0 0 3 2 0 0 0 8 0
# 0 6 0 5 0 0 0 0 9
# 0 0 4 0 0 0 0 3 0
# 0 0 0 0 0 9 7 0 0

# 8 0 0 0 0 0 0 0 0
# 0 0 3 6 0 0 0 0 0
# 0 7 0 0 9 0 2 0 0 
# 0 5 0 0 0 7 0 0 0
# 0 0 0 0 4 5 7 0 0
# 0 0 0 1 0 0 0 3 0
# 0 0 1 0 0 0 0 6 8
# 0 0 8 5 0 0 0 1 0
# 0 9 0 0 0 0 4 0 0 






# #! 상태트리를 dfs하는 backtracking은 결국 넣고 돌고 빼고! 

# N = int(input())
# L = list(map(int,input().split()))
# O = list(map(int,input().split()))
# s = []
# R = []


# def dfs():
#   if sum(O) == 0:
#     result = L[0]
#     for i in range(len(s)):
#       if s[i] == 0:
#         result += L[i+1]
#       if s[i] == 1:
#         result -= L[i+1]
#       if s[i] == 2:
#         result *= L[i+1]
#       if s[i] == 3:
#         if result <= 0:
#           result = (abs(result) // L[i+1])*(-1)
#         else :
#           result //= L[i+1]
#     R.append(result)
#     return
#   else :
#     for i in range(4):
#       if O[i] != 0:
#         s.append(i)  #! 넣고! 
#         O[i] -= 1 
#         dfs()  #! 돌고!
#         s.pop()  #! 빼고!
#         O[i] += 1

# dfs()
# print(max(R))
# print(min(R))







# N = int(input())
# l = list(list(map(int,input().split())) for _ in range(N))
# t = []
# team_s = []
# team_l = []
# choice = []
# temp = set(i for i in range(N))
# R = []

# def combination(N,M,L):
#   if len(t) == M:
#     L.append(t[:])  
#     return
#   else:
#     for i in range(N):
#       if i not in t :
#         if len(t) == 0 or t[-1] < i: #. 0 1과 1 0을 중복으로 보는 조건.  
#           t.append(i)
#           combination(N,M,L)
#           t.pop()

# combination(N,N//2,team_s)
# for i in team_s:
#   team_l.append(list(temp - set(i)))
# combination(N//2,2,choice)
# for i in range(len(team_s)):
#   sum_s = 0
#   sum_l = 0
#   for j in range(len(choice)):
#     sum_s += l[team_s[i][choice[j][0]]][team_s[i][choice[j][1]]] + l[team_s[i][choice[j][1]]][team_s[i][choice[j][0]]]
#     sum_l += l[team_l[i][choice[j][0]]][team_l[i][choice[j][1]]] + l[team_l[i][choice[j][1]]][team_l[i][choice[j][0]]]
#   R.append(abs(sum_s-sum_l))

# print(min(R))
