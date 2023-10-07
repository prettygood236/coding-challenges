# ---
# title: The Apartment President
# tags: [CodingChallenges, Python, DynamicProgramming]
# created: '2022-08-23'
# ---

# # The Apartment President

# ## Problem Description

# In this problem, we are given two integers k and n. There is an apartment with k+1 floors (from 0 to k) and n rooms (from 1 to n) on each floor. The rule of the apartment is that a person can move into room n on the kth floor only if they have lived in room n or room (n-1) on the (k-1)th floor. On the 0th floor, each room i has i people living in it. Your task is to find out how many people live in room number n on the kth floor.

# ## Constraints

# - The input consists of an integer T which represents the number of test cases (1 ≤ T ≤ 1000), followed by T lines each containing two integers k and n (0 ≤ k ≤ 14, 1 ≤ n ≤ 14).

# ## Solution

# We use dynamic programming to solve this problem. We create a list `f` where f[i] represents number of people living in ith room on current floor. For each test case, we start from first floor and for each subsequent floor we update f[i] as sum of all elements from f[0] through f[i].

# ```python
import sys 

l = int(sys.stdin.readline())

for _ in range(l):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    f = list(range(1,15))
    
    for _ in range(k):
        s = 0
        
        for i in range(len(f)):
            s += f[i]
            f[i] = s
            
    print(f[n-1])
