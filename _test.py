# def solution(id_list, report, k):
#     answer = []
    
#     for 
#     return answer



# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]	

my_set = set(report)

# print(my_set)

id_list = ["muzi", "frodo", "apeach", "neo"]

answer = {x:0 for x in id_list} # 메일 보낼 횟수
    
reports = {x:0 for x in id_list} # 신고 당한 횟수 

print(answer)
print(reports)

# for i in report:
#   a,b=i.split()
#   print(a)


# 뒤에 오는 이름이 2번이상이면 앞에 이름에게 1적립. 
# 같은 이름으로 같은 이름 신고는 1회까지만 처리. => 중복 제거로 해결!