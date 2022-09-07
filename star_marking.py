def star_marking(N):
  if N == 1:
    return ['*']
  Star = star_marking(N//3)
  L = []

  for i in Star:
    L.append(i*3)
  for i in Star:
    L.append(i+' '*(N//3)+i)
  for i in Star:
    L.append(i*3)
  return L

import sys
N = int(sys.stdin.readline().strip())
print('\n'.join(star_marking(N)))
