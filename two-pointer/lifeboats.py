# ---
# title: Lifeboats
# tags: [CodingChallenges, Python, TwoPointerAlgorithm]
# created: '2023-08-07'
# ---

# ## Problem Description

# People are trapped on a desert island and you need to rescue them using lifeboats. The lifeboat is small and can only carry up to 2 people at a time, and there is also a weight limit.

# For example, if people's weights are [70kg, 50kg, 80kg, 50kg] and the weight limit of the lifeboat is 100kg then the second person and fourth person can ride together but the first person and third person have a total weight of 150kg which exceeds the weight limit of the lifeboat so they cannot ride together.

# The goal is to use as few lifeboats as possible to rescue all people.

# Given an array `people` containing weights of each person and an integer `limit` denoting weight limit of each boat. You need to return minimum number of boats required to save all people.

# Constraints:
# - The number of people trapped on an uninhabited island ranges from at least one up to 50,000.
# - Each individual's bodyweight ranges from at least 40 kg up to 240 kg.
# - The load capacity (weight limit) for each boat ranges from at least 40 kg up to 240 kg.
# - The load capacity for each boat will always be given larger than maximum individual bodyweight hence it will always be possible for everyone get rescued.


# ## Solution

# ### Two Pointer 
# ####. The Two Pointers algorithm : A technique used in programming to solve problems by moving two pointers within a data structure. 
# ####. It's commonly used in linked lists and sorted arrays for tasks such as finding elements, detecting cycles, or locating subarrays with specific sums.
# ####. The two pointers move at different speeds, so a while loop is used to handle this.

# ```python
def solution(people, limit):
    people.sort(reverse=True)
    answer = 0
    i = 0
    j = len(people) -1

    while i <= j:
        temp = limit
        temp -= people[i]
        i += 1
        # The condition i-1 != j is not necessary, but it can provide precision.
        if people[j] <= temp and i-1 != j :
            j -= 1
        answer += 1

    return answer

     
# Test cases   
people = [70,60,50,30,27,3]
limit = 100
print(solution(people,limit)) #3
people = [70, 50, 80, 50]
limit = 100
print(solution(people,limit)) #3
people = [70, 80, 50]
limit = 100
print(solution(people,limit)) #3
