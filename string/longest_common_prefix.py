# ---
# title: Longest Common Prefix
# tags: [CodingChallenges, Python, Strings]
# created: '2022-07-11'
# ---

# ## Problem Description

# Given an array of strings, find the longest common prefix string amongst them. If there is no common prefix, return an empty string "".

# ## Solution

# The solution first checks if the input list is empty and returns an empty string if it is. Then it finds the shortest string in the list because the common prefix can't be longer than this shortest string. It then iterates over each character in this shortest string and checks if all other strings have same character at that position. If any other string has a different character then it returns prefix up to previous position.

# Here's how this looks in Python:

# ```python
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 

a = Solution()
strs = ["flower","flow","flight"]
print(a.longestCommonPrefix(strs))  # --> "fl"

a = Solution()
strs = ["dog","racecar","car"]
print(a.longestCommonPrefix(strs))  # --> ""
