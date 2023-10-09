# 사칙연산
# 문제 설명
# 사칙연산에서 더하기(+)는 결합법칙이 성립하지만, 빼기(-)는 결합법칙이 성립하지 않습니다.
# 예를 들어 식 1 - 5 - 3은 연산 순서에 따라 다음과 같이 다른 결과를 가집니다.

# ((1 - 5) - 3) = -7
# (1 - (5 - 3)) = -1
# 위 예시와 같이 뺄셈은 연산 순서에 따라 그 결과가 바뀔 수 있습니다.
# 또 다른 예로 식 1 - 3 + 5 - 8은 연산 순서에 따라 다음과 같이 5가지 결과가 나옵니다.

# (((1 - 3) + 5) - 8) = -5
# ((1 - (3 + 5)) - 8) = -15
# (1 - ((3 + 5) - 8)) = 1
# (1 - (3 + (5 - 8))) = 1
# ((1 - 3) + (5 - 8)) = -5
# 위와 같이 서로 다른 연산 순서의 계산 결과는 [-15, -5, -5, 1, 1]이 되며, 이중 최댓값은 1입니다.
# 문자열 형태의 숫자와, 더하기 기호("+"), 뺄셈 기호("-")가 들어있는 배열 arr가 매개변수로 주어질 때, 서로 다른 연산순서의 계산 결과 중 최댓값을 return 하도록 solution 함수를 완성해 주세요.

# 제한 사항
# arr는 두 연산자 "+", "-" 와 숫자가 들어있는 배열이며, 길이는 3 이상 201 이하 입니다.
# arr의 길이는 항상 홀수입니다.
# arr에 들어있는 숫자의 개수는 2개 이상 101개 이하이며, 연산자의 개수는 (숫자의 개수) -1 입니다.
# 숫자는 1 이상 1,000 이하의 자연수가 문자열 형태로 들어있습니다.. (ex : "456")
# 배열의 첫 번째 원소와 마지막 원소는 반드시 숫자이며, 숫자와 연산자가 항상 번갈아가며 들어있습니다.

# def solution(arr):
#     num_list = list(map(int,arr[::2]))
#     op_list = arr[1::2] + ['']
#     n = len(num_list)
#     dp = [[0]*n for _ in range(n)]

#     for i in range(n):
#         dp[i][i] = num_list[i]

#     for i in range(len(num_list)-1, -1, -1):
#         for j in range(i+1, len(num_list)):
#             if op_list[j-1] == '+':
#                 dp[i][j] = dp[i][j-1] + num_list[j]
#             else:
#                 dp[i][j] = max(dp[k+1][j]-dp[i][k]+(num_list[i]*2) for k in range(i,j))
                
#     breakpoint()
#     return dp[0][-1]


# arr = ["1", "-", "3", "+", "5", "-", "8"]	
# print(solution(arr)) # 1
# ["5", "-", "3", "+", "1", "+", "2", "-", "4"]	
# print(solution(arr)) # 3











# 문제 설명
# 계속되는 폭우로 일부 지역이 물에 잠겼습니다. 물에 잠기지 않은 지역을 통해 학교를 가려고 합니다. 집에서 학교까지 가는 길은 m x n 크기의 격자모양으로 나타낼 수 있습니다.

# 아래 그림은 m = 4, n = 3 인 경우입니다.

# image0.png

# 가장 왼쪽 위, 즉 집이 있는 곳의 좌표는 (1, 1)로 나타내고 가장 오른쪽 아래, 즉 학교가 있는 곳의 좌표는 (m, n)으로 나타냅니다.

# 격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다. 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 격자의 크기 m, n은 1 이상 100 이하인 자연수입니다.
# m과 n이 모두 1인 경우는 입력으로 주어지지 않습니다.
# 물에 잠긴 지역은 0개 이상 10개 이하입니다.
# 집과 학교가 물에 잠긴 경우는 입력으로 주어지지 않습니다.


def solution(m, n, puddles):
    dp = [[0]*m for _ in range(n)]
    mod = 1000000007

    for i,j in puddles:
        dp[i-1][j-1] = 'puddle'

    for i in range(1,n):
        if dp[i][0] == 'puddle':
            break
        dp[i][0] = 1

    for j in range(1,m):
        if dp[0][j] == 'puddle':
            break
        dp[0][j] = 1

    for i in range(1,n):
        for j in range(1,m):
            if dp[i][j] == 'puddle' or (dp[i-1][j] == 'puddle' and dp[i][j-1] == 'puddle'):
                continue
            elif dp[i][j-1] == 'puddle':
                dp[i][j] = dp[i-1][j] % mod
            elif dp[i-1][j] == 'puddle':
                dp[i][j] = dp[i][j-1] % mod
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % mod
    
    return dp[-1][-1]

m = 4; n = 3; puddles= [[1,3],[2, 2]]
print(solution(m, n, puddles)) #4