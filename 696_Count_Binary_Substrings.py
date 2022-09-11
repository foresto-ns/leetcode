# https://leetcode.com/problems/count-binary-substrings/
#
# Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's,
# and all the 0's and all the 1's in these substrings are grouped consecutively.
# Substrings that occur multiple times are counted the number of times they occur.

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            for j in range(1, (len(s)-i)//2+1):
                
                if sum(map(int, list(s[i:i+j]))) == 0 and sum(map(int, list(s[i+j:i+2*j]))) == j:
                    count += 1
                elif sum(map(int, list(s[i:i+j]))) == j and sum(map(int, list(s[i+j:i+2*j]))) == 0:
                    count += 1

        return count
