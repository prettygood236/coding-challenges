
#- <Making Quad-Tree>
# import sys

# n = int(sys.stdin.readline())
# l = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
# w = 0
# b = 0

# def solve(x,y,n):
#   global w,b
#   t = l[y][x]
#   for i in range(y,y+n):
#     for j in range(x,x+n):
#       if l[i][j] != t:
#         solve(x,y,n//2)
#         solve(x,y+n//2,n//2)
#         solve(x+n//2,y,n//2)
#         solve(x+n//2,y+n//2,n//2)
#         return
#   if t == 0:
#     w += 1
#   else:
#     b += 1  

# solve(0,0,n)
# print(w,b,sep='\n')




#- <Quad-Tree> 
#. 시작, 끝을 n, x,y를 이용해 정하기! n은 계속 1/2n으로 변화

# import sys

# n = int(sys.stdin.readline())
# l = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]
# result = ''

# def solve(x,y,n):
#   global result
#   t = l[y][x]
#   for i in range(y,y+n):
#     for j in range(x,x+n):
#       if l[i][j] != t:
#         result += '('
#         solve(x,y,n//2)
#         solve(x+n//2,y,n//2)
#         solve(x,y+n//2,n//2)
#         solve(x+n//2,y+n//2,n//2)
#         result += ')'
#         return
#   result += str(t)

# solve(0,0,n)
# print(result)





#- <Spatial-Tree>

# import sys

# n = int(sys.stdin.readline())
# l = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
# result = [0]*3

# def solve(x,y,n):
#   t = l[y][x]
#   for i in range(y,y+n):
#     for j in range(x,x+n):
#       if l[i][j] != t:
#         n = n//3
#         for k in range(3):
#           solve(x,y,n)
#           solve(x+n,y,n)
#           solve(x+(2*n),y,n)
#           y += n
#         return
#   if t == -1:
#     result[0] += 1
#   if t == 0:
#     result[1] += 1
#   if t == 1:
#     result[2] += 1
#   return

# solve(0,0,n)
# print(*result, sep='\n')







#- <Modulo Powers>
#. 모듈로 거듭제곱
#! A^B mod C = ( (A mod C)^B ) mod C
#! 5^117 mod 19 = ( 5^1 mod 19 * 5^4 mod 19 * 5^16 mod 19 * 5^32 mod 19 * 5^64 mod 19) mod 19

#! 임의의 B에서 A^B mod C를 빨리 계산하는 방법
#- 1단계: 이진수를 이용하여 B를 2의 거듭제곱으로 분해
#- 2단계: 2 ≤ B 인 거듭제곱의 mod C 를 계산
#- 3단계: 계산된 mod C 값을 결합하기 위한 모듈러 곱셈 성질 이용

# import sys

# a,b,c = map(int,sys.stdin.readline().split())
# bin_b = bin(b)[2:]
# n = len(bin_b)
# l = []
# start = (a**(2**0))%c
# l.append(start)

# for i in range(1,n):
#   l.append((l[i-1]*l[i-1])%c)
# l.reverse()

# result = 1

# for i in range(n):
#   if int(bin_b[i]):
#     result *= l[i]

# print(result%c)




#- <Lucas Theorem>
# import sys
# import math

# n,k = map(int,sys.stdin.readline().split())

# def lucas(n, k, p):
#     """Computes the binomial coefficient C(n, k) modulo p using Lucas Theorem."""
#     if k == 0:
#         return 1
#     ni = n % p
#     ki = k % p
#     return lucas(n // p, k // p, p) * comb(ni, ki, p) % p

# def comb(n, k, p):
#     """Computes the binomial coefficient C(n, k) modulo p using Fermat's Little Theorem."""
#     if k > n:
#         return 0
#     if k == 0 or k == n:
#         return 1
#     fact_n = fact_mod(n, p)
#     fact_k = fact_mod(k, p)
#     fact_nk = fact_mod(n - k, p)
#     return fact_n * pow(fact_k * fact_nk % p, p - 2, p) % p

