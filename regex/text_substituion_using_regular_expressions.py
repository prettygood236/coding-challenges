# ---
# title: Text Substitution using Regular Expressions
# tags: [CodingChallenges, Python, RegularExpressions, TextProcessing]
# created: '2023-07-11'
# ---

# ## Problem Description

# You are given a string and you are required to replace certain substrings in the string with a specified character. The substrings to be replaced are "dz=", "lj", "nj", and any character that is alphanumeric or underscore followed by a non-alphanumeric and non-underscore character.

# Write a Python script to perform this text substitution.

# ## Solution

# This problem can be solved using regular expressions (regex). Python's `re` module provides functions to work with regular expressions. The `re.sub()` function can be used to replace substrings that match a regex pattern.

# ```python
import re

result = re.sub('dz=|[ln]j|\w\W','A',input())

# 'dz=|[ln]j|\w\W' : This pattern matches either "dz=", "lj", "nj", or 
# any character that is alphanumeric, a number, or an underscore (_) starting and followed by a character that is not alphanumeric, a number, or an underscore (_)

print(result)