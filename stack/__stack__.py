
#- <Stack>
# import sys
# n = int(sys.stdin.readline())
# l = []
# for _ in range(n):
#   str = sys.stdin.readline().split()
#   if str[0] == 'push':
#     l.append(int(str[1]))
#   if str[0] == 'pop':
#     if l:
#       print(l.pop())
#     else :
#       print(-1)
#   if str[0] == 'size':
#     print(len(l))
#   if str[0] == 'empty':
#     if l:
#       print(0)
#     else :
#       print(1)
#   if str[0] == 'top':
#     if l:
#       print(l[-1])
#     else :
#       print(-1)




#- <Zero>
# import sys
# n = int(sys.stdin.readline())
# l = []
# for _ in range(n):
#   t = int(sys.stdin.readline())
#   if t == 0:
#     l.pop()
#     continue
#   l.append(t)

# print(sum(l))




#- <VPS 1(Valid Parenthesis String)>
# import sys
# n = int(sys.stdin.readline())
# for _ in range(n):
#   l = list(sys.stdin.readline().strip())
#   count = 0
#   for i in range(len(l)):
#     t = l.pop()
#     if t == ')':
#       count += 1
#     if t == '(':
#       count -= 1
#     if count < 0:
#       break
#   if count == 0:
#     print('YES')
#     continue
#   print('NO')
  


#- <VPS 2>
# import sys
# while True:
#   s = sys.stdin.readline().rstrip()
  
#   if s == '.':
#     break

#   flag = True
#   l = []
#   for i in s:
#     if i == '(' or i == '[':
#       l.append(i)
#       continue
    
#     if i == ')' or i == ']':
#       if not l:
#         flag = False
#         break

#       else:
#         a = l.pop()
#         if (i == ')' and a == '(') or (i == ']' and a =='['):
#           continue
#         else :
#           flag = False
#           break
  
#   if not l and flag:
#     print('yes')
#     continue
#   print('no')




#- <Stack Sequence>
# import sys
# n = int(sys.stdin.readline())
# l = [int(sys.stdin.readline()) for _ in range(n)]

# count = 0
# stack = []
# result = []
# flag = True
# for num in l:
#   while True:
#     if count >= num:
#       break
#     count += 1
#     result.append('+')
#     stack.append(count)
#   if stack[-1] == num:
#     result.append('-')
#     stack.pop()
#   else :
#     flag = False
#     break

# if flag == False:
#   print('NO')
# else :
#   for i in result:
#     print(i)



#- <같은 숫자는 싫어>
# 문제 설명
# 배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다. 예를 들면,

# arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
# arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
# 배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 배열 arr의 크기 : 1,000,000 이하의 자연수
# 배열 arr의 원소의 크기 : 0보다 크거나 같고 9보다 작거나 같은 정수
# 입출력 예
# arr	answer
# [1,1,3,3,0,1,1]	[1,3,0,1]
# [4,4,4,3,3]	[4,3]
# 입출력 예 설명
# 입출력 예 #1,2
# 문제의 예시와 같습니다.


# def solution(arr):
#     answer = [arr[0]]
#     for i in range(1,len(arr)):
#       if arr[i] == arr[i-1]:
#          continue
#       else:
#          answer.append(arr[i])
#     return answer

# def solution(arr):
#     answer = []
#     for x in arr:
#         #* When using list slicing, even if an index does not exist, a list index out of range error does not occur.
#         if [x] == answer[-1:]:
#             continue
#         else:
#             answer.append(x)
#     return answer

# a = [1,2,3,4]

# breakpoint()

# arr = [1,1,3,3,0,1,1]	
# print(solution(arr)) # [1,3,0,1]
# arr = [4,4,4,3,3]	
# print(solution(arr)) # [4,3]





#- <기능개발>
# 문제 설명
# 프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

# 또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

# 제한 사항
# 작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
# 작업 진도는 100 미만의 자연수입니다.
# 작업 속도는 100 이하의 자연수입니다.
# 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.
# 입출력 예
# progresses	speeds	return
# [93, 30, 55]	[1, 30, 5]	[2, 1]
# [95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]
# 입출력 예 설명
# 입출력 예 #1
# 첫 번째 기능은 93% 완료되어 있고 하루에 1%씩 작업이 가능하므로 7일간 작업 후 배포가 가능합니다.
# 두 번째 기능은 30%가 완료되어 있고 하루에 30%씩 작업이 가능하므로 3일간 작업 후 배포가 가능합니다. 하지만 이전 첫 번째 기능이 아직 완성된 상태가 아니기 때문에 첫 번째 기능이 배포되는 7일째 배포됩니다.
# 세 번째 기능은 55%가 완료되어 있고 하루에 5%씩 작업이 가능하므로 9일간 작업 후 배포가 가능합니다.

# 따라서 7일째에 2개의 기능, 9일째에 1개의 기능이 배포됩니다.

# 입출력 예 #2
# 모든 기능이 하루에 1%씩 작업이 가능하므로, 작업이 끝나기까지 남은 일수는 각각 5일, 10일, 1일, 1일, 20일, 1일입니다. 어떤 기능이 먼저 완성되었더라도 앞에 있는 모든 기능이 완성되지 않으면 배포가 불가능합니다.

# 따라서 5일째에 1개의 기능, 10일째에 3개의 기능, 20일째에 2개의 기능이 배포됩니다.

# ※ 공지 - 2020년 7월 14일 테스트케이스가 추가되었습니다.



# import math 
# def solution(progresses, speeds):
#     done = []
#     for progress,speed in zip(progresses,speeds):
#         done.append(math.ceil((100 - progress) / speed))
#     done = list(reversed(done))

#     answer = []
#     count = 1
#     n = done.pop()
#     while True:
#         if len(done) == 0:
#             answer.append(count)
#             break    
#         if n >= done[-1]:
#             count += 1
#             done.pop()
#             if len(done) == 0:
#                 answer.append(count)
#                 break    
#         if n < done[-1]:
#             answer.append(count)
#             count = 1
#             n = done.pop()
#     return answer


# progresses = [93, 30, 55]
# speeds = [1, 30, 5]
# print(solution(progresses,speeds)) # [2, 1]
# progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1, 1, 1, 1, 1, 1]
# print(solution(progresses,speeds)) # [1, 3, 2]




#- <올바른 괄호> #- <VPS 1(Valid Parenthesis String)>
# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

# "()()" 또는 "(())()" 는 올바른 괄호입니다.
# ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 문자열 s의 길이 : 100,000 이하의 자연수
# 문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.
# 입출력 예
# s	answer
# "()()"	true
# "(())()"	true
# ")()("	false
# "(()("	false
# 입출력 예 설명
# 입출력 예 #1,2,3,4
# 문제의 예시와 같습니다.



# def solution(s):
#     #. If it's an opening parenthesis, add 1. If it's a closing parenthesis, subtract 1.
#     #. If it becomes negative in the middle or if it is not 0 at the end, then it's False.
#     #- 여는 괄호면 +1, 닫는 괄호면 -1
#     #- 중간에 -가 되버리거나, 다 끝났을 때 0이 아니면 False
#     answer = True
#     judge = 0
#     for x in s:
#         if judge < 0 :
#             return False
#         if x == '(':
#             judge += 1
#         if x == ')':
#             judge -= 1
#     if judge != 0:
#         return False 
#     return True


# s = "()()"
# print(solution(s)) # true
# s = "(())()"
# print(solution(s)) # true
# s = ")()("
# print(solution(s)) # false
# s = "(()("
# print(solution(s)) # false


