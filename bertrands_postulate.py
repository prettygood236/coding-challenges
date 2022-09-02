import sys

def prime_list(n):
  sieve = [True] * n

  m = int(n**0.5)
  for i in range(2,m+1):
    if sieve[i] == True:
      for j in range (i+i,n,i):
        sieve[j] = False
  
  return [i for i in range(2,n) if sieve[i] == True]


result = []
while True: 
  N = int(sys.stdin.readline())
  Ms = set(prime_list((N*2)+1))
  Ns = set(prime_list(N+1))
  l = list(Ms - Ns)

  # print(Ms)
  # print(Ns)
  # print(l)
  # print(len(l))

  if N != 0:
    result.append(len(l))

  if N == 0:
    print(*result,sep='\n')
    break


