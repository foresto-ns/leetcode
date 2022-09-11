# https://leetcode.com/problems/minimum-index-sum-of-two-lists/
#
# Given two arrays of strings list1 and list2, find the common strings with the least index sum.
# A common string is a string that appeared in both list1 and list2.
# A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j]
# then i + j should be the minimum value among all the other common strings.
# Return all the common strings with the least index sum. Return the answer in any order.

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d1 = {}
        ans = []
        
        min_sum = len(list1) + len(list2) + 1
        
        for i in range(len(list1)):
            d1[list1[i]] = i
        for i in range(len(list2)):
            if list2[i] in d1:
                if min_sum == i + d1[list2[i]]:
                    ans.append(list2[i])
                elif i + d1[list2[i]] < min_sum:
                    ans = [list2[i]]
                    min_sum = i + d1[list2[i]]
        
        return ans
