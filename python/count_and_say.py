"""
https://leetcode.com/problems/count-and-say/
"""

class Solution:
  def say(self, digit_string: str) -> str:
    
    if digit_string=='1':
      return '11'
    
    prev = digit_string[0]
    counter = 1
    solution = ''

    for i in digit_string[1:]:
        if i==prev:
            counter += 1
        else:
            solution += str(counter)+prev
            prev = i
            counter = 1

    if solution == '':
        return str(counter)+prev
    else:
        return solution + str(counter) + prev
      
  def countAndSay(self, n: int) -> str:
        
    if n==1:
        return "1"

    for i in range(2,n+1):
        if i==2:
            current_say = self.say('1')
        else:
            current_say = self.say(current_say)

    return current_say
