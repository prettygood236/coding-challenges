# ---
# title: Expressing a Number using N
# tags: [CodingChallenges, Python, DynamicProgramming]
# created: '2023-10-07'
# ---

# ## Problem Description

# Given two integers `N` and `number`, you are allowed to use the number `N` along with any of the four basic arithmetic operations (+, -, *, /) to represent or express `number`. The task is to find out the minimum number of times you need to use `N` in an expression that equals `number`.

# Constraints:
# - N is between 1 and 9 inclusive.
# - The target number is between 1 and 32,000 inclusive.
# - Only parentheses and four basic arithmetic operations are allowed in expressions.
# - In division operation, ignore remainder part.
# - If it requires more than 8 uses of N then return -1.

# ## Solution

# This problem can be solved by dynamic programming. We create an array dp where each index represents how many times we have used digit N so far. For each index i we compute all possible values that can be made by using digit N i times. 

# We start from i=2 because when i=1 there's only one possibility which is equal to digit itself.

# ```python
def solution(N, number):
    # Case when only one usage of N is required
    if N == number:
        return 1
    
    # Case when more than one usage of N is required
    # Let's build up from bottom 
    dp = {1:{N}}
    c = 2
    while True:
        if c > 8:
            return -1
        s = set([int(str(N)*c)])
        for i in range(1,c//2+1):
            for x in dp[i]:
                for y in dp[c-i]:
                    s.update((x+y,x-y,y-x,x*y))
                    s.update((x//y,) if y!=0 else ())
                    s.update((y//x,) if x!=0 else ())
        
        # If target number found then return count of uses 
        if number in s:
            return c
        
        dp[c] = s
        c += 1

# Test cases   
N=5;number=24;
print(solution(N,number)) # Expected output :4  
