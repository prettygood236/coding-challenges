
#. BAEKJOON 2745. <Number system conversion 1>
# import sys
# n,b = sys.stdin.readline().split()
# b = int(b)
# result = 0
# c = len(n)-1

# for i in n:
#   temp = int(i,36)
#   result += temp*(b**c)
#   c-=1

# print(result)



#. BAEKJOON 11005. <Number system conversion 2>
# import sys
# n,b = map(int,sys.stdin.readline().split())

# digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  
# result = ""

# while n > 0:
#   remainder = n % b
#   result = digits[remainder] + result
#   n //= b  

# print(result)  
  


#. BAEKJOON 2720. <Quick Change>

