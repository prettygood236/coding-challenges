# ---
# title: Tower of Hanoi
# tags: [CodingChallenges, Python, Recursion]
# created: '2022-09-08'
# ---

# ## Problem Description

# The Tower of Hanoi is a mathematical game or puzzle. It consists of three rods and a number of disks of different sizes, which can slide onto any rod. The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top, thus making a conical shape.

# The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:

# 1. Only one disk can be moved at a time.
# 2. Each move consists only of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
# 3. No disk may be placed on top of a smaller disk.

# Write a function that calculates all moves required to solve this problem given `N` number of disks.

# ## Solution

# This problem is usually solved using recursion. The idea is that we first move `N-1` disks from source peg to auxiliary peg using destination peg. Then we move remaining 1 disk from source peg to destination peg. Finally we again move `N-1` disks from auxiliary peg to destination peg using source peg.

# ```python
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
