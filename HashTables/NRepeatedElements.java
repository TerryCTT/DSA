// 961. N-Repeated Element in Size 2N Array
// Difficulty: Easy
// Problem:
// In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

// Return the element repeated N times.

// Example 1:
// Input: [1,2,3,3]
// Output: 3

// Example 2:
// Input: [2,1,2,5,3,2]
// Output: 2

// Example 3:
// Input: [5,1,5,2,5,3,5,4]
// Output: 5

import java.util.*;

class Solution {
    public int repeatedNTimes(int[] A) {
        // Create a hashmap
        // interate through elements of array, checking if it exists in hashmap
        // if exists, return that element since only one duplicate number in array
        // otherwise, store into hashmap
        HashMap<Integer, Integer> nums = new HashMap<Integer, Integer>();
        
        for (int i = 0; i < A.length; i++) {
            // if exists, return that element since only one duplicate number in array
            if (nums.containsKey(A[i])) {
                return A[i];
            } else {
                nums.put(A[i], 1);
            }
        }
        
        // impossible for value to not have been found if correct input array
        // but return -1 if no duplicate is found
        return -1;
    }
}