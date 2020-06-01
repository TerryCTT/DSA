# 1315. Sum of Nodes with Even-Valued Grandparent
# Difficulty: Medium
# Problem:
# Given a binary tree, return the sum of values of nodes with even-valued grandparent.  
# (A grandparent of a node is the parent of its parent, if it exists.)

# If there are no nodes with an even-valued grandparent, return 0.

# Example 1:
# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 18
# Explanation: The red nodes are the nodes with even-value grandparent 
# while the blue nodes are the even-value grandparents.
 

# Constraints:
# The number of nodes in the tree is between 1 and 10^4.
# The value of nodes is between 1 and 100.

# runtime: O(n): traverse all nodes in tree
# space: O(h): call stack reaches height h of tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        sum = 0
        
        def dfs(node: TreeNode, parent: TreeNode, grandparent: TreeNode, sum: int) -> int:
            # base case
            if (node is None):
                return 0

            # increase sum by values of left and right children who have even grandparents
            sum += dfs(node.left, node, parent, sum) + dfs(node.right, node, parent, sum)

            # increase sum by value of current node if grandparent is even
            if (grandparent is not None and grandparent.val % 2 == 0):
                sum += node.val
            return sum
        
        sum = dfs(root, None, None, sum)
        return sum