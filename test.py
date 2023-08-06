# def solution(participant, completion):
#     # breakpoint()
#     participant.sort()
#     completion.sort()
#     answer = ''
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             answer = participant[i]
#             break
#     if answer == '':
#         answer = participant[-1]
#     return answer

import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return  answer.keys()

print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))   
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))   