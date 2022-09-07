# 재귀 -> 일반항 찾기. 귀납적 방법으로 찾아보자.
# 일반항 N은 2와 3이 서로 바뀐 N-1 + 13 + 1과 2가 서로 바뀐 N-1

def tower_of_hanoi(N):
  if N == 1:
    return ['1 3']
  Hanoi = tower_of_hanoi(N-1)
  L = []

  for i in Hanoi:
    temp = i.replace('2','*').replace('3','2').replace('*','3')
    L.append(temp)
  L.append('1 3')
  for i in Hanoi:
    temp = i.replace('1','*').replace('2','1').replace('*','2')
    L.append(temp)

  return L

import sys
N = int(sys.stdin.readline().strip())
print(len(tower_of_hanoi(N)), *tower_of_hanoi(N), sep='\n')
  

  # if N == 2:
  #   return [12,13,23]
  # if N == 3 :
  #   return [13, 12, 32, 13, 21, 23, 13]  
  # if N == 4 :
  #   return [12, 13, 23, 12, 31, 32, 12, 13, 23, 21, 31, 23, 12, 13, 23]  
