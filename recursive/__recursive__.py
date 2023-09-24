
# def factorial(N):
#   if N <= 1:
#     return 1
#   else:
#     return N * factorial(N-1)


# def fibonacci(N):
#   if N == 0:
#     return 0
#   if N == 1:
#     return 1
#   else :
#     return fibonacci(N-1) + fibonacci(N-2)

# print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
# m = 0
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

# n = int(input())
# recursive_case_one(n,m)


# def isPalidrome(str):
#   call = 0

#   def recursion(str,l,r,call):
#     call += 1
#     if l >= r :
#       print(1,call)
#       return 1
#     elif str[l] != str[r]:
#       print(0,call)
#       return 0
#     else :
#       return recursion(str,l+1,r-1,call)
  
#   return recursion(str,0,len(str)-1,call)

# import sys
# N = int(sys.stdin.readline())
# for _ in range(N):
#   str = sys.stdin.readline().strip()
#   isPalidrome(str)



#- BAEKJOON 4779. <Cantoring Along>
def cantor(str,N):
  if N == 0:
    return '-'
  else:
    return cantor(str,N-1)+' '*(3**(N-1))+cantor(str,N-1)

while True:
  try:
    N = int(input())
    print(cantor('',N))
  except EOFError:
    break