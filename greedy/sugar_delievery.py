# ---
# title: Sugar Delivery
# tags: [CodingChallenges, Python, Greedy]
# created: '2023-08-23'
# ---

# # Sugar Delivery

# ## Problem Description

# A sugar factory needs to deliver N kilograms of sugar to a customer. The factory has two types of bags, one that can carry 5 kilograms and the other can carry 3 kilograms. The goal is to use the least number of bags for delivery. Given N (1 ≤ N ≤ 5000), find out the minimum number of bags needed.

# ## Constraints

# - The input is an integer N (1 ≤ N ≤ 5000).

# ## Solution

# This problem can be solved by using a greedy approach along with simple arithmetic operations. 

# Firstly, we calculate how many 5kg bags (`a`) we can use by dividing `N` by `5`. Then, we calculate the remainder (`b`) when `N` is divided by `5`. 

# In a loop, we check if the remainder (`b`) is divisible by `3`. If it is divisible (`d == 0`), then we print the total number of bags used (`a+c`). If not divisible and there are no more 5kg bags left to adjust(`a == 0`), then it's impossible to deliver exactly `N` kg so print `-1`.

# If not divisible but there are still some 5kg bags left(`a !=0`), then subtract one from the quotient of five and add five to remainder. Continue this process until either it's possible or impossible.

# ```python
import sys

def solution(n):
    # Quotients when divided by five: e.g., for above examples -> 3,0,1,1,2
    a = n//5 
    # Remainders when divided by five: e.g., for above examples -> 3,4,1,4
    b = n%5 

    while True:
        # Quotients when remainder divided by three.
        c = b//3 
        # Remainders when remainder divided by three - Must be zero.
        d = b%3 
        
        if d ==0:
            return(a+c) # If zero -> print(a+c)
    
        if d !=0 and a ==0:
            return -1
    
        # If not zero -> subtract one from the quotient of five and try again.
        a -=1 
        b +=5
i