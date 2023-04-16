def solution(A, B):
    A.sort()
    B.sort()

    points = 0
    b_index = 0

    for x in A:
        while b_index < len(B) and B[b_index] <= x:
            b_index += 1
        if b_index < len(B):
            points += 1
            b_index += 1

    return points


A = [5,1,3,7]	
B = [2,2,6,8]	
# 3

A = [2,2,2,2]	
B = [1,1,1,1]	
# 0

print(solution(A,B))