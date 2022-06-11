class Solution:
  def romanToInt(self, s: str) -> int:
    romans = {
      'I':1,
      'V':5,
      'X':10,
      'L':50,
      'C':100,
      'D':500,
      'M':1000,
    }
    pre = s[0]
    result = 0
    for i in s:
      cur = i
      if romans[pre] >= romans[cur]: 
        result += romans[cur]
      else:
        result += romans[cur] - 2*romans[pre]
      pre = cur
    return result
  
a = Solution()
print(a.romanToInt("MCMXCIV"))

'''
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''
  