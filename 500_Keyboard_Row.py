# https://leetcode.com/problems/keyboard-row/
#
# Given an array of strings words, return the words that can be typed using letters of the alphabet
# on only one row of American keyboard like the image below.
# In the American keyboard:
# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set('zxcvbnm')
        
        ans = []
        for word in words:
            word_set = set(word.lower())
            if word_set.issubset(row1) or word_set.issubset(row2) or word_set.issubset(row3):
                ans.append(word)
                
        return ans
