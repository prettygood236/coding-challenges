def solution(k, d):
    list = []
    for i in range(d+1):
        for j in range(d+1):
            if (i**2)+(j**2) <= d**2:
                list.append((i,j))
    answer = 0
    return list,len(list)


print(solution(1,6))
print(solution(1,7))
print(solution(1,8))
print(solution(1,9))