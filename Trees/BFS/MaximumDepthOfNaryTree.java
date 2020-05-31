// 559. Maximum Depth of N-ary Tree
// Difficulty: Easy
// Problem:

// Given a n-ary tree, find its maximum depth.

// The maximum depth is the number of nodes along the longest 
// path from the root node down to the farthest leaf node.

// Nary-Tree input serialization is represented in their level order traversal, 
// each group of children is separated by the null value (See examples).

// Example 1:
// Input: root = [1,null,3,2,4,null,5,6]
// Output: 3

// Example 2:
// Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
// Output: 5
 
// Constraints:
// The depth of the n-ary tree is less than or equal to 1000.
// The total number of nodes is between [0, 10^4].

// runtime: O(n): process all nodes within tree
// space: O(n): size of queue to hold nodes of a level within tree

import java.util.LinkedList; 
import java.util.Queue;

/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val,List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
    public int maxDepth(Node root) {
        // BFS approach
        // Queue nodes one level at a time
        // Increment a depth counter each time we process a level
        // Finished processing all nodes once queue is empty
        
        // handle null case
        if (root == null) {
            return 0;
        }
        
        int depth = 0;
        Queue<Node> queue = new LinkedList<>();
        queue.add(root);
        
        // process nodes in tree
        while (!queue.isEmpty()) {
            // determine number of nodes in current level
            int levelSize = queue.size();
            
            // only process up to number of nodes in level
            // keeps separation between current level and queueing nodes for next level
            for (int i = 0; i < levelSize; i++) {
                Node parent = queue.remove();
                
                // queue children of current level
                for (int j = 0; j < parent.children.size(); j++) {
                    queue.add(parent.children.get(j));
                }
            }
            // increase depth after processing a level
            depth++;
        }
        return depth;
    }
}