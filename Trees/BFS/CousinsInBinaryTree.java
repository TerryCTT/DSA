// 993. Cousins in Binary Tree
// Difficulty: Easy
// Problem:

// In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

// Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

// We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

// Return true if and only if the nodes corresponding to the values x and y are cousins.

// Example 1:
// Input: root = [1,2,3,4], x = 4, y = 3
// Output: false

// Example 2:
// Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
// Output: true

// Example 3:
// Input: root = [1,2,3,null,4], x = 2, y = 3
// Output: false

// Constraints:
// The number of nodes in the tree will be between 2 and 100.
// Each node has a unique integer value from 1 to 100.

// runtime: O(n): worst case we iterate through all nodes in tree
// space: O(n): queue max size will be bottom 2 levels of a tree
//              for a full tree: 2^maxDepth + 2^(maxDepth - 1)

import java.util.LinkedList; 
import java.util.Queue;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isCousins(TreeNode root, int x, int y) {
        // Breadth-first Search, we queue nodes of the same level
        // First check if a node is parent of both x and y
        //    if true, we know x and y are siblings (return false)
        // Queue all children nodes of next level
        //    not cousins if we process a level and only x or y in queue (return false)        
        boolean xFound = false;
        boolean yFound = false;
        TreeNode parent;
        
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        
        // process nodes in tree
        while (!queue.isEmpty()) {
            // determine number of nodes in level
            int levelSize = queue.size();
            
            // only process up to number of nodes in level
            // keeps separation between current level and queueing nodes for next level
            for (int i = 0; i < levelSize; i++) {
                parent = queue.remove();
                
                // check if parent is either x or y
                if (parent.val == x) {
                    xFound = true;
                } else if (parent.val == y) {
                    yFound = true;
                }
                
                // check if parent's children exist and if they're siblings
                if (parent.left != null && parent.right != null) {
                    if ((parent.left.val == x && parent.right.val == y)
                       || (parent.left.val == y && parent.right.val == x)) {
                        return false;
                    }
                }
                
                // prepare next level of tree
                if (parent.left != null) {
                    queue.add(parent.left);
                }
                if (parent.right != null) {
                    queue.add(parent.right);
                }
            }
            // either x or y found (won't need to process next level)
            if (xFound || yFound) {
                // they're cousins
                if (xFound && yFound) {
                    return true;
                }
                // they're on different levels
                return false;
            }
        }
        
        return false;
    }
}