# def fact_mod(n, p):
#     """Computes n! modulo p using Wilson's Theorem."""
#     if n == 0:
#         return 1
#     fact = 1
#     for i in range(1, p):
#         fact = (fact * i) % p
#         if i == n % p:
#             break
#     return fact * fact_mod(n // p, p) % p if n >= p else fact

# p = 1000000007
# ans = lucas(n, k, p)
# print(ans) # prints 538992043




# import sys
# n = int(sys.stdin.readline())

# for _ in range(n//4):
#   print('long',end=' ')

# print('int')




#- BAEKJOON 2740. <Matrix Multiplication>
# N,M = map(int,input().split())
# A = [list(map(int,input().split()))  for _ in range(N)]

# M,K = map(int,input().split())
# B = [list(map(int,input().split()))  for _ in range(M)]

# result = [[0 for _ in range(K)] for _ in range(N)]

# for n in range(N):
#     for k in range(K):
#         for m in range(M):
#             result[n][k] += A[n][m] * B[m][k]

# for row in result:
#     print(*row)



#- BAEKJOON 10830. <Matrix Exponentiation>
# def multiply(A, B):
#     size = len(A)
#     new_matrix = [[0]*size for _ in range(size)]
    
#     for i in range(size):
#         for j in range(size):
#             for k in range(size):
#                 new_matrix[i][j] += A[i][k] * B[k][j]
#                 new_matrix[i][j] %= 1000
#     return new_matrix

# def power(A, B):
#     if B == 1: 
#         return A
#     elif B % 2: 
#         return multiply(power(A, B-1), A)
#     else:
#         result = power(A, B//2)
#         return multiply(result, result)

# N, B = map(int, input().split())
# A = [list(map(int, input().split())) for _ in range(N)]
# result = power(A, B)

# for row in result:
#     for num in row:
#         print(num % 1000, end=' ')
#     print()





#- BAEKJOON 11444. <Fibonacci 6>
# MOD = 1000000007

# def multiply(F, M): 
#     x = F[0][0] * M[0][0] + F[0][1] * M[1][0]
#     y = F[0][0] * M[0][1] + F[0][1] * M[1][1]
#     z = F[1][0] * M[0][0] + F[1][1] * M[1][0]
#     w = F[1][0] * M[0][1] + F[1][1] * M[1][1]
  
#     F[0][0] = x % MOD
#     F[0][1] = y % MOD
#     F[1][0] = z % MOD
#     F[1][1] = w % MOD

# def power(F, n): 
#     if n == 0 or n == 1:
#         return
#     M = [[1, 1], [1, 0]]
  
#     power(F, n // 2)
#     multiply(F, F)
  
#     if n % 2 != 0:
#         multiply(F, M)

# def fibonacci(n): 
#     F = [[1, 1], [1, 0]]
#     if n == 0:
#         return 0
#     power(F, n - 1)
  
#     return F[0][0]

# n = int(input())
# print(fibonacci(n))




#- BAEKJOON 6549. <Largest Rectangle in a Histogram> ??????
import sys 

def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    index = 0

    # index가 height리스트 길이가 될 때 까지 진행.
    while index < len(heights):
        # stack이 비어있거나 오른쪽 높이가 더 높을 때.
        if not stack or heights[index] >= heights[stack[-1]]:
            stack.append(index)
            index += 1
        # 오른쪽 높이가 더 낮을 때.
        else:
            top_of_stack = stack.pop()
            # stack이 비어있다는 건 가장 왼쪽 것이 제일 높았다는 것이다.
            area = (heights[top_of_stack] *
                    ((index - stack[-1] - 1) if stack else index))
            max_area = max(max_area, area)

    while stack:
        top_of_stack = stack.pop()
        area = (heights[top_of_stack] *
                ((index - stack[-1] - 1) if stack else index))
        max_area = max(max_area, area)

    return max_area


while True:
    L = list(map(int,sys.stdin.readline().split()))
    if len(L)==1 and L[0]==0:
        break
    result = largest_rectangle_area(L)
    print(result)