def solution(number,k):
    stack = [number[0]]
 
    # breakpoint()
    for n in number[1:]:
        while k and stack and n > stack[-1]:
            stack.pop()
            k -= 1
        stack.append(n)

    return ''.join(stack[:-k]) if k else ''.join(stack)


number = '98'
k = 1
print(solution(number, k)) #'9'
number = '98765'
k = 2
print(solution(number, k)) #'987'
number = '98675'
k = 2
print(solution(number, k)) #'987'
number = '444456'
k = 3
print(solution(number, k)) #'456'
number = '1924'
k = 2
print(solution(number, k)) #'94'
number = '1231234'
k = 3
print(solution(number, k)) #'3234'
number = '4177252841'
k = 4
print(solution(number, k)) #'775841'
