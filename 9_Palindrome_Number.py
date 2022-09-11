# https://leetcode.com/problems/palindrome-number/
#
# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        st = str(x)
        x1, x2 = st[:len(st)//2], st[(len(st) + 1)//2:][::-1]
        print(x1, x2)
        if x1 == x2:
            return True
        return False
