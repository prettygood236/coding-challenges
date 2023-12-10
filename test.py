def solution(n, computers):
    def dfs(i):
        # breakpoint()
        visited[i] = True
        for j in range(n):
            if visited[j] != True and computers[i][j] == 1:
                dfs(j)
        return
    
    visited = [False] * n
    answer = 0
    for i in range(n):
        if visited[i] != True:
            dfs(i)
            answer += 1 
    return answer


n = 3	
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	
print(solution(n,computers)) # 2
n = 3	
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]	
print(solution(n,computers)) # 1