# ---
# title: Make a big number
# tags: [Greedy, Stack]
# created: '2023-09-24'
# ---

# # Make a big number

# ## Problem Description

# Find the maximum number that can be obtained by removing k digits from a given number. The given number is provided as a string and k is an integer.

# ## Constraints

# - The number is at least 2 digits and at most 1,000,000 digits.
# - k is a natural number less than the digit length of the number.

# ## Solution

# #. The "Max Number" problem applies the LIFO (Last-In-First-Out) principle. 
# #. If the current digit is larger than previous ones, then previous ones become unnecessary and hence removed. 
# #* By using stack data structure we can implement this logic succinctly.

# ```python
def solution(number, k):
    # Initialize stack with the first number
    stack = [number[0]]
    for num in number[1:]:
        # Remove elements from the stack while top of the stack is less than num and k > 0
        while len(stack) > 0 and stack[-1] < num and k > 0:
            # remove one element from removal count
            k -= 1
            # remove last element from stack as it's smaller than current element 
            stack.pop()
        # append current element to end of list (stack)
        stack.append(num)
    # If still have to remove more elements (k>0), remove them from end of list(stack)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)

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



