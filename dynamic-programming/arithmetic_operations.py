# ---
# title: Arithmetic Operations
# tags: [CodingChallenges, Python, DynamicProgramming]
# created: '2023-10-14'
# ---

# ## Problem Description

# In arithmetic operations, addition (+) follows the associative law, but subtraction (-) does not. For example, the expression 1 - 5 - 3 can yield different results depending on the order of operations:

# ((1 - 5) - 3) = -7
# (1 - (5 - 3)) = -1
# As shown above, subtraction can produce different results depending on the order of operations. 

# Another example is the expression 1 - 3 + 5 - 8 which can yield five different results depending on operation orders:

# (((1 - 3) + 5) - 8) = -5
# ((1 - (3 + 5)) -8 ) =-15 
# (1- ((3+5)-8))=1 
# (1-(3+(5-8)))=1 
# ((1-3)+(5-8))=-5 
# The different operation orders for this expression give [-15,-5,-5,1,11] and among these maximum is `11`.

# Given an array `arr` containing strings of numbers and two operators "+" and "-", return the maximum value that can be obtained by calculating in all possible orders.

# ## Solution

# This problem can be solved using dynamic programming. The idea is to calculate maximum and minimum values for all possible sets of numbers by considering each possible location of operators.

# ```python
def solution(arr):
    # n is the number of digits in the given array.
    n = (len(arr) + 1) // 2

    # dp_max and dp_min are tables (2D arrays) to store the maximum and minimum values, respectively. 
    # Initialize with very small (-infinity) and very large (+infinity) values.
    dp_max = [[-float('inf')] * n for _ in range(n)]
    dp_min = [[float('inf')] * n for _ in range(n)]

    # Set each digit's own maximum and minimum values to itself.
    for i in range(n):
        dp_max[i][i] = dp_min[i][i] = int(arr[i*2])

    # This part performs a loop over all possible sections (sets of numbers).
    for cnt in range(2, n+1):
        # 'cnt' represents the number of digits included in each section.
        # Starting from '2', it considers all possible sections starting from those made up of two digits.
        
        for start in range(n-cnt+1):
            # 'start' is the starting point of each section. 
            # For example, if the array is [1,'+',2,'-',3], possible starting points are first element '1', third element '2', fifth element '3', etc., which correspond to indices 0, 2, 4 respectively.
            
            end = start + cnt - 1
            # 'end' is the end point of each section calculated based on the defined 'start' and number of digits included ('cnt').

            # For '+' case: Based on where the '+' operator is located, divide into left and right sections,
            # The sum of either maximum or minimum value from each section becomes that section's maximum or minimum value.
            # For '-' case: Based on where the '-' operator is located, divide into left and right sections,
            # Subtracting right section's minimum value from left section's maximum value becomes that section's maximum value,
            # Subtracting right section's maximum value from left section's minimum value becomes that section’s minimum value.
            for i in range(start, end):
                if arr[i*2+1] == '+':
                    dp_max[start][end] = max(dp_max[start][end], dp_max[start][i] + dp_max[i+1][end])
                    dp_min[start][end] = min(dp_min[start][end], dp_min[start][i] + dp_min[i+1][end])
                else:
                    dp_max[start][end] = max(dp_max[start][end], dp_max[start][i] - dp_min[i+1][end])
                    dp_min[start][end] = min(dp_min[start][end], dp_min[start][i] - dp_max[i+1][end])

                print(dp_max)
                print(dp_min)


    # Finally, 'dp_max[0][-1]' represents among calculation results of largest possible scope containing all numbers. 
    return int(dp_max[0][-1])

arr = ["1", "-", "3", "+", "5", "-", "8"]	
print(solution(arr)) # 1
arr = ["5", "-", "3", "+", "1", "+", "2", "-", "4"]	
print(solution(arr)) # 3