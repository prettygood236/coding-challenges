
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
import sys
n = int(sys.stdin.readline())
distances = list(map(int,sys.stdin.readline().split()))
costs = list(map(int,sys.stdin.readline().split()))

value = costs[0]
result = 0
for i in range(n-1):
  if costs[i] < value:
    value = costs[i]
  result += value * distances[i]

print(result)