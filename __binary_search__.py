
#. BAEKJOON 1920. <Find the number>
def binary_search(L,target,start,end):
    if start > end:
        return False
    mid = (start + end) // 2
    if target == L[mid]:
        return mid + 1
    elif target < L[mid]:
        return binary_search(L,target,start,mid-1)
    else:
        return binary_search(L,target,mid+1,end)

N = int(input())
L = list(map(int,input().split()))
L.sort()
M = int(input())
target_list = list(map(int,input().split()))


for i in range(M):
    target = target_list[i]
    answer = binary_search(L,target,0,len(L)-1)
    if answer :
        print(1)
    elif not answer :
        print(0)




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