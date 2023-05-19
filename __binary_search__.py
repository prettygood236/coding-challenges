
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
N,M = map(int,input().split())
L = list(map(int,input().split()))

start_num = min(L)
end_num = max(L)

while True:
    mid_num = (start_num + end_num) // 2

    required_wood = 0
    for i in L:
        if i > mid_num:
            required_wood += i - mid_num

    if required_wood == M:
        print(mid_num)
        break
    
    if required_wood > M:
        start_num = mid_num + 1
    else:
        end_num = mid_num - 1



