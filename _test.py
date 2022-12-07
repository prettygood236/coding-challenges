# from itertools import combination

# result = ''.join(sorted(str(n),key=lambda x:int(x),reverse=True))




# l = []

# def solution(people,limit):
#   if limit < 0:
#     return
  
#   for i in people:
#     limit -= people[i]
#     people = people[i:]
#     solution(people,limit)

#   answer = 0



# people = [70, 50, 80, 50]
# limit = 100

# solution(people,limit)




# scoville = [1, 2, 3, 9, 10, 12]	
# K = 7

# scoville.sort()
# count = 0

# while True:
#   count += 1
#   m = min(scoville[0],scoville[1])
#   n = max(scoville[0],scoville[1])
#   scoville[1] = m + (n * 2)
#   del scoville[0]
#   if len(scoville) == 1 and scoville[0] < K:
#     print(-1)
#     break
#   if scoville[0] >= K and scoville[1] >= K:
#     print(count)
#     break

# print(scoville)




# n = 8
# a = 4
# b = 7

# c = a
# a = min(c,b)
# b = max(c,b)

# t = n // 2
# answer = 0
# m = n
# count = 1
# while True:
#   if m == 2:
#     break
#   m = n // 2
#   count += 1


# if (a > t and b <= t):
#   answer = count
# elif b%2==0 and b-a==1:




# n = 2
# words = 	["hello", "one", "even", "never", "now", "world", "draw"]	
# d = {}
# d[words[0]] = 1
# criminal = 0
# answer = [0,0]

# for i in range(1,len(words)):
#   if (words[i] in d) or (words[i-1][-1]!=words[i][0]):
#     criminal = i+1
#     break
#   d[words[i]] = 1

# if criminal == 0:
#   answer = [0,0]
# else :
#   answer[0] = (criminal%n) or n
#   if answer[0] == n:
#     answer[1] = (criminal//n)
#   else :
#     answer[1] = (criminal//n) + 1

# print(answer)



w = input()
vowels = ['A','E','I','O','U']
answer = []

def dfs(word):
  for i in range(len(vowels)):
    word = word + vowels[i]
    if len(word) > 5:
      return
    answer.append(word)  #! 넣고!
    dfs(word) #! 돌리고!
    word = word[:-1] #! 뺴고! #?

dfs('')
print(answer.index(w)+1)

