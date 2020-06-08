// 1302. Deepest Leaves Sum
// Difficulty: Medium
// Problem:
// Given a binary tree, return the sum of values of its deepest leaves.

// Example 1:
// Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
// Output: 15
 

// Constraints:
// The number of nodes in the tree is between 1 and 10^4.
// The value of nodes is between 1 and 100.

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
    int levelSum = 0;
    int maxDepth = 0;
    public int deepestLeavesSum(TreeNode root) {
        // DFS
        // traverse through tree to find max level and add value of
        // nodes at max level to sum
        
        // runtime: O(n): traverse through all nodes of tree once
        // space: O(h): call stack reaches height of tree 
        
        dfs(root, 0);
        return levelSum;
    }
    
    private void dfs(TreeNode node, int level) {
        // base case
        if (node == null) {
            return;
        }
        
        // true if we've reached a deeper level
        if (level > maxDepth) {
            maxDepth = level;
            levelSum = 0;
        }
        
        // add val to sum only if no children (potentially deepest level of tree)
        // and know we are potentially at the deepest level
        if (node.left == null && node.right == null && level == maxDepth) {
            levelSum += node.val;
        }
        
        dfs(node.left, level + 1);
        dfs(node.right, level + 1);   
    }
}