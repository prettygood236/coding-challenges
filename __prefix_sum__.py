
#* Prefix Sum


# n,m = map(int,input().split())
# data = list(map(int,input().split()))
# prefix_sum = [0]
# for i in range(n):
#   prefix_sum.append(prefix_sum[i]+data[i])

# for _ in range(m):
#   i,j = map(int,input().split())
#   print(prefix_sum[j]-prefix_sum[i-1])



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



#. 아 왜 50점이야 아
# import copy
# S = input()
# L = [{'a':0, 'b':0, 'c':0, 'd':0,'e':0, 'f':0, 'g':0, 'h':0,'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0, 'v':0, 'w':0,'x':0, 'y':0, 'z':0} for _ in range(len(S))]
# L[0][S[0]] = 1

# for i in range(1,len(S)):
#   L[i] = copy.deepcopy(L[i-1])
#   L[i][S[i]] += 1

# for i in range(int(input())):
#   a,l,r = input().split()
#   l,r = map(int,[l,r])
#   if l == 0:
#     print(L[r][a])
#     continue
#   print(L[r][a]-L[l-1][a])





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








N,M = map(int,input().split())
data = []
for _ in range(N):
  data.append(list(map(int,input().split())))

prefix_sum = [[0] for _ in range(N)]

for i in range(N):
  for j in range(N):
    if i == 0:
      sum = prefix_sum[i][j] + data[i][j]
    else :
      sum = prefix_sum[i-1][j] + prefix_sum[i][j] + data[i][j]
    prefix_sum[i].append(sum)

print(prefix_sum)
