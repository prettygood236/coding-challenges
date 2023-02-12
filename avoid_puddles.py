from collections import deque

def solution(m,n,puddles):
    answer = bfs(m,n,puddles)
    return answer

def bfs(m,n,puddles):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 'PUDDLE'
    for i in puddles:
        x,y = i
        dp[y-1][x-1] = 'PUDDLE'
    queue = deque()
    queue.append((1,1,0))
    # right down left up
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    result = 0
    while queue:
        print(queue)
        print(dp)
        x,y,d = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nd = d + 1
            if nx < 1 or nx > m or ny < 1 or ny > n:
                continue
            if dp[ny-1][nx-1] == 'PUDDLE':
                continue
            if dp[ny-1][nx-1] == 0:
                dp[ny-1][nx-1] = nd
            if dp[ny-1][nx-1] < nd:
                continue
            if nx == m and ny == n:
                result = (result%1000000007) + 1
            else:
                queue.append((nx,ny,nd))
    return result

# m = 4
# n = 3 
# puddles	= [[2, 2]]
# 4

# m = 100
# n = 100
# puddles	= [[2, 2],[13,14],[3,52],[6,77],[53,79],[99,99]]

m = 10
n = 10
puddles	= [[2, 2],[6,9],[9,9]]

print(solution(m,n,puddles))