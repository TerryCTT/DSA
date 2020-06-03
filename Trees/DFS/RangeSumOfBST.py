# 938. Range Sum of BST
# Difficulty: Easy
# Problem: Given the root node of a binary search tree, 
# return the sum of values of all nodes with value between L and R (inclusive).

# The binary search tree is guaranteed to have unique values.

# Example 1:
# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32

# Example 2:
# Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
# Output: 23

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        # DFS pre-order
        # If root's val is between L and R (inclusive) add to sum
        # Due to nature of BST: 
        # If val is less than L, we know all values left are less than L
        # and if val is greater than R, we know all values right are greater than R
        # so we won't need to traverse through those nodes
        
        # runtime: O(n): iterate through all nodes n
        # space: O(h): callstack reaches at most height h of tree
        def dfs(root: TreeNode):
            # base case
            if (root is None):
                return

            # add val to sum if within bounds L and R
            # check appropriate nodes, due to nature of BST: 
            # If val is less than L, we know all values left are less than L
            # and if val is greater than R, we know all values right are greater than R
            # so we won't need to traverse through those nodes
            if (root.val >= L and root.val <= R):
                self.sum += root.val
                dfs(root.left)
                dfs(root.right)
            elif (root.val >= L):
                dfs(root.left)
            elif (root.val <= R):
                dfs(root.right)
                
        self.sum = 0
        dfs(root)
        return self.sum