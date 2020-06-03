# June Challenge Day 1: Invert Binary Tree
# Problem:
# Invert a binary tree.

# Example:

# Input:

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # DFS (pre-order)
        # swap left and right child

        # runtime: O(n): process all n nodes in tree
        # space: O(h): callstack reaches height h of tree
        
        # base case
        if (root is None):
            return root
        
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root