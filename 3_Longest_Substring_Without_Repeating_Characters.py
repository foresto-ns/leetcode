# https://leetcode.com/problems/longest-substring-without-repeating-characters/
#
# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst = []
        max_len = 0
        
        for i in range(len(s)):
            if s[i] not in lst:
                lst += s[i]
            else:
                index = lst.index(s[i])
                lst = lst[index+1:]
                lst += s[i]
            max_len = max(max_len, len(lst))

        return max_len
