from collections import deque

def solution(a):
  dq = deque(a)
  for i in range(len(dq)-1):
    dq.remove(min(dq[i],dq[i+1]))
                 
  return

a = [9,-1,-5]	# 3
# a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]	# 6

solution(a)