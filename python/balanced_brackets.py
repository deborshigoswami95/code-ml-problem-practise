"""
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.

"""

# My solution
def check_balance(s):
    close_dict = {"{": "}", 
               "(":")", 
               "[":"]"}
    close_set = {"}", "]", ")"}
    open_set = {"{", "[", "("}
    close_list = []
    
    for i in s:
        if len(close_list)>0:
            if i in close_set and i == close_list[-1]:
                close_list = close_list[:-1]
            elif i in open_set:
                close_list.append(close_dict[i])
            else:
                return False
        else:
            if i in open_set:
                close_list.append(close_dict[i])
            else:
                return False
    return True
  
if __name__=="__main__":
  check_balance("{}(([])){[]}") # True
  check_balance("{{])}") # False
    
