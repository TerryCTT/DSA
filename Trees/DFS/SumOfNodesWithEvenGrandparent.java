// 1315. Sum of Nodes with Even-Valued Grandparent
// Difficulty: Medium
// Problem:
// Given a binary tree, return the sum of values of nodes with even-valued grandparent.  
// (A grandparent of a node is the parent of its parent, if it exists.)

// If there are no nodes with an even-valued grandparent, return 0.

// Example 1:
// Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
// Output: 18
// Explanation: The red nodes are the nodes with even-value grandparent 
// while the blue nodes are the even-value grandparents.
 

// Constraints:
// The number of nodes in the tree is between 1 and 10^4.
// The value of nodes is between 1 and 100.

// runtime: O(n): traverse all nodes in tree
// space: O(h): call stack reaches height h of tree

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
    public int sumEvenGrandparent(TreeNode root) {
        // DFS
        // Keep track of a sum, as well as parent and grandparent
        // If grandparent is even, add node's current value to sum
        int sum = 0;
        sum = dfs(root, null, null, sum);
        return sum;
    }
    
    public int dfs(TreeNode node, TreeNode parent, TreeNode grandparent, int sum) {
        // base case
        if (node == null) {
            return 0;
        }
        
        // increase sum by values of left and right children who have even grandparents
        sum += dfs(node.left, node, parent, sum) + dfs(node.right, node, parent, sum);
        
        // increase sum by value of current node if grandparent is even
        if (grandparent != null && grandparent.val % 2 == 0) {
            sum += node.val;
        }
        return sum;
    }
}