import sys

def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left

def longest_increasing_subsequence(arr):
    lis = [arr[0]]
    
    breakpoint()

    for num in arr[1:]:
        if lis[-1] < num:
            lis.append(num)
        else:
            index = binary_search(lis, num)
            lis[index] = num
            
    return len(lis)

input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))


result = longest_increasing_subsequence(arr)
print(result)

#7
#10 20 5 30 15 35 35 20 30       