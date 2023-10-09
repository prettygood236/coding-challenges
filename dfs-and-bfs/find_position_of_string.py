# ---
# title: Find Position of String 
# tags: [CodingChallenges, Python, DFS]
# created: '2022-08-22'
# ---

# # Find Position of String in Lexicographically Sorted List of Vowel Strings

# ## Problem Description

# Given a string w consisting only of vowels ('A', 'E', 'I', 'O', 'U'), find its position when all strings consisting only of these vowels and having length at most 5 are sorted lexicographically.

# ## Constraints

# - The string w has length between 1 and 5.
# - Each character in w is an uppercase vowel ('A', 'E', 'I', 'O', or 'U').

# ## Solution

# This problem can be solved using depth-first search (DFS). The idea is to generate all possible strings with the given vowels and up to length 5. These strings are stored in a list called `answer`. The position of the input string in this list (plus one because the positions start from one) is the answer.

# ```python
def solution(w):
    vowels = ['A','E','I','O','U']
    answer = []

    def dfs(word):
      for i in range(len(vowels)):
        word = word + vowels[i]
        if len(word) > 5:
          return
        answer.append(word)  #! Add it!
        dfs(word) #! Run it!
        word = word[:-1] #! Remove it!

    dfs('')
    return answer.index(w)+1
