import sys

N = int(sys.stdin.readline())

def prime_list(n):
  sieve = [True] * n

  m = int(n**0.5)
  for i in range(2,m+1):
    if i == True:
      for j in range (i+i,n,i):
        sieve[j] = False
  
  return [i for i in range(2,n) if sieve[i] == True]

l = list(set(prime_list((N*2)+1)) - set(prime_list(N+1)))

print(l)
print(len(l))



