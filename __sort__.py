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

# import sys

# N = int(sys.stdin.readline())

# count = [0] * ( 10000 + 1)

# for _ in range(N):
#   M = int(sys.stdin.readline())
#   count[M] += 1

# for i in range(len(count)):
#   for j in range(count[i]):
#     print(i)



# import sys

# N,k = map(int,sys.stdin.readline().split())
# L = list(map(int,sys.stdin.readline().split()))
# Sorted = []

# count = [0] * (10000 +1)

# for i in L:
#   count[i] += 1

# for i in range(len(count)):
#   for j in range(count[i]):
#     Sorted.append(i)

# print(Sorted[-k])


from collections import Counter

def modefinder(numbers):   #numbers는 리스트나 튜플 형태의 데이터
  c = Counter(numbers)
  mode = c.most_common(2)
  if len(mode) == 2 and mode[0][1] == mode[1][1]:
    return mode[1][0]
  return mode[0][0]

# import sys 

# N = int(sys.stdin.readline())
# L = []

# for _ in range(N):
#   L.append(int(sys.stdin.readline()))

# L.sort()

# print(round(sum(L)/N))
# print(L[len(L)//2])
# print(modefinder(L))
# print(L[-1]-L[0])



# import sys
# N = sys.stdin.readline().strip()
# L = list(map(int,N))

# L.sort(reverse=True)
# print(*L,sep='')




# import sys
# N = int(sys.stdin.readline())
# L = []

# for _ in range(N):
#   L.append(list(map(int,sys.stdin.readline().split())))

# L.sort()

# for i in L:
#   print(*i)



# import sys
# N = int(sys.stdin.readline())
# L = []

# for _ in range(N):
#   L.append(list(map(int,sys.stdin.readline().split())))

# L.sort(key=lambda x:[x[1],x[0]]) 
# # L.sort(key=lambda x:x[1]) #? 이거 왜 안돼??

# for i in L:
#   print(*i)



# import sys 
# N = int(sys.stdin.readline())
# L = []

# for _ in range(N):
#   L.append(sys.stdin.readline().strip())

# New_L = list(set(L))
# New_L.sort()
# Sorted_L = sorted(New_L, key=len)

# for i in Sorted_L:
#   print(i)



# import sys
# N = int(sys.stdin.readline())
# L = []

# for i in range(N):
#   A,B = sys.stdin.readline().split()
#   A = int(A)
#   L.append([A,B,i])

# L.sort(key=lambda x:[x[0],x[2],x[1]])

# for i in L:
#   del i[2]
#   print(*i)



import sys
N = int(sys.stdin.readline())
L = list(map(int,sys.stdin.readline().split()))

R = sorted(list((set(L))))
dic_R = {x : i for i,x in enumerate(R)} #! dict는 key를 이용해 O(1)의 시간복잡도로 value를 찾을 수 있다!.

for i in L :
  # print(R.index(i),end=' ') #! index는 O(N)이 걸리기 때문에 O(N^2)으로 시간복잡도를 초과하게 된다.
  print(dic_R[i], end=' ')  
