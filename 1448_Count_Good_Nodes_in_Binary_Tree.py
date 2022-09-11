# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
#
# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with
# a value greater than X.
# Return the number of good nodes in the binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode, mx=None) -> int:
        cnt = 0
        
        if not mx and mx != 0:
            mx = root.val
        
        if root.val >= mx:
            mx = root.val
            cnt += 1
        
        if root.left:
            cnt += self.goodNodes(root.left, mx)
        if root.right:
            cnt += self.goodNodes(root.right, mx)
        
        return cnt
