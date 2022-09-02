# 예를들어 10000이면 5000부터 해서 중간에 가까운 소수를 찾고 그 소수를 뺀게 소수인지 확인. 아니면 더 작은 소수로. 계속 반복. 

import sys

def prime_list(n):
  sieve = [True] * n
  
  m = int(n**0.5)
  for i in range(2,m+1):
    if sieve[i] == True:
      for j in range(i+i,n,i):
        sieve[j] = False
  
  return [i for i in range(2,n) if sieve[i] == True]

l = prime_list(10001)

n = int(sys.stdin.readline())

for _ in range(n):
  m = int(sys.stdin.readline())
  o = int(m/2)
  if o in l:
    print(o,o)
    continue 
  while True:
    o -= 1
    if o in l and m-o in l:
      print(o, m-o)
      break
