# N으로 표현
# 문제 설명
# 아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

# 12 = 5 + 5 + (5 / 5) + (5 / 5)
# 12 = 55 / 5 + 5 / 5
# 12 = (55 + 5) / 5

# 5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
# 이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

# 제한사항
# N은 1 이상 9 이하입니다.
# number는 1 이상 32,000 이하입니다.
# 수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
# 최솟값이 8보다 크면 -1을 return 합니다.

# 예제 #2
# 11 = 22 / 2와 같이 2를 3번만 사용하여 표현할 수 있습니다.


def solution(N, number):
    # N을 1번만 쓰는 경우
    if N == number:
        return 1
    
    # N을 2번 이상 쓰는 경우
    # 바텀업으로 올라가보자
    dp = {1:{N}}
    c = 2
    while True:
        if c > 8:
            return -1
        s = set([int(str(N)*c)])
        for i in range(1, c//2+1):
            for x in dp[i]:
                for y in dp[c-i]:
                    s.update((x+y,x-y,y-x,x*y))
                    s.update((x//y if y!=0 else 0,))
                    s.update((y//x if x!=0 else 0,))
        if number in s:
            return c
        dp[c] = s
        c += 1

N = 5 
number = 24
print(solution(N, number)) # 4
N = 2
number = 11
print(solution(N, number)) # 3

