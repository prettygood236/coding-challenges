
#. Strings are immutable. Therefore, you can't use 'sort', but you can use 'sorted'.
#. In Python, strings are indeed immutable. This means that once a string is created, it cannot be changed. However, you can reassign the variable to a new string. This doesn't change the original string but rather creates a new one. For example, if you have a string s = "Hello", and then do s = "World", you haven't changed "Hello" to "World". Instead, you've created a new string "World" and made s point to it.
#. Read the problem correctly.

#- <Print Verbatim>

# while True:
#   try:
#     print(input())
#   except EOFError:
#     break




#- <Starring>

# n = int(input())

# for i in range(1,n):
#     print(' '*(n-i)+'*'*(i*2-1))

# for i in range(n,0,-1):
#     print(' '*(n-i)+'*'*(i*2-1))




#- <Reorder Baskets>

# import sys

# n,m = map(int,sys.stdin.readline().split())
# l = [i+1 for i in range(n)]

# for _ in range(m):
#     i,j,k = map(int,sys.stdin.readline().split())
#     a = l[i-1:k-1]
#     b[0] = l[k-1:j]
#     l[i-1:j] = b[0]+a
    
# print(*l)




#- <Check for Palindromes>

# import sys
# s = list(sys.stdin.readline().rstrip())
# r = list(reversed(s))

# if s == r:
#     print(1)
# else :
#     print(0)



#- <Your rating is>

import sys

result = 0
count = 0

for _ in range(20):
    a,b,c = sys.stdin.readline().rstrip().split()
    if c != 'P':
        count += int(b[0])
    if c == 'A+':
        result += int(b[0])*4.5
    if c == 'A0':
        result += int(b[0])*4
    if c == 'B+':
        result += int(b[0])*3.5
    if c == 'B0':
        result += int(b[0])*3
    if c == 'C+':
        result += int(b[0])*2.5
    if c == 'C0':
        result += int(b[0])*2
    if c == 'D+':
        result += int(b[0])*1.5
    if c == 'D0':
        result += int(b[0])*1

print(round(result/count,6))