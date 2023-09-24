# ---
# title: Sugar Delivery
# tags: [Loop]
# created: '2022-08-23'
# ---

# # Sugar Delivery

# ## Problem Description


# ## Solution
# The goal is to minimize the number of bags. Start by dividing all by 5 and try to fit in 3. Keep subtracting 5 until it divides evenly.

# ```python
import sys

n = int(sys.stdin.readline()) # Examples: 18, 4, 6, 9, 11

a = n//5 # Quotients when divided by five: e.g., for above examples -> 3,0,1,1,2
b = n%5 # Remainders when divided by five: e.g., for above examples -> 3,4,1,4,

while True:
    c = b//3 # Quotients when remainder divided by three.
    d = b%3 # Remainders when remainder divided by three - Must be zero. If not zero -> subtract one from the quotient of five and try again. If zero -> print(a+c)

    if d ==0:
        print(a+c)
        break
    
    if d !=0 and a ==0:
        print(-1)
        break
    
    a -=1 
    b +=5 
