
# # 사람들은 다음 두 가지 규칙만 따르면 된다.
# # 1. 무조건 빨간모자와 파란모자 사이에 선다.  
# # 2. 빨간모자 혹은 파란모자만 존재할 경우 아무데나 선다.

# import queue from collections  
# def solution(hats):
#     l = []
#     l.extend(hats[:2])

#     for hat in hats[2:]:
#         if l[-1] != l[-2]:






#     breakpoint()

#     return

# hats = ['r','r','b','r','b','b','r','b']
# print(solution(people))



class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
