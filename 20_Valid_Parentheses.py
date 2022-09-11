# https://leetcode.com/problems/valid-parentheses/
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:        
        res = [s[0]]
        
        for i in range(1, len(s)):
            
            res.append(s[i])
            
            if s[i] == ')':
                if len(res) > 1 and res[-2] == '(':
                    res.pop(-1)
                    res.pop(-1)
                else:
                    return False
            
            elif s[i] == ']':
                if len(res) > 1 and res[-2] == '[':
                    res.pop(-1)
                    res.pop(-1)
                else:
                    return False
                
            elif s[i] == '}':
                if len(res) > 1 and res[-2] == '{':
                    res.pop(-1)
                    res.pop(-1)
                else:
                    return False
            
        
        if len(res) == 0:
            return True
        else:
            return False
