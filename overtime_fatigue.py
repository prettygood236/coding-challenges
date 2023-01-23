def solution(n, works):
    works.sort(reverse=True)
    while True:
      if n == 0 or works[0] == 0:
        print('11111111')
        print('n =',n)
        print(works)
        break
      count = 1
      diff = 0 
      for i in range(1,len(works)):
        diff = works[i-1] - works[i]
        print('diff =',diff)
        if diff == 0:
          print('2222222')
          count = i+1
          print('count =',count)
        else:
          print('3333333333')
          break 
      if diff > n or works[0] == works[-1]:
        print('44444444')
        print('n =',n)
        if n//count:
          print('55555555')
          print('n//count =',n//count)
          for j in range(count):
            works[j] -= n//count
          n = n % (n//count)
          print(works)
          print('n =',n)
        else:
          print('66666666')
          for j in range(n):
            works[j] -= 1
          print(works)
          n = 0
          break
      if n >= diff:
        print('7777777777')
        for j in range(count):
          works[j] -= diff
          n -= diff
          print(works)
          print('n =',n)
          if n < diff :
            print('88888888')
            print(works)
            print('n =',n)
            break
    answer = 0
    if works[0] < 0:
      answer = 0
    else:  
      for i in works:
        answer += i**2
    return answer


# works = [4, 3, 3]	
# n = 4	
# # result = 12

# works = [2, 1, 2]	
# n = 1	
# # result = 6

# works = [1,1]	
# n = 3	
# # result = 0

works = [40000,45000,45000,45000,45000,50000]
n = 999999

print(solution(n, works))