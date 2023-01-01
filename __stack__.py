
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
import sys
while True:
  data = list(sys.stdin.readline().rstrip())
  if len(data) == 1 and data[0] == '.':
    break
  l = []
  flag = True
  for i in range(len(data)):
    a = data.pop()
    if a == '(':
      if l:
        b = l.pop()
        if b != ')':
          print('NO')
          flag = False
          break
      else:
        print('NO')
        flag = False
        break
    
    if a == '[':
      if l:
        b = l.pop()
        if b != ']':
          print('NO')
          flag = False
          break
      else:
        print('NO')
        flag = False
        break

    if a == ')' or a ==']':
      l.append(a)

  if not(flag):
    continue 
  if data or l:
    print('NO')
    continue
  print('YES')