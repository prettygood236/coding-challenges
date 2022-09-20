import sys

while True:
  L = list(map(int,sys.stdin.readline().split()))
  if L[0] == 0 and L[1] == 0:
    break
  if max(L) % min(L) == 0:
    if L[0] > L[1]:
      print('multiple')
    if L[1] > L[0]:
      print('factor')
  else:
    print('neither')