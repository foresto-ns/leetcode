# https://leetcode.com/problems/container-with-most-water/
#
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints
# of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        j = len(height) - 1
        mx = 0
        for i in range(len(height)):
            while i < j and height[i] >= height[j]:
                mx = max(mx, (min(height[i], height[j])*(j-i)))
                j -= 1
            mx = max(mx, (min(height[i], height[j])*(j-i)))
                
        return mx
