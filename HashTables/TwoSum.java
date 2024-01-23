// 1. Two Sum
// Difficulty: Easy
// Problem:
// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// You can return the answer in any order.

// Example 1:

// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
// Example 2:

// Input: nums = [3,2,4], target = 6
// Output: [1,2]
// Example 3:

// Input: nums = [3,3], target = 6
// Output: [0,1]

// Constraints:
// 2 <= nums.length <= 10^4
// -10^9 <= nums[i] <= 10^9
// -10^9 <= target <= 10^9
// Only one valid answer exists.
 

// Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

// Topics: Array, Hash Table

// =====================================================================================

// Intuition:
// We can solve naively by checking each element in nums against all other elements in nums and see if their sum is equal to target. This would be O(n^2) time complexity.
// We can improve on this by instead checking only once for each element in nums by calculating the difference between target and the element and seeing if that difference exists in the array. To check this difference in constant time we would have to use a hashmap

import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Approach:
        // (1) Create an array to store our solution: The indices of the two elements that add up to our target
        // (2) Create a hashmap to store the array element values and their corresponding indices within the hashmap as Key: element value and Value: index
        // (3) Iterate through elements of array, checking if the difference between the target and current element's value exists as a key within the hashmap.
        // (4) If the difference exists as a key within the hashmap, store the difference's array index and the current element's index in the solution array
        // (5) If the difference is not a key within the hashmap, store the current element's value and its index to the hashmap
        // (6) Return the array we created with the solution indices.

        // time complexity: O(n). Worst case: iterate over all elements of nums
        // space complexity: O(n). Worst case: store all but last element of nums into hashmap. Solution array is always created
        int[] solution = new int[2]; // (1)
        HashMap<Integer, Integer> table = new HashMap<>(); // (2)

        for (int i = 0; i < nums.length; i++) { // (3)
            if (table.containsKey(target - nums[i])) { // (4)
                solution[0] = table.get(target - nums[i]);
                solution[1] = i;
                break; // We can stop iterating through the array since we have found our solution
            }
            else { // (5)
                table.put(nums[i], i);
            }
        }

        return solution; // (6)
    }
}