// 938. Range Sum of BST
// Difficulty: Easy
// Problem: Given the root node of a binary search tree, 
// return the sum of values of all nodes with value between L and R (inclusive).

// The binary search tree is guaranteed to have unique values.

// Example 1:
// Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
// Output: 32

// Example 2:
// Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
// Output: 23

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    int sum = 0;
    public int rangeSumBST(TreeNode root, int L, int R) {
        // DFS pre-order
        // If root's val is between L and R (inclusive) add to sum
        // Due to nature of BST: 
        // If val is less than L, we know all values left are less than L
        // and if val is greater than R, we know all values right are greater than R
        // so we won't need to traverse through those nodes
        
        // runtime: O(n): iterate through all nodes n
        // space: O(h): callstack reaches at most height h of tree 
        dfs(root, L, R);
        return sum;
    }
    
    public void dfs(TreeNode root, int L, int R) {
        // base case
        if (root == null) {
            return;
        }
        // add val to sum if within bounds L and R
        // check appropriate nodes, due to nature of BST: 
        // If val is less than L, we know all values left are less than L
        // and if val is greater than R, we know all values right are greater than R
        // so we won't need to traverse through those nodes
        if (root.val >= L && root.val <= R) {
            sum += root.val;
            dfs(root.left, L, R);
            dfs(root.right, L, R);
        } else if (root.val >= L) {
            dfs(root.left, L, R);
        } else if (root.val <= R) {
            dfs(root.right, L, R);
        }
        
        return;
    }
}