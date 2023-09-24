# ---
# title: 2022 KAKAO BLIND RECRUITMENT - Receiving Report Results
# tags: [Hashmap, String Processing]
# created: '2022-11-06'
# ---

# # 2022 KAKAO BLIND RECRUITMENT - Receiving Report Results

# ## Problem Description


# ## Solution

# ```python
def solution(id_list, report, k):
    report = set(report) # If a user reports the same user multiple times => treat as one report. Remove duplicates.
    answer = {x:0 for x in id_list} # Number of mails to be sent
    
    reports = {x:0 for x in id_list} # Number of times reported 
    for x in report :
        reports[x.split()[1]]+=1
        
    for x in report : # If the number of times reported is greater than k then add 1 to the number of mails to be sent by the reporter
        if reports[x.split()[1]] >= k :
            answer[x.split()[0]] +=1
        
    return list(answer.values())
