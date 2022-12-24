
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
#. 아 왜 50점이야 아
import copy
S = input()
L = [{'a':0, 'b':0, 'c':0, 'd':0,'e':0, 'f':0, 'g':0, 'h':0,'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0, 'v':0, 'w':0,'x':0, 'y':0, 'z':0} for _ in range(len(S))]
L[0][S[0]] = 1

for i in range(1,len(S)):
  L[i] = copy.deepcopy(L[i-1])
  L[i][S[i]] += 1

for i in range(int(input())):
  a,l,r = input().split()
  l,r = map(int,[l,r])
  if l == 0:
    print(L[r][a])
    continue
  print(L[r][a]-L[l-1][a])





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
    # table.append(list(map(int, input().split())))

# prefix_sums = [[0 for _ in range(n+1)] for _ in range(n+1)]
# for i in range(1,n+1):
#   for j in range(1,n+1):
#     prefix_sums[i][j] = prefix_sums[i-1][j] + prefix_sums[i][j-1] - prefix_sums[i-1][j-1] + table[i-1][j-1]

# for _ in range(m):
#   x1, y1, x2, y2 = map(int,input().split())
#   submatrix_sum = prefix_sums[x2][y2] - prefix_sums[x2][y1-1] - prefix_sums[x1-1][y2] + prefix_sums[x1-1][y1-1]
#   print(submatrix_sum)




#- <Repaint the chessboard 2>












