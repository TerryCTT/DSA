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
// space: O(h): hashtable to store parent and level of x and y node
//              as well as maximum height h of tree for call stack

import java.util.HashMap;
import java.util.Map;

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
        // Depth-first Search
        // Create a hashtable to store parent and levle of x and y node
        // Recursively check (DFS-preorder) if node is x or y
        //    if so: store x or y as key and values [level, parent]     
        // Compare x and y's parents and level once both are found
        //    not cousins if same parent or different levels        
        Map<Integer, int[]> map = new HashMap<>();

        dfs(root, 0, 0, x, y, map);
        return ((map.get(x)[0] == map.get(y)[0]) && (map.get(x)[1] != map.get(y)[1]));
    }
    public void dfs(TreeNode root, int level, int parent, int x, int y, Map<Integer, int[]> map) {
        // base case
        if (root == null || map.size() == 2) {
            return;
        }

        // preorder traversal of tree
        if (root.val == x || root.val == y) {
            map.put(root.val, new int[]{level, parent});
        }
        dfs(root.left, level + 1, root.val, x, y, map);
        dfs(root.right, level + 1, root.val, x, y, map);
        return;
    }
}