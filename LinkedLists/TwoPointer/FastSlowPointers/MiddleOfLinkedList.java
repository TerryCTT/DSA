// 876. Middle of the Linked List
// Difficulty: Easy
// Problem:

// Given a non-empty, singly linked list with head node head, return a middle node of linked list.

// If there are two middle nodes, return the second middle node.

// Example 1:
// Input: [1,2,3,4,5]
// Output: Node 3 from this list (Serialization: [3,4,5])
// The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
// Note that we returned a ListNode object ans, such that:
// ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

// Example 2:
// Input: [1,2,3,4,5,6]
// Output: Node 4 from this list (Serialization: [4,5,6])
//Since the list has two middle nodes with values 3 and 4, we return the second one.

// runtime: O(n): iterate through all nodes to check if next exists
// space: O(1): constant space, use two pointers

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
    public ListNode middleNode(ListNode head) {
        // use two pointers
        // first pointer will be "slow" and iterate through nodes one at a time
        // second pointer will be "fast" and iterate through nodes two at a time
        // by the the time fast pointer reaches end (fast.next == null), then
        // slow pointer will be at halfway point
        
        // initialize both pointers to head
        ListNode slow = head;
        ListNode fast = head;
        
        // if next exists, increment both fast and slow
        while (fast.next != null) {
            fast = fast.next;
            slow = slow.next;
            // increment fast pointer an additional time to keep ahead of slow 
            if (fast.next != null){
                fast = fast.next;
            }
        } 
        // slow will be at mid point
        return slow;
    }
}