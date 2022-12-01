
#* Prefix Sum


# n,m = map(int,input().split())
# data = list(map(int,input().split()))
# prefix_sum = [0]
# for i in range(n):
#   prefix_sum.append(prefix_sum[i]+data[i])

# for _ in range(m):
#   i,j = map(int,input().split())
#   print(prefix_sum[j]-prefix_sum[i-1])



n,k = map(int,input().split())
data = list(map(int,input().split()))
prefix_sum = [0]

for i in range(n):
  prefix_sum.append(prefix_sum[i]+data[i])

result = prefix_sum[0+k] - prefix_sum[0]
for i in range(n-k+1):
  temp = prefix_sum[i+k] - prefix_sum[i]
  result = max(result,temp)

print(result)