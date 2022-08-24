
# 소인수 분해

def prime_list(n):
  sieve = [True]*(n)

  m = int(n ** 0.5)

  for i in range(2,m+1):
    if sieve[i] == True:
      for j in range(i+i,n,i):
        sieve[j] = False

  return [i for i in range(2,n) if sieve[i] == True] 

import sys

N = int(sys.stdin.readline())

if N != 1:
  l = prime_list(N+1)
  while True:
    if N in l: # 탈출 조건
      print(N)
      break
    for i in l:
      if N % i == 0:
        print(i)
        N //= i
        break