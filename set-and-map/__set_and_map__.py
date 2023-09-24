
# M = int(sys.stdin.readline())
# L = list(map(int,sys.stdin.readline().split()))
# Set_b = set(L)

# intersection = Set_a & Set_b

# for i in range(M):
#   if L[i] in intersection:
#     print(1)
#   else:
#     print(0)



#. In set, the time complexity of finding an element is also O(1) like a dictionary.
# import sys 
# N,M = map(int,sys.stdin.readline().split())
# S = set(sys.stdin.readline().strip() for _ in range(N))
# count = 0

# for _ in range(M):
#   temp = sys.stdin.readline().strip()
#   if temp in S:
#     count += 1

# print(count)



# import sys
# N,M = map(int,sys.stdin.readline().split())
# D = {}

# for i in range(1,N+1):
#   temp = sys.stdin.readline().strip()
#   D[str(i)] = temp
#   D[temp] = str(i)

# for _ in range(M):
#   Q = sys.stdin.readline().strip()
#   print(D[Q])








# import sys
# N,M = map(int,sys.stdin.readline().split())

# S_a = set(sys.stdin.readline().strip() for _ in range(N))
# S_b = set(sys.stdin.readline().strip() for _ in range(M))

# intersection = S_a & S_b
# L = list(intersection)
# L.sort()

# print(len(L))
# for i in L:
#   print(i)




# import sys
# N,M = map(int,sys.stdin.readline().split())

# Set_A = set(map(int,sys.stdin.readline().split()))
# Set_B = set(map(int,sys.stdin.readline().split()))

# print(len(Set_A ^ Set_B))
# # print(len((Set_A - Set_B) | (Set_B-Set_A)))




# import sys

# str = sys.stdin.readline().strip()
# S = set()

# for i in range(1,len(str)+1):
#   for j in range(len(str)+1-i):
#     temp = str[j:i+j]
#     S.add(temp)

# print(len(S))





#- BAEKJOON 25192. <A bear who greets well>
# n = int(input())
# people_set = set()
# count = 0 
# for _ in range(n):
#   s = input()
#   if s == 'ENTER':
#     people_set = set()
#   else:
#     if s in people_set:
#       continue
#     else:
#       people_set.add(s)
#       count += 1

# print(count)



#- BAEKJOON 26069. <ChongChong Who has a strong attachment>
# n = int(input())
# people_set = set(['ChongChong'])
# count = 1
# for _ in range(n):
#   a,b = input().split()
#   if a in people_set and not b in people_set:
#     people_set.add(b)
#     count += 1
#   if b in people_set and not a in people_set:
#     people_set.add(a)
#     count += 1

# print(count)