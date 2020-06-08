# 1302. Deepest Leaves Sum
# Difficulty: Medium
# Problem:
# Given a binary tree, return the sum of values of its deepest leaves.

# Example 1:
# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
 

# Constraints:
# The number of nodes in the tree is between 1 and 10^4.
# The value of nodes is between 1 and 100.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        # DFS
        # traverse through tree to find max level and add value of
        # nodes at max level to sum
        
        # runtime: O(n): traverse through all nodes of tree once
        # space: O(h): call stack reaches height of tree 
        levelSum = 0
        maxDepth = 0

        def dfs(node: TreeNode, level: int):
            nonlocal levelSum, maxDepth
            
            # base case
            if (node is None):
                return
            
            # true if we've reached a deeper level
            if (level > maxDepth):
                maxDepth = level
                levelSum = 0
            
            # add val to sum only if no children (potentially deepest level of tree)
            # and know we are potentially at the deepest level
            if (node.left is None and node.right is None and level == maxDepth):
                levelSum += node.val
            
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
    
        dfs(root, 0)
        return levelSum 