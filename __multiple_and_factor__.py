# import sys

# while True:
#   L = list(map(int,sys.stdin.readline().split()))
#   if L[0] == 0 and L[1] == 0:
#     break
#   if max(L) % min(L) == 0:
#     if L[0] > L[1]:
#       print('multiple')
#     if L[1] > L[0]:
#       print('factor')
#   else:
#     print('neither')





# import sys
# cnt = int(sys.stdin.readline())
# L = list(map(int,sys.stdin.readline().split()))

# print(max(L)*min(L))


    


# import sys
# a, b = map(int,sys.stdin.readline().split())
# if a > b:
#   temp = a
#   a = b
#   b = temp

# G = 1
# for i in range(2,a+1):
#   if a % i == 0 and b % i == 0:
#     G = i

# L = (a*b) // G

# print(G)
# print(L)




#* Euclidean algorithm(유클리드 호제법)
#! A,B의 최대공약수 G를 구하는 방법.
#! A = B*Q + R (Q는 몫, R은 나머지) 일 때, GCD(A,B) = GCD(B,R)이고, 이를 반복하여 R이 0이 될 때 B가 최대공약수 G이다. 
#. (증명) A = a*G, B = b*G (a와 b는 서로소)-> a*G = b*G*Q + R -> R = (a-bQ)G, B = bG 이다. 
#. 따라서 이 때, a-bQ와 b가 서로소이면 R과 B의 최대공약수도 G이다!.
#. a-bQ와 b가 서로소가 아니라고 가정해보자. 공통의 약수 t가 존재할 것이다. 
#. a-bQ = mt, b = nt -> a-ntQ = mt -> a = (m+nQ)t, b = nt
#. 그러나 위에서 a와 b는 서로소라고 했다. 따라서 a-bQ와 b는 서로소가 될 수 없고 그러므로 
#! R과 B의 최대공약수도 G이다!.

#* 최대공약수(GCD)와 최소공배수(LCM)
#. A * B = aG * bG = a*b*G*G (a,b는 서로소)
#. 따라서 a*b*G가 최소공배수이다. 
#. A * B / G = L

# import sys

# T = int(sys.stdin.readline())

# for _ in range(T):
#   m,n = map(int,sys.stdin.readline().split())
#   A = m
#   B = n
#   while True:
#     R = A % B
#     if R == 0:
#       print(int(m*n/B))
#       break
#     A = B
#     B = R





#. a = MQ + R, b = MQ' + R c = MQ'' + R
#. a-b = M(Q-Q'), b-c = M(Q'-Q'')
#. M은 a-b, b-c의 공약수이므로, 
#* 즉, M은 a-b, b-c의 최대공약수의 약수이다. 

# import sys
        
# N = int(sys.stdin.readline())
# L = sorted(list(int(sys.stdin.readline()) for _ in range(N)))
# R = []

# D = [L[i+1]-L[i] for i in range(N-1)] 

# # Uclidean Algorithm
# def GCD(a,b):
#   while True:
#     r = a % b
#     if r == 0:
#       return b
#     a = b
#     b = r

# G = D[0]
# for i in range(1,len(D)):
#   G = GCD(G, D[i])

# for i in range(1, int(G**0.5)+1):
#   if G % i == 0:
#     if i**2 == G:
#       R.append(i)

#     else: 
#       R += [i,G//i]

# R.remove(1)
# R.sort()

# for i in R:
#   print(i,sep=' ')




#* 기약분수 : 분자, 분모의 공약수가 1뿐인 분수. 
#. 분자, 분모를 분자, 분모의 최대공약수로 나누면 된다. 

# import sys
# N = int(sys.stdin.readline())
# L = list(map(int,sys.stdin.readline().split()))

# def GCD(a,b):
#   while True:
#     r = a % b
#     if r == 0 :
#       return b  
#     a = b
#     b = r

# for i in range(1,len(L)):
#   d = GCD(L[0],L[i])
#   print(int(L[0]/d),'/',int(L[i]/d),sep='')




# 조합 nCk를 구하는 문제 
# import sys

# N,K = map(int,sys.stdin.readline().split())
# a = 1
# b = 1

# for _ in range(K):
#   a *= N
#   b *= K
#   N -= 1
#   K -= 1

# print(a//b)




# dynamic programming을 이용한 이항계수 nCk 정리.

import sys

N,K = map(int,sys.stdin.readline().split())
dp = [[0]*(i+1) for i in range(1001)]

dp[0][0] = 1

for i in range(1,1001):
  for j in range(i):
    if j == 0 or j == i:
      dp[i][j] = 1
      dp[i][i] = 1
    else:
      dp[i][j] = dp[i-1][j-1] + dp[i-1][j] 

print(dp[N][K]%10007)

