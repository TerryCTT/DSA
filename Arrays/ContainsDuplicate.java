// 217. Contains Duplicate
// NeetCode: Arrays & Hashing 1/9
// Solved on 1/29/24
// Difficulty: Easy
// Problem: 
// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

// Example 1:

// Input: nums = [1,2,3,1]
// Output: true
// Example 2:

// Input: nums = [1,2,3,4]
// Output: false
// Example 3:

// Input: nums = [1,1,1,3,3,4,3,2,4,2]
// Output: true
 

// Constraints:

// 1 <= nums.length <= 10^5
// -10^9 <= nums[i] <= 10^9

// Topics: Arrays, Hash Table

// =====================================================================================

// Intuition:
// We can solve naively by checking each element in nums against all other elements in nums and see if there exist any duplicates. This would be O(n^2) time complexity.
// We can improve on this by instead checking only once for each element in nums. To check this difference in constant time we would have to use a hashset

class Solution {
    public boolean containsDuplicate(int[] nums) {
        // Approach:
        // (1) Create a hashset to store the array element values
        // (2) Iterate through elements of array, checking if the element's value exists within the hashset
        // (3) If the element's value exists within the hashset, return true since a duplicate has been found
        // (4) If the elemenet's value is not within the hashset, store the current element's value into the hashset
        // (5) Return false if we iterate through the entire array with no found duplicates

        // time complexity: O(n). Worst case: iterate over all elements of nums
        // space complexity: O(n). Worst case: store all elements of nums into hashset
       HashSet<Integer> set = new HashSet<>(); // (1)

       for (int i = 0; i < nums.length; i++) { // (2)
           if (set.contains(nums[i])) { // (3)
               return true;
           }
           else {
               set.add(nums[i]); // (4)
           }
       }
       return false; // (5)
    }
}