// 1290. Convert Binary Number in a Linked List to Integer
// Difficulty: Easy
// Problem: Given head which is a reference node to a singly-linked list. T
// he value of each node in the linked list is either 0 or 1. The linked list 
// holds the binary representation of a number.

// Return the decimal value of the number in the linked list.

// Example 1:
// Input: head = [1,0,1]
// Output: 5
// Explanation: (101) in base 2 = (5) in base 10

// Example 2:
// Input: head = [0]
// Output: 0

// Example 3:
// Input: head = [1]
// Output: 1

// Example 4:
// Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
// Output: 18880

// Example 5:
// Input: head = [0,0]
// Output: 0
 

// Constraints:
// The Linked List is not empty.
// Number of nodes will not exceed 30.
// Each node's value is either 0 or 1.

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int getDecimalValue(ListNode head) {
        // simulate binary operations
        // iterate through all nodes
        // while iterating, keep track of sum
        
        // runtime: O(n): iterate through all n nodes once
        // space: O(1): int var to keep track of sum
        
        int sum = 0;
        
        while (head != null) {
            // sum starts with 0, left shift sum for 1 bit, 
            // then bitwise or with head.val.
            sum = (sum << 1) | head.val;
            // same effect as:
            // sum = sum * 2 + head.val;
            head = head.next;
        }
                
        return sum;
    }
}