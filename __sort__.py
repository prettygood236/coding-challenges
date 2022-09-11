def bubble_sort(array):
  for i in range(len(array)):
    swapped = False
    for j in range(0,len(array)-i-1):
      if array[j] > array[j+1]:
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
        swapped = True
    
    if swapped == False:
      break

  return array


def quick_sort(array):
  if len(array) <= 1:
    return array
  
  pivot = array[0]
  tail = array[1:]

  left_side = [x for x in tail if x <= pivot ]
  right_side = [x for x in tail if x > pivot ]

  return quick_sort(left_side) + [pivot] + quick_sort(right_side)
  

def merge_sort(array):
    if len(array) > 1:
        mid = len(array)//2
        L = array[:mid]
        R = array[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
  
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
            
    return array



# count_sort

import sys

count = [0] * ( 10000 + 1)

N = int(sys.stdin.readline())

for _ in range(N):
  M = int(sys.stdin.readline())
  count[M] += 1

for i in range(len(count)):
  for j in range(count[i]):
    print(i)

