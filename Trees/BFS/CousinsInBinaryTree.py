# 993. Cousins in Binary Tree
# Difficulty: Easy
# Problem:

# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

# Return true if and only if the nodes corresponding to the values x and y are cousins.

# Example 1:
# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false

# Example 2:
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true

# Example 3:
# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false

# Constraints:
# The number of nodes in the tree will be between 2 and 100.
# Each node has a unique integer value from 1 to 100.

# runtime: O(n): worst case we iterate through all nodes in tree
# space: O(n): queue max size will be bottom 2 levels of a tree
#              for a full tree: 2^maxDepth + 2^(maxDepth - 1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # Breadth-first Search, we queue nodes of the same level
        # First check if a node is parent of both x and y
        #    if true, we know x and y are siblings (return false)
        # Queue all children nodes of next level
        #    not cousins if we process a level and only x or y in queue (return false)        

        xFound = False
        yFound = False
        queue = []
        queue.append(root)
        
        # process nodes in tree
        while (queue):
            # determine number of nodes in level
            levelSize = len(queue)
            
            # only process up to number of nodes in level
            # keeps separation between current level and queueing nodes for next level
            for i in range(levelSize):
                parent = queue.pop(0)
                
                # check if parent is either x or y
                if (parent.val == x):
                    xFound = True
                elif (parent.val == y):
                    yFound = True
                
                # check if parent's children exist and if they're siblings
                if (parent.left is not None and parent.right is not None):
                    if ((parent.left.val == x and parent.right.val == y) 
                        or (parent.left.val == y and parent.right.val == x)):
                        return False
                
                # prepare next level of tree
                if (parent.left is not None):
                    queue.append(parent.left)
                if (parent.right is not None):
                    queue.append(parent.right)
                    
            # either x or y found (won't need to process next level)
            if (xFound or yFound):
                # they're cousins
                if (xFound and yFound):
                    return True
                # they're on different levels
                return False
                    
        return False