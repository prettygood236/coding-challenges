def fac(N):
  if N == 0:
    return 1
  
  f = 1
  result = 1
  while True:
    if f == N:
      return result
    f += 1
    result *= f

N = int(input())
print(fac(N))