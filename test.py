# 도둑질
# 문제 설명
# 도둑이 어느 마을을 털 계획을 하고 있습니다. 이 마을의 모든 집들은 아래 그림과 같이 동그랗게 배치되어 있습니다.

# image.png

# 각 집들은 서로 인접한 집들과 방범장치가 연결되어 있기 때문에 인접한 두 집을 털면 경보가 울립니다.

# 각 집에 있는 돈이 담긴 배열 money가 주어질 때, 도둑이 훔칠 수 있는 돈의 최댓값을 return 하도록 solution 함수를 작성하세요.

# 제한사항
# 이 마을에 있는 집은 3개 이상 1,000,000개 이하입니다.
# money 배열의 각 원소는 0 이상 1,000 이하인 정수입니다.


def solution(money):
    dp_first = [0]*len(money) # 첫 번째 집부터 시작
    dp_first[0]=money[0]
    dp_first[1]=max(money[0],money[1])
    
    for i in range(2,len(money)-1): # 마지막집은 방문하지 않음
        dp_first[i]=max(dp_first[i-2]+money[i],dp_first[i-1])
        
    dp_second=[0]*len(money) # 두 번째지장부터 시작
    dp_second[0]= 0 
    dp_second[1]=money[1]
    
    for i in range(2,len(money)): 
        dp_second[i]=max(dp_second[i-2]+money[i],dp_second[i-1])

        
    return max(max(dp_first),max(dp_second))  


money	= [1, 2, 3, 1] #4