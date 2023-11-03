# ---
# title: Target Number
# tags: [CodingChallenges, Python, DFS]
# created: '2023-11-03'
# ---

# ## Problem Description

# Given an array of non-negative integers, you can either add or subtract each number to reach a target number. The order of the numbers cannot be changed. The goal is to find out how many ways there are to reach the target number.

# ## Constraints

# - The number of given integers is 2 to 20.
# - Each number is a natural number from 1 to 50.
# - The target number is a natural number from 1 to 1000.

# ## Solution

# The problem can be solved using depth-first search (DFS). We start with the sum of 0 and the first number in the array. For each number, we recursively subtract and add it to the sum until we reach the end of the array. If the sum equals the target number, we increment a counter.

# ```python
def solution(numbers, target):
    answer = 0

    def dfs(sum, i):
        nonlocal answer
        if i == len(numbers):
            if sum == target:
                answer += 1
            return
        dfs(sum-numbers[i], i+1)
        dfs(sum+numbers[i], i+1)

    dfs(0, 0)
    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target)) # Expected: 5

numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target)) # Expected: 2
