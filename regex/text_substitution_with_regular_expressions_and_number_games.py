# ---
# title: Text Substitution with Regular Expressions and Number Games
# tags: [CodingChallenges, Python, RegularExpressions, TextProcessing]
# created: '2023-07-11'
# ---

# ## Problem Description

# You are given a range of numbers from 1 to n and you are required to replace certain numbers in this range with a specified character. The numbers to be replaced are "3", "6", and "9".

# Write a Python script to perform this number substitution.

# ## Solution

# This problem can be solved using regular expressions (regex) and list comprehension in Python. Python's `re` module provides functions to work with regular expressions. The `re.sub()` function can be used to replace substrings that match a regex pattern.

# ```python
import re
list = [] 
for _ in range(1, int(input())+1):
  list.append(str(_))
  
temp = ' '.join(list) 

result = re.sub(r"(3|6|9)", "X", temp)

print(*result,sep='')
