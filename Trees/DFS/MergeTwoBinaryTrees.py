# 617. Merge Two Binary Trees
# Difficulty: Easy
# Problem:
# Given two binary trees and imagine that when you put one of them to cover
# the other, some nodes of the two trees are overlapped while the others are not.

# You need to merge them into a new binary tree. The merge rule is that if two 
# nodes overlap, then sum node values up as the new value of the merged node. 
# Otherwise, the NOT null node will be used as the node of new tree.

# Example 1:

# Input: 
#     Tree 1                     Tree 2                  
#           1                         2                             
#          / \                       / \                            
#         3   2                     1   3                        
#        /                           \   \                      
#       5                             4   7                  
# Output: 
# Merged tree:
#          3
#         / \
#        4   5
#       / \   \ 
#      5   4   7

# Note: The merging process must start from the root nodes of both trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # DFS
        # Traverse both trees at the same time
        # Create a new tree (could overwrite t1 or t2, but may want to preserve data)
        # If a node exists at the same place in both trees t1 t2, sum their values
        # If only one node exists, take that node and put into new tree
        # If t1 or t2 is fully processed, copy the rest of the other tree
        
        # runtime: O(n + m): process all n nodes in t1 and all m nodes in t2
        # space: O(max(n,m)): larger of n or m nodes in t1 since overlap = 1 node
        merged = TreeNode()

        def dfs(mergedCurr: TreeNode, t1Curr: TreeNode, t2Curr: TreeNode) -> TreeNode:
            # base case. If either tree reaches null, return rest of other tree
            # (or null in event both trees reach null)
            if (t1Curr is None):
                return t2Curr
            elif (t2Curr is None):
                return t1Curr
            
            # pre-order traversal
            mergedCurr = TreeNode(t1Curr.val + t2Curr.val)
            mergedCurr.left = dfs(mergedCurr.left, t1Curr.left, t2Curr.left)
            mergedCurr.right = dfs(mergedCurr.right, t1Curr.right, t2Curr.right)
        
            return  mergedCurr

        merged = dfs(merged, t1, t2)
        return merged