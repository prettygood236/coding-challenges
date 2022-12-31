
#- <Prefix Sum 4>

# n,m = map(int,input().split())
# data = list(map(int,input().split()))
# prefix_sum = [0]
# for i in range(n):
#   prefix_sum.append(prefix_sum[i]+data[i])

# for _ in range(m):
#   i,j = map(int,input().split())
#   print(prefix_sum[j]-prefix_sum[i-1])



#- <Sequence>

# n,k = map(int,input().split())
# data = list(map(int,input().split()))
# prefix_sum = [0]

# for i in range(n):
#   prefix_sum.append(prefix_sum[i]+data[i])

# result = prefix_sum[0+k] - prefix_sum[0]
# for i in range(n-k+1):
#   temp = prefix_sum[i+k] - prefix_sum[i]
#   result = max(result,temp)

# print(result)



#- <Human-Computer interaction>
#! sys.stdin.readline 은 input과 달리 한줄을 한번에 버퍼에 저장하고, (input은 입력할때마다 저장)
#! prompt message를 받아 출력하는 기능이 없기 때문에 속도가 더 빠르다. 
import sys
S = sys.stdin.readline().strip()
N = int(sys.stdin.readline())
L = [[0 for _ in range(26)] for _ in range(len(S))]
L[0][ord(S[0]) - 97] = 1

for i in range(1, len(S)):
  L[i][ord(S[i]) - 97] = 1
  for j in range(26):
    L[i][j] += L[i - 1][j]

for i in range(N):
  a,l,r = sys.stdin.readline().split()
  l,r = map(int, [l,r])
  result = L[r][ord(a) - 97] - L[l - 1][ord(a) - 97]
  if l == 0:
    result = L[r][ord(a) - 97]
  print(result)






#- <Sum of the rest>

# N,M = map(int,input().split())
# data = list(map(int,input().split()))
# prefix_sum = [0]
# r = [0]*M

# for i in range(len(data)):
#   sum = prefix_sum[i]+data[i]
#   prefix_sum.append(sum)
#   r[sum%M] += 1

# count = r[0]

# for i in range(len(r)):
#   count += r[i]*(r[i]-1)//2

# print(count)





#- <Prefix Sum 5>

# n,m = map(int, input().split())

# table = []
# for i in range(n):
#     table.append(list(map(int, input().split())))

# prefix_sums = [[0 for _ in range(n+1)] for _ in range(n+1)]
# for i in range(1,n+1):
#   for j in range(1,n+1):
#     prefix_sums[i][j] = prefix_sums[i-1][j] + prefix_sums[i][j-1] - prefix_sums[i-1][j-1] + table[i-1][j-1]

# for _ in range(m):
#   x1, y1, x2, y2 = map(int,input().split())
#   submatrix_sum = prefix_sums[x2][y2] - prefix_sums[x2][y1-1] - prefix_sums[x1-1][y2] + prefix_sums[x1-1][y1-1]
#   print(submatrix_sum)




#- <Repaint the chessboard 2>

# import sys

# def find_min(color):
#   new_board = [[0 for _ in range(m)] for _ in range(n)]
#   for i in range(n):
#     for j in range(m):
#       if (i+j) % 2 == 0 and board[i][j] != color:
#         new_board[i][j] = 1
#       if (i+j) % 2 != 0 and board[i][j] == color:
#         new_board[i][j] = 1

#   prefix_sum = [[0 for _ in range(m+1)] for _ in range(n+1)]
#   for i in range(1,n+1):
#     for j in range(1,m+1):
#       prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + new_board[i-1][j-1]

#   result = sys.maxsize
#   for i in range(n-k+1): 
#     for j in range(m-k+1):
#       result = min(result, prefix_sum[k+i][k+j] - prefix_sum[k+i][j] - prefix_sum[i][k+j] + prefix_sum[i][j])
  
#   return result

# n, m, k = map(int,input().split())
# board = [list(input()) for _ in range(n)]
# print(min(find_min('B'),find_min('W')))













