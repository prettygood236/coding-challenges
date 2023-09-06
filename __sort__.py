def solution(strings, n):
  strings = ["abce", "abcd", "cdx"]	
  n = 2
  answer = []
  answer = sorted(strings, key = lambda x: (x[n],x))
  return answer


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



  
import math

def merge_sort(array,result):
  if len(array) > 1:
    # mid = len(array)//2
    mid = math.ceil(len(array)/2)
    # print(mid)
    L = array[:mid]
    R = array[mid:]
    # print('L',L)
    # print('R',R)
    # print('call merge_sort L')
    merge_sort(L,result)
    # print('call merge_sort R')
    merge_sort(R,result)
    i = j = k = 0

    while i < len(L) and j < len(R):
      if L[i] < R[j]:
        array[k] = L[i]
        # print('array',array)
        i += 1
        # print('i',i)

      else:
        array[k] = R[j]
        # print('array',array)
        j += 1
        # print('j',j)

      k += 1
      # print('k',k)

    while i < len(L):
      array[k] = L[i]
      # print('array',array)
      i += 1
      k += 1
      # print('i',i)
      # print('k',k)
  
    while j < len(R):
      array[k] = R[j]
      j += 1
      k += 1
      # print('j',j)
      # print('k',k)

  if len(array) > 1:
    result += array
  return array,result
  

# import sys
# N,K = map(int,sys.stdin.readline().split())
# array = list(map(int,sys.stdin.readline().split()))
# result = []
# array,result = merge_sort(array,result)

# if K <= len(result):
#   print(result[K-1])
# else:
#   print(-1)





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



# import sys
# N = int(sys.stdin.readline())
# L = list(map(int,sys.stdin.readline().split()))

# R = sorted(list((set(L))))
# dic_R = {x : i for i,x in enumerate(R)} #! dict는 key를 이용해 O(1)의 시간복잡도로 value를 찾을 수 있다!.

# for i in L :
#   # print(R.index(i),end=' ') #! index는 O(N)이 걸리기 때문에 O(N^2)으로 시간복잡도를 초과하게 된다.
#   print(dic_R[i], end=' ')  





# L = [int(input()) for _ in range(5)]

# L.sort()

# print(sum(L)//5)
# print(L[2])



# #. BAEKJOON 20920. <Memorizing English words are painful>
# def sort_key(word, freq):
#   return (-freq[word], -len(word), word)

# N, M = map(int, input().split())

# words = []
# freq = {}

# for _ in range(N):
#   word = input().strip()
#   if len(word) >= M:
#     if word not in freq:
#       freq[word] = 0
#       words.append(word)
#     freq[word] += 1

# #- I see that it's possible to pass the time complexity requirement just by creating a custom sort function and using the built-in sort method.
# words.sort(key=lambda word: sort_key(word, freq))

# for word in words:
#   print(word)




#- <K-th number>
# 문제 설명
# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

# 예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

# array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
# 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
# 2에서 나온 배열의 3번째 숫자는 5입니다.
# 배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# array의 길이는 1 이상 100 이하입니다.
# array의 각 원소는 1 이상 100 이하입니다.
# commands의 길이는 1 이상 50 이하입니다.
# commands의 각 원소는 길이가 3입니다.
# 입출력 예
# array	commands	return
# [1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3]
# 입출력 예 설명
# [1, 5, 2, 6, 3, 7, 4]를 2번째부터 5번째까지 자른 후 정렬합니다. [2, 3, 5, 6]의 세 번째 숫자는 5입니다.
# [1, 5, 2, 6, 3, 7, 4]를 4번째부터 4번째까지 자른 후 정렬합니다. [6]의 첫 번째 숫자는 6입니다.
# [1, 5, 2, 6, 3, 7, 4]를 1번째부터 7번째까지 자릅니다. [1, 2, 3, 4, 5, 6, 7]의 세 번째 숫자는 3입니다.

# def solution(array, commands):
#     # answer = []
#     # for x in commands:
#     #     i,j,k = x
#     #     answer.append(sorted(array[i-1:j])[k-1])
#     # return answer
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

# array	= [1, 5, 2, 6, 3, 7, 4]	
# commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	# [5, 6, 3]
# print(solution(array, commands))



#- <The biggest number>
# 문제 설명
# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

# def solution(numbers):
#     answer = ''.join(sorted(list(map(str,numbers)),key=lambda x: x*3,reverse=True))
#     return  '0' if answer[0] == '0'  else answer

import functools

def comparator(a, b):
  t1 = a + b
  t2 = b + a
  return (int(t1) > int(t2)) - (int(t1) < int(t2)) 

def solution(numbers):
  n = [str(x) for x in numbers]
  #. By using cmp_to_key, we can use a function that compares two argument as a key!
  n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)
  answer = str(int(''.join(n)))
  return answer


numbers = [3, 998, 9998, 34, 5, 9]
print(solution(numbers))  # "999898995343"
numbers = [0, 0, 0]
print(solution(numbers))  # "0"
numbers	= [6, 10, 2]	
print(solution(numbers)) # "6210"
numbers	= [3, 30, 34, 5, 9]	
print(solution(numbers)) # "9534330"


