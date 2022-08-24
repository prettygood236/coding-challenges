# 하나씩 나눠보며 구하기
# import sys

# n = int(sys.stdin.readline())
# l = list(map(int,sys.stdin.readline().split()))

# r = 0
# for i in l:
#   if i == 1 :
#     continue
#   if i == 2 :
#     r += 1
#     continue

#   d = 1 
#   while True:
#     d += 1
#     if i % d == 0 and i != d:
#       break
#     elif i == d:
#       r += 1
#       break
  
# print(r)
  


# Sieve of Eratosthenes
def prime_list(n):
  sieve = [True]*n

  m = int(n ** 0.5)
  for i in range(2, m+1):
    if sieve[i] == True:
      for j in range(i+i,n,i):
        sieve[j] = False

  return [i for i in range(2,n) if sieve[i] == True]

print(prime_list(62)) # 62보다 작은 자연수 중 소수의 리스트 출력.



# M <= 요 사이 소수 구하기 <= N
import sys

def prime_list(n):
  sieve = [True]*n

  m = int(n ** 0.5)
  for i in range(2,m+1):
    if sieve[i] == True:
      for j in range(i+i,n,i):
        sieve[j] = False
  
  return [i for i in range(2,n) if sieve[i] == True]
       
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

Ml = prime_list(M)
Nl = prime_list(N+1)

complement = list(set(Nl)-set(Ml))

if len(complement) == 0:
  print(-1)
else:
  print(sum(complement))
  print(complement[0])



# 소인수 분해

def prime_list(n):
  
  m = int(n ** 0.5)
  sieve = [True]*(m+1)

  mm = int(m ** 0.5)
  for i in range(2,mm+1):
    if sieve[i] == True:
      for j in range(i+i,m,i):
        sieve[j] = False

  return [i for i in range(2,m) if sieve[i] == True] 
  