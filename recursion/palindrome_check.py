# ---
# title: Palindrome Check
# tags: [CodingChallenges, Python, Recursion, Palindrome]
# created: '2022-09-09'
# ---

# ## Problem Description

# A palindrome is a word, number, phrase, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization). Write a function that checks if given string is palindrome.

# ## Solution

# This problem can be solved using recursion. The idea is to compare first and last character of the string. If they are equal then we recursively check for remaining substring (by excluding first and last character). If at any point first and last character are not equal then we return 0 indicating it's not a palindrome.


# ```python
def isPalidrome(str):
  call = 0

  def recursion(str,l,r,call):
    call += 1
    if l >= r :
      print(1,call)
      return 1
    elif str[l] != str[r]:
      print(0,call)
      return 0
    else :
      return recursion(str,l+1,r-1,call)
  
  return recursion(str,0,len(str)-1,call)

import sys
N = int(sys.stdin.readline())
for _ in range(N):
  str = sys.stdin.readline().strip()
  isPalidrome(str)
