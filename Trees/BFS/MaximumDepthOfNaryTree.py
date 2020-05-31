# 559. Maximum Depth of N-ary Tree
# Difficulty: Easy
# Problem:

# Given a n-ary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest 
# path from the root node down to the farthest leaf node.

# Nary-Tree input serialization is represented in their level order traversal, 
# each group of children is separated by the null value (See examples).

# Example 1:
# Input: root = [1,null,3,2,4,null,5,6]
# Output: 3

# Example 2:
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: 5
 
# Constraints:
# The depth of the n-ary tree is less than or equal to 1000.
# The total number of nodes is between [0, 10^4].

# runtime: O(n): process all nodes within tree
# space: O(n): size of queue to hold nodes of a level within tree

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # BFS approach
        # Queue nodes one level at a time
        # Increment a depth counter each time we process a level
        # Finished processing all nodes once queue is empty
        
        # handle null case
        if (root is None):
            return 0
        
        depth = 0;
        queue = []
        queue.append(root);
        
        # process nodes in tree
        while (queue):
            # determine number of nodes in current level
            levelSize = len(queue)
            
            # only process up to number of nodes in level
            # keeps separation between current level and queueing nodes for next level
            for i in range(levelSize):
                parent = queue.pop(0)
                
                # queue children of current level
                for j in range(len(parent.children)):
                    queue.append(parent.children[j])

            # increase depth after processing a level
            depth += 1

        return depth