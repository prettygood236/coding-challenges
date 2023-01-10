
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
import sys
n = int(sys.stdin.readline())
l = [int(sys.stdin.readline()) for _ in range(n)]

count = 0
stack = []
result = []
flag = True
for num in l:
  while True:
    if count >= num:
      break
    count += 1
    result.append('+')
    stack.append(count)
  if stack[-1] == num:
    result.append('-')
    stack.pop()
  else :
    flag = False
    break

if flag == False:
  print('NO')
else :
  for i in result:
    print(i)