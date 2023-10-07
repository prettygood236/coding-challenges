# ---
# title: Random Number Game
# tags: [CodingChallenges, Python, Greedy]
# created: '2022-11-08'
# ---

# ## Problem Description

# In the random number game, two players A and B each have a list of numbers. Both lists are sorted in ascending order. Each player chooses one number from their list and compares it with the other player's chosen number. 
# The player whose chosen number is larger gets one point. The game continues until there are no more numbers to choose from.
# The goal is to find out how many points Player B can score if both players always choose their smallest available number that has not been used yet.

# ## Solution

# This problem can be solved by using a greedy algorithm approach.

# ### Greedy Algorithm Approach

# ```python
def solution(A, B):
    A.sort()
    B.sort()

    points = 0
    b_index = 0

    for x in A:
        while b_index < len(B) and B[b_index] <= x:
            b_index += 1
        if b_index < len(B):
            points += 1
            b_index += 1

    return points


A = [5,1,3,7]	
B = [2,2,6,8]	
# Expected output: 3

A = [2,2,2,2]	
B = [1,1,1,1]	
# Expected output: 0

print(solution(A,B))
