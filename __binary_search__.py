
#! Binary search can be used in problems where the dataset is sorted and you need to find a specific value or an optimal solution within a continuous range.
#! The time complexity is O(logN)

#. BAEKJOON 1920. <Find the number>
# def binary_search(L,target,start,end):
#     if start > end:
#         return False
#     mid = (start + end) // 2
#     if target == L[mid]:
#         return mid + 1
#     elif target < L[mid]:
#         return binary_search(L,target,start,mid-1)
#     else:
#         return binary_search(L,target,mid+1,end)

# N = int(input())
# L = list(map(int,input().split()))
# L.sort()
# M = int(input())
# target_list = list(map(int,input().split()))

# for i in range(M):
#     target = target_list[i]
#     answer = binary_search(L,target,0,len(L)-1)
#     if answer :
#         print(1)
#     elif not answer :
#         print(0)




#. BAEKJOON 10816. <Number Card 2>
# import sys
# from collections import Counter
# N = int(sys.stdin.readline())
# L = map(int,sys.stdin.readline().split())
# R = []

# cnt = Counter(L)
# M = int(sys.stdin.readline())

# R = list(map(int,sys.stdin.readline().split()))
  
# for i in R:
#   print(cnt[i])





#. BAEKJOON 1654. <Cutting off the online connection>
# K,N = map(int,input().split())
# L = list(int(input()) for _ in range(K))

# start_num = 1
# end_num = max(L)

# while start_num <= end_num:
#     mid_num = (start_num + end_num) // 2

#     lines = 0
#     for i in L:
#         lines += i // mid_num

#     if lines >= N:
#         start_num = mid_num + 1
#     else:
#         end_num = mid_num - 1

# print(end_num)




#. BAEKJOON 2805. <EKO>
# import sys
# N,M = map(int,sys.stdin.readline().split())
# L = list(map(int,sys.stdin.readline().split()))
# L.sort(reverse=True)

# start_num = 0
# end_num = L[0]

# while start_num <= end_num:
#     mid_num = (start_num + end_num) // 2

#     required_wood = 0
#     for i in L:
#         if i <= mid_num:
#             break
#         required_wood += (i - mid_num)

#     if required_wood >= M:
#         start_num = mid_num + 1
#     else:
#         end_num = mid_num - 1

# print(end_num)





#. BAEKJOON 2110. <Aggressive cows>
# def check_distance(stalls,min_distance,cows):
#     cows_count = 1
#     last_stall = stalls[0]

#     for stall in stalls[1:]:
#         if stall - last_stall >= min_distance:
#             cows_count += 1
#             last_stall = stall
#             if cows_count == cows:
#                 return True
#     return False

# def largest_minimum_distance(N,C,stalls):
#     # breakpoint()
#     stalls.sort()
#     #. 범위를 설정하고 이분탐색한다!! 
#     #. largest_minimum_distance의 가능한 범위는 1 ~ stalls[-1] - stalls[0]
#     left = 1
#     right  = stalls[-1] - stalls[0]
#     ans = 0

#     while left <= right:
#         mid = (left + right) // 2
          #. mid가 정답인지 판별할 식 작성!
#         if check_distance(stalls,mid,C):
#             ans = mid
#             left = mid + 1
#         else:
#             right = mid - 1
    
#     return ans

# N,C = map(int,input().split())
# # N : stall의 개수 C: 소의 마리수
# stalls = [int(input()) for _ in range(N)]
# # stalls : 축사 위치의 집합
# print(largest_minimum_distance(N,C,stalls))




#. BAEKJOON 1300. <K-th Number>
# N = int(input())  
# k = int(input())  

# # Initialize the binary search range 
# left, right = 1, k  
# while left <= right:
#   mid = (left + right) // 2  
#   # The variable to count the number of elements less than or equal to mid
#   cnt = 0  
#   # Iterate through row indices (i) from 1 to N
#   for i in range(1, N + 1):  
#     # Calculate the number of elements less than or equal to mid in each row, and accumulate it to cnt
#     cnt += min(mid // i, N)  
#   if cnt < k: 
#     left = mid + 1  
#   else:  
#     right = mid - 1  

# print(left)  




#. BAEKJOON 12015. <Longest Increasing Subsequence>
#. Just memorzing it !!!! ㅠ.ㅠ

import sys

def binary_search(L,num):
  left, right = 0, len(L) - 1
  while left <= right:
    mid = (left + right) // 2
    if L[mid] < num:
      left = mid + 1
    else:
      right = mid - 1

  return left
    

def longest_increasing_subsequence(L):
  subsequence = [L[0]]

  for num in L[1:]:
    if subsequence[-1] < num:
      subsequence.append(num)
    else:
      #. In the subsequence list, use binary search to find the rank of a number in terms of size.
      index = binary_search(subsequence,num)
      subsequence[index] = num

  return len(subsequence)
    

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
result = longest_increasing_subsequence(A)

print(result)