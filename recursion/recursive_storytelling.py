# ---
# title: Recursive Storytelling
# tags: [CodingChallenges, Python, Recursion]
# created: '2022-09-08'
# ---

# ## Problem Description

# Write a function that generates a recursive story. The story starts with a question about recursion and each time it is answered by telling another recursive story.

# ## Solution

# This problem can be solved using recursion. The idea is to print the starting part of the story and then recursively call the function to generate remaining part of the story until we reach base case where we print ending part of the story.


# ```python

def recursive_case_one(n,m):
  if n == 0:
    print("____"*m,'"재귀함수가 뭔가요?"',sep="")
    print("____"*m,'"재귀함수는 자기 자신을 호출하는 함수라네"',sep="")
    print("____"*m,'라고 답변하였지.',sep="")
    return
  
  print("____"*m,'"재귀함수가 뭔가요?"',sep="")
  print("____"*m,'"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.',sep="")
  print("____"*m,"마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.",sep="")
  print("____"*m,'그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."',sep="")

  recursive_case_one(n-1,m+1)
  
  print("____"*m,'라고 답변하였지.',sep="")

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
m = 0

n = int(input())
recursive_case_one(n,0)
