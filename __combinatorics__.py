
#. BAEKJOON 15439. <Vera and Outfits>
# n = int(input())
# print(n*(n-1))



#. BAEKJOON 24723. <The Green Tower>
# n = int(input())
# print(2**n)



#. BAEKJOON 11050. <Binomial Coefficient>
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



#. BAEKJOON 1010. <Building bridges>
#. M^C^N을 구하는 문제. 
# import sys

# T = int(sys.stdin.readline())


# def factorial(x):
#   if x > 1:
#     return x * factorial(x-1)
#   else:
#     return 1 

# for _ in range(T):
#   N,M = map(int,sys.stdin.readline().split())
#   print(factorial(M) // (factorial(M-N)*factorial(N)))
