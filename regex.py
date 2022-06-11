import re

result = re.sub('dz=|[ln]j|\w\W','A',input())

# 'dz=|[ln]j|\w\W' : dz= 이거나 lj / nj 이거나 
# 알파벳, 숫자, _ (w)인 문자로 시작해 알파벳, 숫자, _가 아닌 문자(W)로 끝나는 것

print(result)


# import re
# list = [] 
# for _ in range(1, int(input())+1):
#   list.append(str(_))
  
# temp = ' '.join(list) 

# result = re.sub(r"(3|6|9)", "X", temp)

# print(*result,sep='')


