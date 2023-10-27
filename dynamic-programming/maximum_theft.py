# ---
# title: Maximum Theft 
# tags: [CodingChallenges, Python, DynamicProgramming]
# created: '2023-10-21'
# ---

# ## Problem Description

# A thief is planning to rob a village. The houses in the village are arranged in a circle as shown below.

# [Image]

# Each house has a security system connected to its adjacent houses. Therefore, if two adjacent houses are robbed, the alarm will go off.

# Given an array `money` that contains the amount of money in each house, write a function `solution(money)` that returns the maximum amount of money that the thief can steal without setting off an alarm.

# ## Solution

# This problem can be solved using dynamic programming. The idea is to calculate maximum amounts for all possible sets of houses by considering each possible starting point (first or second house) and excluding last house when first one is considered because they are connected.


# ```python
def solution(money):
    n = len(money)

    # The case where the first house can be chosen (the last house cannot be chosen)
    dp_first = [0] * n
    dp_first[0] = money[0] # Don't visit last house
    dp_first[1] = max(money[0],money[1])

    for i in range(2,n-1):
        dp_first[i] = max(dp_first[i-2]+money[i],dp_first[i-1])

    # The case where the last house can be chosen (the first house cannot be chosen)
    dp_last = [0] * n
    dp_last[0] = 0 # Don't visit first house
    dp_last[1] = money[1]

    for i in range(2,n):
        dp_last[i] = max(dp_last[i-2]+money[i],dp_last[i-1])

    return max(max(dp_first),max(dp_last))
money=[1,3,5,7,9]; 
print(solution(money)) #14