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

# ============================================================================
# Personal Notes:
# While this approach works, DFS is better solution (0 ms compared to 3 ms)
# and space comparison is O(h) for height of tree while BFS is O(w) for width
# ============================================================================

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        # BFS
        # traverse through tree by level, keeping a sum of level
        # reset level sum to 0 at start of each level
        # once final level has been processed, return level sum
        
        # runtime: O(n): traverse through all nodes of tree once
        # space: O(w): queue max size is the widest level of tree 
        
        levelSum = 0
        
        queue = []
        queue.append(root)

        # process all nodes of tree
        while (queue):
            levelSum = 0
            
            # determine number of nodes in current level
            levelSize = len(queue)
            
            # process up to number of nodes of that level
            for i in range (levelSize):
                parent = queue.pop(0)
                
                levelSum += parent.val
                # might seem like an optimization to only add value if
                # parent has no children (since we only care about last level)
                # but operation to add takes about same time to check if
                # the parent node has no children
                
                # setup next level
                if (parent.left is not None):
                    queue.append(parent.left)
                
                if (parent.right is not None):
                    queue.append(parent.right)
        
        return levelSum