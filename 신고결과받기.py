# 2022 KAKAO BLIND RECRUITMENT

def solution(id_list, report, k):
    report = set(report) # 한 유저가 같은 유저를 여러 번 신고한 경우는 신고 횟수 1회로 처리 => 중복제거
    answer = {x:0 for x in id_list} # 메일 보낼 횟수
    
    reports = {x:0 for x in id_list} # 신고 당한 횟수 
    for x in report :
        reports[x.split()[1]]+=1
        
    for x in report : # 신고당한 횟수가 k 보다 크면 신고한 사람 메일 보낼 횟수 1 추가
        if reports[x.split()[1]] >= k :
            answer[x.split()[0]] +=1
        
    return list(answer.values())