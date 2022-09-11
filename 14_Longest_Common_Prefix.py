# https://leetcode.com/problems/longest-common-prefix/
#
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for i in range(len(strs[0])):
            prefix += strs[0][i]
            for j in range(1, len(strs)):
                if len(strs[j]) == i-1 or strs[j][:i+1] != prefix:
                    return prefix[:-1]
        return prefix
